#include <iostream>
#include <cstdio>
#include <string.h>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <sstream>
#include <cmath>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forv(i, v) forn(i, v.size())
#define all(v) v.begin(), v.end()
#define pb push_back

double calc(vector<double> p) {
    int n = (int)p.size();
    vector< vector<double> > dp(n + 1, vector<double>(n + 1));
    dp[0][0] = 1.0;
    forn(i, n) {
        forn(j, min(i + 1, n / 2 + 1)) {
            dp[i + 1][j + 1] += dp[i][j] * p[i];
            dp[i + 1][j] += dp[i][j] * (1 - p[i]);
        }
    }
    return dp[n][n / 2];
}

void solveCase(int tc) {
    printf("Case #%d: ", tc);
    cerr << tc << endl;
    int n, k; cin >> n >> k;
    vector<double> p(n);
    forn(i, n) cin >> p[i];
    sort(all(p));
    double ans = 0;
    for (int f = 0; f <= n; f++) {
        for (int l = 0; l + f <= n; l++) {
            if (f + l != k) continue;
            vector<double> q;
            forn(i, f) q.push_back(p[i]);
            forn(i, l) q.push_back(p[n - 1 - i]);
            ans = max(ans, calc(q));
        }
    }
    cout.precision(15);
    cout << fixed << ans << endl;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc; cin >> tc;
    forn(it, tc) solveCase(it + 1);
    return 0;
}
