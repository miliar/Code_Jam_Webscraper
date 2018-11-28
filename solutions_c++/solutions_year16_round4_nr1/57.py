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

int win(int x, int y) {
    if ((x + 1) % 3 != y) swap(x, y);
    return x;
}

pii better(pii p) {
    if (p.fi > p.se) swap(p.fi, p.se);
    return p;
}

vi solve(int n, int p, int r, int s, vi ord) {
    if (n == 0) {
        vi ans;
        if (p) ans.pb(0);
        if (r) ans.pb(1);
        if (s) ans.pb(2);
        return ans;
    }
    int x = p + r - s, y = r + s - p, z = p + s - r;
    if (min(x, min(y, z)) < 0) return vi();
    if (x % 2 || y % 2 || z % 2) return vi();
    x /= 2;
    y /= 2;
    z /= 2;
    vector< pair<pii, int> > tord;
    tord.pb(mp(better(mp(ord[0], ord[1])), 0));
    tord.pb(mp(better(mp(ord[1], ord[2])), 1));
    tord.pb(mp(better(mp(ord[2], ord[0])), 2));
    sort(all(tord));
    vi nord(3);
    forn(i, 3) nord[tord[i].se] = i;
    vi v = solve(n - 1, x, y, z, nord);
    if (v.empty()) return vi();
    vi ans;
    for (int x: v) {
        int y = x, z = (x + 1) % 3;
        if (ord[y] > ord[z]) swap(y, z);
        ans.pb(y);
        ans.pb(z);
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.precision(10);
    cout << fixed;

    int t;
    cin >> t;
    for1(tc, t) {
        int n, r, p, s;
        cin >> n >> r >> p >> s;
        vi ord;
        forn(i, 3) ord.pb(i);
        vi v = solve(n, p, r, s, ord);
        cout << "Case #" << tc << ": ";
        if (v.empty()) cout << "IMPOSSIBLE";
        else {
            for (int x: v) cout << "PRS"[x];
        }
        cout << '\n';
    }

#ifdef LOCAL_DEFINE
    cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
#endif
    return 0;
}
