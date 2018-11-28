#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

const int N = 205;

int num[1 << 4];
double p[N];
double f[N][N];
double pi[N];

double solve(int n) {
    memset(f, 0, sizeof(f));
    f[0][0] = 1;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j <= n; ++j) {
            f[i + 1][j] += f[i][j] *(1 - pi[i + 1]);
            f[i + 1][j + 1] += f[i][j] * pi[i + 1];
        }
    return f[n][n / 2];
}

int main() {
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    int T;
    scanf("%d", &T);
    while (T--) {
        int n, m;
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; ++i)
            scanf("%lf", &p[i]);
        sort(p, p + n);
        double ans = 0;
        for (int i = 0; i <= m; ++i) {
            int l = i, r = m - i;
            int t = 0;
            for (int j = 0; j < l; ++j)
                pi[++t] = p[j];
            for (int j = 0; j < r; ++j)
                pi[++t] = p[n - j - 1];
            ans = max(ans, solve(m));
        }
        static int ca = 0;
        printf("Case #%d: %.10f\n", ++ca, ans);
    }
    return 0;
}
