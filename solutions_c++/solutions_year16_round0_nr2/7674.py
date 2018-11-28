#include<iostream>
#include<string.h>
using namespace std;
char s[100],temp[100];
int main(){
    int T,c=1,len,i,TT,stat,result,dec;
    cin>>T;
    while(T--){
        cin>>s;
        len = strlen(s);
        result = 0;
        stat = 0;
        for(i=len-1;i>=0;i--){
            if(s[i]=='-'){
                TT = i;
                stat = 1;
                break;
            }
        }
        if(stat == 0){
            TT = -1;
        }
        while(TT!=-1){
            for(i=0;i<=TT;i++){
                if(s[i]=='+'){
                    s[i] = '-';
                }else{
                    break;
                }
            }
            if(i>0){
                result++;
            }
            for(;i<=TT;i++){
                if(s[i]=='+'){
                    break;
                }
            }
            dec = i;
            {
                int i=0,j=0;
                for(i=0;i<=TT;i++){
                    if(s[i]=='-'){
                        temp[i] = '+';
                    }else{
                        temp[i] = '-';
                    }
                }
                for(j=0,i=TT;i>=0;i--,j++){
                    s[j] = temp[i];
                }
            }
            result++;
            TT -= dec;
        }
        cout<<"Case #"<<c++<<": "<<result<<"\n";
    }
    return 1;
}