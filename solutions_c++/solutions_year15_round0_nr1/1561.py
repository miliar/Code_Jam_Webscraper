#include <cstdio>

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        int n, cur = 0, ans = 0;
        char a[1005];
        scanf("%d %s", &n, a);
        for (int i = 0; a[i]; i++) {
            if (cur < i) {
                ans += i - cur;
                cur = i;
            }
            cur += a[i] - '0';
        }
        printf("Case #%d: %d\n", t, ans);
    }
}
