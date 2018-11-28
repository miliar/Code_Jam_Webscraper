#include <cstdio>
#include <algorithm>
#include <cstdlib>
using namespace std;
const int MAXN = 1000 + 3;
const int INF = 1000000000;
int a[MAXN];
int main()
{
    int T;
    scanf("%d", &T);
    for (int kase = 1; kase <= T; ++kase) {
        int n;
        scanf("%d", &n);
        int lim = 0;
        for (int i = 0; i < n; ++i) {
            scanf("%d", &a[i]);
            lim = max(lim, a[i]);
        }
        int ans = INF;
        for (int i = 1; i <= lim; ++i) {
            int cur = 0;
            for (int j = 0; j < n; ++j) {
                int t = a[j] - i;
                if (t > 0) {
                    int k = t / i;
                    if (t % i != 0) ++k;
                    cur += k;
                }
            }
            cur += i;
            ans = min(ans, cur);
        }
        printf("Case #%d: %d\n", kase, ans);
    }
    return 0;
}

