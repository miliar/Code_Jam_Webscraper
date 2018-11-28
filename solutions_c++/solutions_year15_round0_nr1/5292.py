#include <bits/stdc++.h>
using namespace std;

char s[1005];
int main(){
    freopen("A-large.in", "rt", stdin);
    freopen("out2.txt", "wt", stdout);
    int T , z ,cas = 0;
    scanf("%d",&T);
    while(T--){
       scanf("%d%s",&z,s);
       int Min = 0 ;
       int cnt = 0 ;
       for(int i = 0 ; i <= z ; i++){
           if(cnt >= i){
                cnt += (s[i]-'0');
           }else{
                Min += (i-cnt);
                cnt += (i-cnt);
                cnt += (s[i]-'0');
           }
       }
       printf("Case #%d: %d\n",++cas,Min);
    }
}
