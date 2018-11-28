#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <set>
using namespace std;

int charArr[30];
int charArr2[30];
int charArrC[30];
int charArr2C[30];
//set<string> strSet;

int main(){
    int tCase;
    cin >> tCase;
    for(int cCase = 1;cCase <= tCase;cCase++){
        int result = 0;
        bool fw = false;
        memset(charArr,0,sizeof(charArr));
        memset(charArr2,0,sizeof(charArr));
        memset(charArrC,0,sizeof(charArr));
        memset(charArr2C,0,sizeof(charArr));
        
        int n;
        bool init = false;
        int pt1 = 0;
        int pt2 = 0;
        string str,str2;
        cin >> n;
        
            cin >> str >> str2;
            
            //cout << str << " " << str2 << endl;
            
            while(!(pt1 >= str.size() && pt2 >= str2.size())){
                if(str[pt1] == str[pt1+1] && str2[pt2] == str2[pt2+1]){
                    pt1++;
                    pt2++;
                    continue;
                }
                if(str[pt1] == str[pt1+1]){
                    result += 1;
                    pt1++;
                    continue;
                }
                if(str2[pt2] == str2[pt2+1]){
                    result += 1;
                    pt2++;
                    continue;
                }
                
                //cout << "pt1 " << pt1 << " " << str[pt1] << " ";
                //cout << "pt2 " << pt2 << " " << str2[pt2] << endl;
                
                if(str[pt1] != str2[pt2]){
                    fw = true;
                    break;
                }
                pt1++;
                pt2++;
           
                
            }
        
            /*for(int j=0;j<str.size()-1;j++){
                int chNum = str[j] - 'a';
                int chNum2 = str[j+1] - 'a';
                
                if(!init){
                    if(chNum == chNum2){
                        
                        //cout << chNum << " "<< chNum2 << " | ";
                        
                        charArr[chNum]++;
                    }
                    charArrC[chNum] = 1;
                        

                }
                else{
                    if(chNum == chNum2)
                        charArr2[chNum]++;
                    charArr2C[chNum] = 1;
                    
                
                }
                
                
                
            }
            if(init){
                for(int j=0;j<30;j++){
                
                    if((charArrC[j] == 0 && charArr2C[j] > 0) || (charArrC[j] >0 && charArr2C[j] == 0)){
                        fw = true;
                        break;
                    }
                    
                    else{
                        if(charArr[j] > charArr2[j]){
                            result += charArr[j] - charArr2[j];
                        }
                        else{
                            result += charArr2[j] - charArr[j];
                        }
                    }
                    
                        
                }
            }
            
            init = true;
        }
        */
        
        if(fw){
            cout << "Case #" << cCase << ": " << "Fegla Won"<< endl;
            
        }
        else
        cout << "Case #" << cCase << ": " << result << endl;
    }
}