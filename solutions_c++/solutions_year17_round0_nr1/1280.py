#include <cstdio>
#include <cstring>


char s[1010];

int main() {
    int T = 0;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        int k = 0;
        scanf("%s%d", s, &k);
        int n = strlen(s);
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (s[i] == '-') {
                if (i + k > n) {
                    ans = -1;
                    break;
                }
                for (int j = i; j < i + k; j++)
                    if (s[j] == '-') s[j] = '+';
                    else s[j] = '-';
                ans++;
            }
        }
        if (ans == -1) printf("Case #%d: IMPOSSIBLE\n", cas);
        else printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
