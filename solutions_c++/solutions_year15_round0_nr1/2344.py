#include <cstdio>
#include <cstring>

#define _N 0x1000

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    char buf[_N];
    int t;

    scanf("%d", &t);
    for (int cas = 1; cas <= t; ++cas) {
        int n, ret = 0;
        scanf("%d%s", &n, buf);
        int cur = buf[0] - '0';
        for (int i = 1; i <= n; ++i) {
            if (buf[i] == '0') continue;
            if (cur >= i) {
                cur += buf[i] - '0';
            }
            else {
                ret += i - cur;
                cur = i + buf[i] - '0';
            }
        }

        printf("Case #%d: %d\n", cas, ret);
    }

    return 0;
}
