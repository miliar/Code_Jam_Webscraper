#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<ll, int> pli;

int T, n;
ll B;
ll x[40];

int main() {
    scanf("%d", &T);
    for (int caseNum = 1; caseNum <= T; ++caseNum) {
        scanf("%lld%d", &B, &n);
        memset(x, 0, sizeof(x));
        for (int i = 0; i < n; ++i) {
            scanf("%lld", &x[i]);
        }
        sort(x, x + 37);
        double res = 0.0;
        for (int i = 0; i <= 36; ++i) {
            int leastCount = 0;
            ll need = 0;
            for (int j = 0; j <= i; ++j) {
                leastCount += 1;
                need += x[i] - x[j];
            }
            if (need > B) {
                continue;
            }
            ll b = B - need;
            ll pl = x[i] - 1, pr = 10000000000000LL;
            while (pl + 1 < pr) {
                ll pm = pl + (pr - pl) / 2;
                ll curCost = leastCount * (pm - x[i]);
                for (int j = i + 1; j <= 36; ++j) {
                    if (x[j] < pm + 1) {
                        curCost += pm + 1 - x[j];
                    }
                }
                if (curCost > b) {
                    pr = pm;
                } else {
                    pl = pm;
                }
            }

            ll usable = 0;
            for (int j = 0; j <= i; ++j) {
                usable += pl - x[j];
            }
            ll cost = leastCount * (pl - x[i]);
            for (int j = i + 1; j <= 36; ++j) {
                if (x[j] < pl + 1) {
                    cost += pl + 1 - x[j];
                }
            }
            //printf("%lld %lld %lld %lld %d\n", pl, usable, need, cost, leastCount);
            double profit = usable * 36.0 / leastCount - need - cost;
            res = max(res, profit);
        }
        printf("Case #%d: %.13f\n", caseNum, res);
    }
    return 0;
}
