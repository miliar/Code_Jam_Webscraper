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
const int MAXN = 13;

string dp[MAXN][3];
vector<vector<int>> ps = {{0, 1}, {1, 2}, {0, 2}};

bool check(string ss, int r, int p, int s) {
    forn(i, ss.length()) {
        if (ss[i] == 'R')
            r--;
        else if (ss[i] == 'P')
            p--;
        else
            s--;
    }
    return r == 0 && p == 0 && s == 0;
}
void solve() {
    int n, r, p,s;
    cin >> n >> r >> p >> s;
    assert(r + p + s == (1 << n));
    forn(i, 3) {
        if (check(dp[n][i], r, p, s)) {
            cout << dp[n][i] << '\n';
            return;
        }
    }
    cout << "IMPOSSIBLE\n";
}

int main() {
#ifdef LOCAL
    //freopen("", "r", stdin);
    //freopen("", "w", stdout);
    //freopen("", "w", stderr);
#endif
    dp[0][0] = "P";
    dp[0][1] = "R";
    dp[0][2] = "S";
    forn(i, MAXN - 1) {
        forn(j, 3) {
            string s = dp[i][ps[j][0]];
            string t = dp[i][ps[j][1]];
            string a1 = s + t;
            string a2 = t + s;
            dp[i + 1][j] = min(a1, a2);
        }
    }


    int T;
    cin >> T;
    forn(test, T) {
        cout << "Case #" << test + 1 << ": ";
        solve();
    }
    
    return 0;
}

