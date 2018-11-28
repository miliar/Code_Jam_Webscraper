#include<cstdio>

int main() {
    int T;
    scanf("%d", &T);
    for(int ca=1; T--; ca++) {
        char S[101], pre;
        int ans = 0;
        scanf("%s", S);
        pre = S[0];
        for(int i=0; S[i]; i++) {
            if(pre != S[i]) {
                pre = S[i];
                ans++;
            }
        }
        if(pre == '-')
            ans++;
        printf("Case #%d: %d\n", ca, ans);
        
    }
    return 0;
}
