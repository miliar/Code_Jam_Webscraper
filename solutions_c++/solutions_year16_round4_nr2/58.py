#include <iostream>
#include <tuple>
#include <sstream>
#include <vector>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <numeric>

#define mp make_pair
#define mt make_tuple
#define fi first
#define se second
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)

using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vpi;
typedef vector<vi> vvi;
typedef long long i64;
typedef vector<i64> vi64;
typedef vector<vi64> vvi64;
typedef pair<i64, i64> pi64;
typedef double ld;

template<class T> bool uin(T &a, T b) { return a > b ? (a = b, true) : false; }
template<class T> bool uax(T &a, T b) { return a < b ? (a = b, true) : false; }

const int maxn = 202;
double dp1[maxn][maxn], dp2[maxn][maxn];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.precision(10);
    cout << fixed;

    int ttt;
    cin >> ttt;
    for1(tc, ttt) {
        int n, k;
        cin >> n >> k;
        vector<ld> p(n);
        forn(i, n) cin >> p[i];
        sort(all(p));
        forn(i, n + 1) forn(j, n + 1) dp1[i][j] = dp2[i][j] = 0;
        dp1[0][0] = 1;
        forn(i, n) {
            forn(j, i + 1) {
                dp1[i + 1][j + 1] += p[i] * dp1[i][j];
                dp1[i + 1][j] += (1.0 - p[i]) * dp1[i][j];
            }
        }
        reverse(all(p));
        dp2[0][0] = 1;
        forn(i, n) {
            forn(j, i + 1) {
                dp2[i + 1][j + 1] += p[i] * dp2[i][j];
                dp2[i + 1][j] += (1.0 - p[i]) * dp2[i][j];
            }
        }
        ld ans = 0.0;
        forn(i, k + 1) {
            ld res = 0.0;
            forn(j, k / 2 + 1) res += dp1[i][j] * dp2[k - i][k / 2 - j];
            uax(ans, res);
        }
        cout << "Case #" << tc << ": " << ans << '\n';
    }

#ifdef LOCAL_DEFINE
    cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
#endif
    return 0;
}
