#include <cstdio>
#include <cstring>
#include <iostream>

#define _N 1010

using namespace std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int m[_N], t, n;
    scanf("%d", &t);
    for (int cas = 1; cas <= t; ++cas) {
        scanf("%d", &n);
        int ret = 0, lim = 0;
        for (int i = 0; i < n; ++i) {
            scanf("%d", &m[i]);
            if (i > 0 && m[i] < m[i - 1]) {
                ret += m[i - 1] - m[i];
                lim = max(lim, m[i - 1] - m[i]);
            }
        }
        printf("Case #%d: %d", cas, ret);
        ret = 0;
        for (int i = 0; i < n - 1; ++i) {
            ret += min(m[i], lim);
        }
        printf(" %d\n", ret);
    }

    return 0;
}
