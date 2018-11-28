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

const int maxn = 1001;
int x[maxn], y[maxn], z[maxn], vx[maxn], vy[maxn], vz[maxn];
int vis[maxn];

int n, s;

void dfs(int v, int m) {
    if (vis[v]) return;
    vis[v] = 1;
    forn(i, n) {
        if ((x[i] - x[v]) * (x[i] - x[v]) + (y[i] - y[v]) * (y[i] - y[v]) + (z[i] - z[v]) * (z[i] - z[v]) <= m) dfs(i, m);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.precision(10);
    cout << fixed;

    int T;
    cin >> T;
    for1(tc, T) {
        cerr << tc << '\n';
        cin >> n >> s;
        forn(i, n) cin >> x[i] >> y[i] >> z[i] >> vx[i] >> vy[i] >> vz[i];
        int l = -1, r = 1e9;
        while (r - l > 1) {
            int m = (l + r) / 2;
            forn(i, n) vis[i] = 0;
            dfs(0, m);
            (vis[1] ? r : l) = m;
        }
        cout << "Case #" << tc << ": " << sqrt(1.0 * r) << '\n';
    }

#ifdef LOCAL_DEFINE
    cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
#endif
    return 0;
}
