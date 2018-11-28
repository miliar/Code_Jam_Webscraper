#include <bits/stdc++.h>

using namespace std;

int n, k;
double p[200];

double f[201][201];

double calc(vector<double>& pi) {
    memset(f, 0x00, sizeof(f));
    f[0][0] = 1.0;
    for(int i = 0; i < k; ++i)
        for(int j = 0; j <= i && j <= k / 2; ++j) {
            f[i + 1][j + 1] += f[i][j] * pi[i];
            f[i + 1][j] += f[i][j] * (1.0 - pi[i]);
        }
    return f[k][k / 2];
}

int main() {

    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int T;
    cin >> T;

    for (int test = 1; test <= T; ++test) {

        cin >> n >> k;
        for (int i = 0; i < n; ++i) {
            cin >> p[i];
        }

        sort(p, p + n);

        double res = 0;

        for (int i = 0; i <= k; ++i) {
            vector<double> b;
            for (int j = 0; j < i; ++j) {
                b.push_back(p[j]);
            }
            for (int j = 0; j < k - i; ++j) {
                b.push_back(p[n - 1 - j]);
            }
            res = max(res, calc(b));
        }

        printf("Case #%d: %.12lf\n", test, res);

    }

    return 0;
}
