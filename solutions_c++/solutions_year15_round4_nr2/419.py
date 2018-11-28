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
#include <unordered_map>
#include <iomanip>

using namespace std;

#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

#define forit(X,Y) for(typeof((Y).begin()) X = (Y).begin(); X != (Y).end(); ++X)

#define mplus(x, y) ((x) == -1 || (y) == -1) ? -1 : ((x) + (y))
#define mmax(x, y) ((x) == -1 || (y) == -1) ? -1 : max((x), (y))
#define mmin(x, y) ((x) == -1) ? (y) : ((y) == -1) ? (x) : min((x), (y))
#define checkbit(n, k) (((1L << (k)) & (n)) != 0)

#define debug(x) cerr << '>' << #x << ':' << x << endl;

typedef long long int64;

typedef vector <int> vi;
typedef vector < vi > vvi;

double f(int n, double v, double x, vector<double> r, vector<double> c) {
    if (n == 1) {
        if (fabs(x - c[0]) < 1e-5) {
            return v / r[0];
        } else {
            return -1;
        }
    } else {
        double r1 = r[0], r2 = r[1];
        double c1 = c[0], c2 = c[1];
        if (fabs(c1 - c2) < 1E-5) {
            if (fabs(x - c1) < 1E-5) {
                return v / (r1 + r2);
            } else {
                return -1;
            }
        }
        double x1 = v / r1 * (x - c2) / (c1 - c2);
        double x2 = v / r2 * (c1 - x) / (c1 - c2);
        if (x1 >= 0 && x2 >= 0)
            return max(x1, x2);
        else
            return -1;
    }
}


int main() {
    int T;
    cin >> T;
    for (int tt = 1; tt <= T; ++tt) {
        int n;
        double v, x;
        cin >> n >> v >> x;
        vector<double> r(n), c(n);
        for (int i = 0; i < n; ++i)
            cin >> r[i] >> c[i];
        double res = f(n, v, x, r, c);
        if (res >= 0)
            printf("Case #%d: %.9f\n", tt, res);
            // cout << "Case #" << tt << ": " << res << endl;
        else
            cout << "Case #" << tt << ": " << "IMPOSSIBLE" << endl;
    }
}
