#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <ctime>
#include <cmath>
#include <string>
#include <iomanip>
#include <vector>
#include <set>
#include <map>
#include <cassert>
#include <queue>
#include <bitset>

using namespace std;

#define FOR(a, b) for (int a = 0; a < (b); ++a)
#define clr(a) memset(a, 0, sizeof(a))
#define pb push_back
#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)
#ifdef LOCAL
#define debug(a) cerr << #a << ": " << a << '\n';
#else
#define debug(a)
#endif

typedef long long ll;
typedef long double ld;

const int INF = 1e9;
const ld EPS = 1e-8;
const ld PI = acos(-1.0L);
const int MAXN = 210;

ld p[MAXN];
ld dp[MAXN][MAXN];

ld calc(vector<ld> p) {
    int n = p.size();
    clr(dp);
    dp[0][0] = 1;
    for (int i = 1; i <= n; ++i) {
        dp[i][0] = dp[i - 1][0] * p[i - 1];
    }
    for(int i = 1; i <= n; ++i) {
        for (int j = 1; j <= i; ++j) {
            dp[i][j] = p[i - 1] * dp[i - 1][j] + (1.0L - p[i - 1]) * dp[i - 1][j - 1];
        }
    }
    return dp[n][n / 2];
}

int n, k;
ld calc2(bitset<MAXN> msk) {
    vector<ld> pr;
    forn(i, n) {
        if (msk[i]) {
            pr.pb(p[i]);
        }
    }
    return calc(pr);
}

void solve() {
    cin >> n >> k;
    forn(i, n)
        cin >> p[i];
    sort(p, p + n);

    bitset<MAXN> msk;
    forn(i, k)
        msk[i] = 1;
    int p = k;
    ld cur = calc2(msk);
    while (p >= 0) {
        if (msk[p]) {
            if (p < n - 1 && (!msk[p + 1])) {
                bitset<MAXN> nmsk = msk;
                nmsk[p] = 0;
                nmsk[p + 1] = 1;
                ld na = calc2(nmsk);
                if (na > cur - EPS) {
                    cur = na;
                    msk = nmsk;
                    p += 2;
                }
            }
        }
        p--;
    }
    cout << fixed << setprecision(20) << cur << '\n';
}

int main() {
#ifdef LOCAL
    //freopen("", "r", stdin);
    //freopen("", "w", stdout);
    //freopen("", "w", stderr);
#endif
    int T;
    cin >> T;
    forn(test, T) {
        cout << "Case #" << test + 1 << ": ";
        solve();
    }
    
    return 0;
}

