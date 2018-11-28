#include <iostream>
#include <iosfwd>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cassert>
#include <cctype>
#include <climits>
#include <vector>
#include <bitset>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <deque>
#include <string>
#include <list>
#include <iterator>
#include <sstream>
#include <complex>
#include <fstream>
#include <functional>
#include <numeric>
#include <utility>
#include <algorithm>
#include <assert.h>
#include <unordered_map>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef vector < long long > vll;
typedef pair <long long, long long> pll;
typedef pair <int, int> pii;
typedef vector < int > vii;
typedef complex < double > Point;

#define csl ios_base::sync_with_stdio(false); cin.tie(NULL)
#define mp make_pair
#define fst first
#define snd second
#define prev PREV
ll t, n, m, u, v, q, r, ql, qr, k, l, s, w, h, c, z, d, y, x, a;
const int N = 1e5 + 500;
const int K = 1e6 + 500;
const int LN = 20;
const long long mod = 1e9 + 7;
const long long INF = 1LL << 52LL;
const bool JUDGE = false;
double P[N];
double dp[202][202];
inline double solve(vector <double> f) {
    memset(dp, 0, sizeof(dp));
    dp[0][0] = 1;
    for (int i = 1; i <= f.size(); ++i)
        for (int j = 0; j <= f.size() / 2; ++j) {
            dp[i][j] = (dp[i - 1][j] * (1.0 - f[i - 1])) + (dp[i - 1][j - 1] * (f[i - 1]));
        }
    return dp[f.size()][f.size() / 2];
}
int main() {
    csl;
    if (JUDGE) {
        freopen("angry.in", "r", stdin);
        freopen("angry.out", "w", stdout);
    }
    cin >> t;
    for (int ii = 1; ii <= t; ++ii) {
        cout << "Case #" << ii << ": ";
        cin >> n >> k;
        double ans = 0.0;
        for (int i = 0; i < n; ++i)
            cin >> P[i];
        sort(P, P + n);
        double ans1 = 0.0;
        for (int i = 0; i < n; ++i) {
            vector < double > s;
            for (int j = i; j <= i + k - 1; ++j)
                s.push_back(P[j % n]);
            ans1 = max(ans1, solve(s));
        }
        cout << fixed << setprecision(6) << ans1;
        cout << '\n';
    }
    return 0;
}















