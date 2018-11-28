#include<iostream>
#include<string>
#include<cstring>
#include<vector>
#include<set>
#include<map>
#include<cstdio>
#include<cmath>
#include<algorithm>
using namespace std;
int taken[11];
char str[10000];
char temp[10000];
int main(){
    freopen("input.txt","r",stdin);
      freopen("output.txt","w",stdout);
    string str,ch,temp;
    int counter,i,j,x,y,rem,t,testcase;
    char c;
    cin>>testcase;
    for( t = 1; t <= testcase; t++){

        for( j = 0; j <= 9; j++){
            taken[j] = 0;
        }
        cin>>str;
        if( str == "0"){
            printf("Case #%d: INSOMNIA\n",t);
        }
        else{
            counter = 0;
            for( i = 0; i < str.size(); i++){
                x = str[i] - '0';
                if( taken[x] == 0){
                    taken[x] = 1;
                    counter++;
                }
            }
            ch = "";
            for( i = str.size() - 1; i >=0 ;i--){
                ch = ch + str[i];
            }
            str = ch;
            while( true ){
                if( counter == 10 ){
                    break;
                }
                temp = "";
                i = 0;
                j = 0;
                rem = 0;
                while( i < str.size()){

                     if( j < ch.size() ){
                        x = ch[j] - '0';
                        j++;
                     }
                     else{
                        x = 0;
                     }
                     y = str[i] - '0';
                     x = rem + x + y;
                     rem = x / 10;
                     x = x % 10;
                     if( taken[x] == 0){
                        taken[x] = 1;
                        counter++;
                     }
                     c = x + '0';
                     temp = temp + c;
                     i++;
                }
                if( rem > 0){
                    if( taken[rem] == 0){
                        taken[rem] = 1;
                        counter++;
                     }
                     c = rem + '0';
                    temp = temp + c;
                }
                str = temp;
            }
            printf("Case #%d: ",t);
            for( j = str.size() -1 ; j>=0 ; j--){
                cout<<str[j];
            }
            printf("\n");
        }

    }
return 0;
}
