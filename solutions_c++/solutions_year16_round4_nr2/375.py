#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 1000;

int n, k;
double P[N];

double DP(const vector<double> vec) {
    double dp[N][N];
    dp[0][0] = 1;
    for(int i = 0; i < k; ++i) {
        for(int j = 0; j < k; ++j)
            for(int u = 0; u < k; ++u) {
                dp[j + 1][u] = dp[j][u] * vec[i];
                dp[j][u + 1] = dp[j][u] * (1 - vec[i]);

            }
    }
    return dp[k / 2][k / 2];
}
int main() {
    freopen("in.txt", "r", stdin);
    freopen("B.txt", "w", stdout);
    int _, cas = 1;
    for(scanf("%d", &_); _--; ) {
        printf("Case #%d: ", cas++);
        scanf("%d %d", &n, &k);
        for(int i = 0; i < n; ++i) scanf("%lf", P + i);
        sort(P, P + n);

        double ans = 0;
        for(int i = 0; i <= k; ++i) {
            int j = k - i;
            vector<double> vec;
            for(int L = 0; L < i; ++L) vec.push_back(P[L]);
            for(int R = n - 1; R > n - j; --R) vec.push_back(P[R]);
            ans = max(ans, DP(vec));
        }

        printf("%.10f\n", ans);
    }
    return 0;
}
