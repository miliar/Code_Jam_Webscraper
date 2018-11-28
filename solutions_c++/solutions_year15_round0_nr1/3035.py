#include <cstdio>

int n;
char s[1111];

int main() {
    int T;
    scanf("%d", &T);
    for (int kase = 0; kase < T; ++ kase) {
        scanf("%d%s", &n, s);
        for (int a = 0; a <= n; ++ a) {
            int c = a;
            bool chk = true;
            for (int i = 0; i <= n; ++ i) {
                if (c >= i) {
                    c += s[i] - '0';
                } else if (s[i] != '0') {
                    chk = false;
                    break;
                }
            }
            if (chk) {
                printf("Case #%d: %d\n", kase + 1, a);
                break;
            }
        }
    }
    return 0;
}
