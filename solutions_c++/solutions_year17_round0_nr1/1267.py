#include<cstdio>
#include<cstring>

int main() {
    
    int T, k;
    char s[1024];
    scanf("%d", &T);
    for(int ca=1; ca<=T; ca++) {
        scanf("%s%d", s, &k);
        int ans = 0, len = strlen(s);
        for(int i=0; s[i]; i++) {
            if(s[i] == '-') {
                if(len - i < k) {
                    ans = -1;
                    break;
                }
                for(int j=0; j<k; j++)
                    s[i+j] ^= 6;
                ans++;
            }
        }
        printf("Case #%d: ", ca);
        if(~ans)    printf("%d\n", ans);
        else puts("IMPOSSIBLE");

    }
    return 0;
}
