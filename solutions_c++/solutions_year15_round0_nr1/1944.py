#include <cstdio>

char s[1010];

int main() {
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        int n;
        scanf("%d%s", &n, s);
        int ans = 0;
        int cur = 0;
        for (int i = 0; s[i] != '\0'; i++) {
            int si = s[i] - '0';
            cur += si;
            if (cur < i + 1) {
                ans++;
                cur++;
            }
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
