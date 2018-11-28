#include <iostream>
#include <algorithm>
#include <vector>
#include <cassert>
using namespace std;

int bitCount(int n) {
    return __builtin_popcount(n);
}

double calc(const vector<double>& p) {
    int n = p.size();
    vector<vector<double> > d(n + 1);
    for (int i = 0; i <= n; ++i) d[i].resize(n + 1);
    d[0][0] = 1.0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j <= i; ++j) {
            d[i + 1][j] += d[i][j] * (1 - p[i]);
            d[i + 1][j + 1] += d[i][j] * p[i];
        }
    }
    return d[n][n / 2];
}

double solve(vector<double> p, int k) {
    int n = p.size();
    double ans = 0.0;
    sort(p.begin(), p.end());
    for (int i = 0; i <= k; ++i) {
        int j = k - i;
            vector<double> pp;
            for (int s = 0; s < i; ++s) pp.push_back(p[s]);
            for (int s = n - j; s < n; ++s) pp.push_back(p[s]);
            assert(pp.size() == k);
            ans = max(ans, calc(pp));
    }
    return ans;
}

int main() {
    int tc;
    cin >> tc;
    cout.precision(10);
    cout << fixed;
    for (int t = 1; t <= tc; ++t) {
        cerr << t << endl;
        int n, k;
        cin >> n >> k;
        vector<double> p(n);
        for (int i = 0; i < n; ++i) cin >> p[i];
        cout << "Case #" << t << ": " << solve(p, k) << endl;
    }
    return 0;
}
