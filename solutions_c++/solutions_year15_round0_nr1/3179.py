#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(){
    int T;
    scanf("%d", &T);
    for(int _ = 1 ; _ <= T; ++_){
        int n;
        static char str[1024];
        scanf("%d%s", &n, str);
        printf("Case #%d:", _);
        for(int ans = 0; ans < 1024; ++ans){
            int u = ans;
            bool isok = true;
            for(int i = 0; i <= n; ++i){
                int v = str[i] - '0';
                if(i > u){
                    isok = false;
                    break;
                }
                u += v;
            }
            if(isok) {
                printf(" %d\n", ans);
                break;
            }
        }
    }
}
