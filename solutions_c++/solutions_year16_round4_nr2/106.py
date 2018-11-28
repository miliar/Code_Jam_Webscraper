#include <bits/stdc++.h>

using namespace std;

const int Inf = 1e9 + 7;

int T, cas, n, k;

double p[205], f[205][205];

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> T;
    while (T --) {
        cin >> n >> k;
        for (int i = 0; i < n; i ++) {
            scanf("%lf", &p[i]);
        }
        sort(p, p + n);
        double mx = 0.0;
        for (int l = 0; l <= k; l ++) {
            vector<double> v;
            for (int i = 0; i < l; i ++)
                v.push_back(p[i]);
            for (int i = n - 1; i >= n - (k - l); i --)
                v.push_back(p[i]);
            memset(f, 0, sizeof(f));
            f[0][0] = 1.0;
            for (int i = 1; i <= k; i ++) {
                for (int j = 0; j <= i; j ++) {
                    f[i][j] += f[i - 1][j] * (1 - v[i - 1]);
                    if (j) f[i][j] += f[i - 1][j - 1] * v[i - 1];
                }
            }
            mx = max(mx, f[k][k / 2]);
        }
        printf("Case #%d: %.6f\n", ++ cas, mx);
    }
}
