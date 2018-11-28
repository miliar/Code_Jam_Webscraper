#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int n, m;
double p[205];

vector<double> v;
double dp[205][205];
double tie(int yes, int idx) {
    if (dp[yes][idx] != -1.0)
        return dp[yes][idx];
    if (idx == v.size())
        return dp[yes][idx] = 2 * yes == v.size() ? 1.0 : 0.0;
    return dp[yes][idx] = v[idx] * tie(yes+1, idx+1)
                        + (1.0 - v[idx]) * tie(yes, idx+1);
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d %d", &n, &m);
        for (int i = 0; i < n; i++)
            scanf("%lf", &p[i]);
        double ans = 0.0;
        for (int mask = 0; mask < 1 << n; mask++) {
            if (__builtin_popcount(mask) != m) continue;
            v.clear();
            for (int k = 0; k < n; k++)
                if (mask >> k & 1)
                    v.push_back(p[k]);
            for (int i = 0; i <= n; i++)
                for (int j = 0; j <= n; j++)
                    dp[i][j] = -1.0;
            ans = max(ans, tie(0, 0));
        }
        printf("Case #%d: %.7lf\n", t, ans);
    }
}
