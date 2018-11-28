#include <stdio.h>
#include <algorithm>
using namespace std;
int c[1010];
int main() {
    int T, ri = 1, n, t, i, ans, res;
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while (T--) {
        scanf("%d", &n);
        for (i = 0; i < n; i++) scanf("%d", &c[i]);
        ans = 1000;
        for (t = 1; t < ans; t++) {
            res = t;
            for (i = 0; i < n; i++) {
                res += (c[i] + t - 1) / t - 1;
            }
            ans = min(ans, res);
        }
        printf("Case #%d: %d\n", ri++, ans);
    }
    return 0;
}
