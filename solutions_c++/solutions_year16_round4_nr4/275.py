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
const int MAXN = 4;

char t[MAXN][MAXN];
char st[MAXN][MAXN];

int n;
int p[MAXN];
bool occ[MAXN];

bool rec(int i) {
    if (i == n) {
        return true;
    }
    bool flag = false;
    forn(j, n) {
        if (!occ[j] && st[p[i]][j]) {
            flag = true;
            occ[j] = true;
            if (!rec(i + 1)) {
                return false;
            }
            occ[j] = false;
        }
    }
    /*
    if (!flag) {
        cerr <<"FAIL " <<  i << '\n';
        forn(i, n) {
            cerr <<p[i] << ' ';
        }
        cerr << '\n';
        forn(i, n) {
            cerr << occ[i];
        }
        cerr << '\n';
    }*/
    return flag;
}
bool check() {
    forn(i, n)
        p[i] = i;
    do {
        clr(occ);
        if (!rec(0)) {
            return false;
        }
    } while (next_permutation(p, p + n));
    return true;
}
void solve() {
    cin >> n;
    int c1 = 0;
    forn(i, n) {
        forn(j, n) {
            cin >> t[i][j];
            t[i][j] -= '0';
            st[i][j] = t[i][j];
            if (t[i][j] == 1) {
                c1++;
            }
        }
    }
    int m = n * n;
    int ans = m;
    forn(msk, (1 << m)) {
        bool flag = true;
        forn(i, m) {
            int x = i / n, y = i % n;
            st[x][y] = (msk & (1 << i)) != 0;
            if (t[x][y] == 1 && st[x][y] == 0) {
                flag = false;
                break;
            }
        }
        if (!flag)
            continue;
        if (check()) {
            ans = min(ans, __builtin_popcount(msk) - c1);
        }
    }
    cout << ans << '\n';

}
int main() {
#ifdef LOCAL
    freopen("d.in", "r", stdin);
    freopen("d.out", "w", stdout);
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

