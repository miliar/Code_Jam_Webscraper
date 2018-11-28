#include <bits/stdc++.h>
using namespace std;
const int MAXN = 300;
int TC, N, K;
double P[MAXN];
double m[MAXN][MAXN];
bool v[MAXN][MAXN];
vector<double> p;
double dp(int n, int y) {
    if (y > n) return 0.0;
    if (y < 0) return 0.0;
    if (n == 0 && y == 0) return 1.0;
    if (v[n][y]) return m[n][y];
    v[n][y] = 1;
    m[n][y] = dp(n-1, y) * (1.0 - p[n-1]) + dp(n-1, y-1) * p[n-1];
    return m[n][y];
}
int main() {
    scanf("%d", &TC);
    for (int T = 1; T <= TC; ++T) {
        scanf("%d%d", &N, &K);
        double ans = 0.0;
        for (int i = 0; i < N; ++i) scanf("%lf", &P[i]);
        sort(P, P+N);
        for (int k1 = 0; k1 <= K; ++k1) {
            p.clear();
            memset(v, 0, sizeof v);
            for (int i = 0; i < k1; ++i) {
                p.push_back(P[i]);
            }
            for (int i = 0; i < K-k1; ++i) {
                p.push_back(P[N-i-1]);
            }
            assert(p.size() == K);
            if (dp(K, K/2) > ans) {
                ans = max(dp(K, K/2), ans);
                /*
                for (int i = 0; i < p.size(); ++i) {
                    printf("%.2lf ", p[i]);
                }
                printf("%d+%d: %.6lf\n", K, K/2, dp(K, K/2));
                */
            }
        }
        printf("Case #%d: %.9lf\n", T, ans);
    }
}