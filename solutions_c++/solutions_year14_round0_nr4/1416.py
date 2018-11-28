#include <bits/stdc++.h>
using namespace std;

set<double> s;
double a[1010], b[1010];

int dp[1010][1010];

int f(int x, int y) {
    if (x < 0 || y < 0) return 0;
    return dp[x][y];
}

int main() {
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            scanf("%lf", &a[i]);
        }
        sort(a, a + n);
        for (int i = 0; i < n; i++) {
            scanf("%lf", &b[i]);
            s.insert(b[i]);
        }
        sort(b, b + n);
        int pts1 = 0;
        set<double> :: iterator pos;
        for (int i = n - 1; i >= 0; i--) {
            if ((pos = s.lower_bound(a[i])) == s.end()) {
                pts1++;
                s.erase(s.begin());
            } else {
                s.erase(pos);
            }
        }
        memset(dp, 0, sizeof(dp));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dp[i][j] = max(dp[i][j], f(i - 1, j));
                dp[i][j] = max(dp[i][j], f(i, j - 1));
                if (a[i] > b[j]) {
                    dp[i][j] = max(dp[i][j], f(i - 1, j - 1) + 1);
                }
            }
        }
        int pts0 = dp[n - 1][n - 1];
        printf("Case #%d: %d %d\n", cas, pts0, pts1);
    }
    return 0;
}
