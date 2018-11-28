#include <bits/stdc++.h>
using namespace std;
int main(){
    freopen("input.txt","r",stdin) ;
    freopen("output.txt","w",stdout) ;
    int T , i , l , u , CASE = 0 ; cin >> T ;
    while(T--){
        char s[10000] ; scanf("%d %s",&u,s) ;
        int k = 0 , ret = 0 ; l = strlen(s) ;
        for(i = 0 ; i < l ; i++){
            if(k>=i){
            }
            else{
                ret += (i-k) ;
                k += (i-k) ;
            }
            k += (s[i] - '0') ;
        }
        printf("Case #%d: %d\n",++CASE,ret) ;
    }
}
