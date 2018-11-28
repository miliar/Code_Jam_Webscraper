#include<iostream>
#include<string>
#include<queue>
#include<cstring>
#include<vector>
#include<set>
#include<map>
#include<cstdio>
#include<cmath>
#include<algorithm>
using namespace std;
int main(){

    int i,present,t,testcase;
    long long counter;
    string str;
  //  freopen("input.txt","r",stdin);
 //   freopen("output.txt","w",stdout);
    scanf("%d",&testcase);
    for( t = 1; t <= testcase; t++){
        cin>>str;
        counter = 0;
        for( i = 0; i < str.size(); i++){

            if( i == 0){
                if( str[i] =='-'){
                    present = 0;
                }
                else{
                    present = 1;
                }
            }
            else{
                if(str[i] == '-'){
                    if( present == 1){
                        counter++;
                        present = 0;
                    }
                }
                if( str[i] == '+'){
                    if(present == 0){
                        counter++;
                        present = 1;
                    }
                }
            }
        }
        if( present == 0){
            counter++;
        }
        printf("Case #%d: %lld\n",t,counter);
    }
return 0;
}
