#include<cstdio>
#include<cstring>

char S[1000];
int T;

int main() {
    scanf("%d", &T);
    for(int cas = 1; cas <= T; cas++) {
        scanf("%s", S);
        printf("Case #%d: ", cas);
        int ans = 0;
        for(int i = 0; S[i]; i++) {
            if(S[i] == '-' &&(i == 0 || S[i - 1] == '+')) {
                ans++;
            }
        }
        ans *= 2;
        if(S[0] == '-') ans--;
        printf("%d\n", ans);
    }
    return 0;
}