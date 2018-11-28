#include <stdio.h>
#include <iostream>

using namespace std;

int main(){
    freopen("a.large.in", "r", stdin);
    freopen("a.large.out", "w", stdout);
    int T,s_max;
    char s[1001];
    while(scanf("%d",&T)!=EOF){
        for(int k=1;k<=T;k++){
            scanf("%d %s",&s_max,s);
            int total = s[0]-'0',need = 0;
            for(int i=1;i<=s_max;i++){
                if(total<i){
                    need += i - total;
                    total = i;
                }
                total += s[i] - '0';
            }
            printf("Case #%d: %d\n",k,need);
        }
    }
    return 0;
}
