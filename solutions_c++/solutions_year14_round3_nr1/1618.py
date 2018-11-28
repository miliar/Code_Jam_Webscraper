#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

typedef __int64 lld;
int main() {
    int T;
    lld n, m;
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        scanf("%I64d/%I64d", &n, &m);
        bool ok = false;
        lld d = __gcd(n, m);
        n /= d; m /= d;
        for (lld i = 1; i <= m; i <<= 1) {
            if (m == i) {
                ok = true; break;
            }
        }
        printf("Case #%d: ", cas);
        if (!ok) {
            printf("impossible\n");
            continue;
        }
        int cnt;
        double ans = 1.0 * n / m;
        for (lld i = 1; i <= 40; i++) {
            if (ans >= 1.0 / (1 << i)) {
                cnt = i; break;
            }
        }
        printf("%d\n", cnt);
    }
    return 0;
}
/*
5
1/2
3/4
1/4
2/23
123/31488
*/
