#20220829       
#print("================ 判斷是否為時間 =============================")
#判斷是否為時間_函式
def time_str_check(time_str):
    time_str = time_str.replace(' ', '') #去除字串中的空白
    #time_str = time_str.replace('\n', '')#去除字串中的空行
    # time_1 = ds.datetime.strptime('00:00:01.002',"%H:%M:%S.%f")
    import datetime as ds
    #time_str = '19:00:09'
    time_str = time_str
    
    try:                      # 使用 try，測試內容是否正確
        # print("可以判斷")
        ds.datetime.strptime(time_str, "%H:%M:%S")
        return True
    
    except:                   # 如果 try 的內容發生錯誤，就執行 except 裡的內容
        # print('time_str 發生錯誤')
        return False

#判斷是否為時間_函式測試
# time_str = '    00:00:05 '    
# print(time_str)
# print(time_str_check(time_str))


print("================== 讀取檔案 ===========================")
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
#yanjie 準備-------------------20220826準備帶參數

# path = '許院長開幕致詞_pyT-in.srt'
# path = 'test.txt'
# path = 'in-bom.txt' 
# path = 'in.txt' 
path = 'all-in.txt' 
f = None

try:   
    # 開啓檔案
    f = open(path, 'r',encoding="utf-8")
    #print(f.read())  #印出檔案裏的資料 #讀過之後面的程式碼就不能用，需要重新open。
    RealStrNum = 0    #計算有資料的字串
    RealStrList = []  #所有有資料的字串 -> 存到 list #[0]索引值從0開始。
    RealStrList1 = [] #存時間
    RealStrList2 = [] #存字串
    for line_srt in f.readlines(): #讀取一行字串        
        str_temp = line_srt.replace('\n', '') #字串\n的地方取代為空白        
        str_temp = str_temp.replace(' ', '')  #字串'空格'的地方取代為空白
        if str_temp != '':
            RealStrNum = RealStrNum + 1
            # print(str_temp + " 第 " + str(RealStrNum)) 
            RealStrList.append(str_temp) # 使用 append() 添加元素
            
            #準備兩個 list => RealStrList1 存時間，RealStrList2 存字串。
            str_CheckTF = time_str_check(str_temp) #判斷是否為時間
            if str_CheckTF == True:
                RealStrList1.append(str_temp)
            else:
                RealStrList2.append(str_temp)
        #else:
            #print("p") # 沒有資料的一行字串。 #就不要存 list 了。     
    
    #print("---------------------------------------------------")
    
    # print(len(RealStrList))
    # print(RealStrList[7]) 
    
    #將 RealStrList1 的時間資料轉成時間軸
    RealStrList1_TL = [] #存時間軸，格式如 00:01:14,000 --> 99:99:99,999
    for item_str in range(len(RealStrList1)-1): 
        RealStrList1_TL.append(RealStrList1[item_str] + ",000 --> " + RealStrList1[item_str+1] + ",000")                 
        #print(RealStrList1_TL[item_str])
    RealStrList1_TL.append(RealStrList1[len(RealStrList1)-1] + ",000 --> " + "23:59:59,000")
    #print(RealStrList1_TL[len(RealStrList1)-1])   
        
    #印出時間軸,與資料
    str_temp_out = '' #準備輸出的資料
    for item_str in range(len(RealStrList1_TL)):
        str_temp_out += str(item_str+ 1) + "\n"
        str_temp_out += RealStrList1_TL[item_str] + "\n" 
        str_temp_out += RealStrList2[item_str] + "\n\n"
        
    print(str_temp_out)
    
    path = 'all-in-output.srt'
    f = open(path, 'w' , encoding="utf-8")
    f.write(str_temp_out)
    f.close()
  
    
except IOError:
    print('ERROR: can not found ' + path)
    if f:
        f.close()
finally:
    if f:
        f.close()
 
    
    ##準備存到 list
    # list = []          ## 空列表
    # list.append('Google')   ## 使用 append() 添加元素
    # list.append('Runoob')
    # print list
    
# =============================================================================
#     str_temp = f.readline() #讀取一行字串
#     str_temp = str_temp.replace('\n', '') #字串\n的地方取代為空白
#     str_CheckTF = time_str_check(str_temp) #判斷是否為時間
#     print(str_temp) 
#     print(str_CheckTF) 
#     print("---------------------------------------------------")
#     print(f.readline().replace('\n', '') + "a")
#     print(f.readline().replace('\n', '') + "b")
#     print(f.readline())
# 
#     print(f.readlines())
# =============================================================================
      
  