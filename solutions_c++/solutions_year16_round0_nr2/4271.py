#include <stdio.h>
#include <string.h>

int t;
char s[105];

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("outB.out", "w", stdout);
    scanf("%d", &t);
    for(int ca=1; ca<=t; ca++){
        scanf("%s", s);
        int l = strlen(s);
        int ans = 0;
        for(int i=l-1; i>=0; i--){
            int now = ((s[i]=='+'?0:1) + ans)%2;
            if(now == 1) ans ++;
        }
        printf("Case #%d: %d\n", ca, ans);
    }
    return 0;
}
