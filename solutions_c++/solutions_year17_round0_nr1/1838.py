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

    string str;
    int testcase,k,i,j,l,counter,flag;
    //freopen("input.txt","r",stdin);
  //  freopen("output.txt","w",stdout);
    scanf("%d",&testcase);
    for( int t = 1; t <= testcase; t++ ){
        cin>>str>>k;
        counter = 0;
        flag = true;
        l = str.size();
        for( i = 0; i <= l - k; i++ ){
            if( str[i] == '-'){
                for( j = i; j <= i+k-1; j++){
                    if( str[j] == '-'){
                        str[j] = '+';
                    }
                    else{
                        str[j] = '-';
                    }
                }
                counter++;
            }
        }
        for( ; i < str.size(); i++ ){
            if( str[i] == '-' ){
                flag = false;
            }
        }
        printf("Case #%d: ",t);
        if(!flag ){
            printf("IMPOSSIBLE\n");
        }
        else{
            printf("%d\n",counter);
        }
    }

return 0;
}
