#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <bitset>
#include <set>
#include <sstream>
#include <stdlib.h>
#include <map>
#include <queue>
#include <stack>
#include <assert.h>
#include <iomanip>

using namespace std;

#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

#define mplus(x, y) ((x) == -1 || (y) == -1) ? -1 : ((x) + (y))
#define mmax(x, y) ((x) == -1 || (y) == -1) ? -1 : max((x), (y))
#define mmin(x, y) ((x) == -1) ? (y) : ((y) == -1) ? (x) : min((x), (y))

#define checkbit(n, k) (((1L << (k)) & (n)) != 0)

#define forit(X,Y) for(typeof((Y).begin()) X = (Y).begin(); X != (Y).end(); ++X)

#define debug(x) cerr << "> " << #x << ": " << (x) << endl;

typedef long long int64;

typedef vector <int> vi;
typedef vector < vi > vvi;

double foo(int n, int k, vector<double>& p) {
    double res = 0;
    sort(p.begin(), p.end());
    for (int left = 0; left <= k; ++left) {
        int right = n - k + left;
        vector<double> dp(k + 1), dp1(k + 1);
        dp[0] = 1;
        for (int i = 0; i < n; ++i) {
            if (i >= left && i < right) continue;
            dp1.assign(k + 1, 0);
            for (int j = 0; j <= k; ++j) {
                if (j > 0)
                    dp1[j] += p[i] * dp[j - 1];
                dp1[j] += (1 - p[i]) * dp[j];
            }
            dp.swap(dp1);
        }
        res = max(res, dp[k / 2]);
    }
    return res;
}

// double foo_slow(int n, int k, vector<double>& p) {
//     double res = 0;
//     for (int m = 1; m < (1 << n); ++m) {
//         int c = 0;
//         for (int i = 0; i < n; ++i) {
//             if (checkbit(m, i)) ++c;
//         }
//         if (c != k) continue;

//         vector<double> distr(k + 1);
//         distr[0] = 1;
//         for (int i = 0; i < n; ++i) {
//             if (!checkbit(m, i)) continue;
//             vector<double> distr1(k + 1);
//             for (int j = 0; j < k + 1; ++j) {
//                 distr1[j] = (1 - p[i]) * distr[j];
//                 if (j > 0) distr1[j] += p[i] * distr[j - 1];
//             }
//             distr.swap(distr1);
//         }
//         res = max(res, distr[k / 2]);
//     }
//     return res;
// }

int main() {
     // freopen("input.txt", "rt", stdin);
    // freopen("output.txt", "wt", stdout);

	int testCount;
    cin >> testCount;

    for (int testNumber = 1; testNumber <= testCount; ++testNumber) {
        int n, k;
        cin >> n >> k;
        vector<double> p(n);
        for (int i = 0; i < n; ++i)
            cin >> p[i];
        auto res = foo(n, k, p);
        printf("Case #%d: %.7f\n", testNumber, res);
        // cout << "Case #" << testNumber << ": " << setprecision(6) << res << endl;
    }

    return 0;
}
