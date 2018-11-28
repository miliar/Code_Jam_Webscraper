#include <iostream>
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
typedef vector<vi> vvi;
typedef long long i64;
typedef vector<i64> vi64;
typedef vector<vi64> vvi64;

template<class T> bool uin(T &a, T b) { return a > b ? (a = b, true) : false; }
template<class T> bool uax(T &a, T b) { return a < b ? (a = b, true) : false; }

const int MAXN = 1100000;
const int MAXT = 2100000;
int sal[MAXN];
vi e[MAXN];
int ans[MAXT];

int N, D;

void dfs(int v, int l, int r) {
    uax(l, sal[v] - D);
    uin(r, sal[v] + 1);
//    cerr << v << ' ' << l << ' ' << r << '\n';
    if (l >= r) return;
    ++ans[l];
    --ans[r];
    for (int u: e[v]) dfs(u, l, r);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.precision(10);
    cout << fixed;

    int T;
    cin >> T;
    for1(tn, T) {
        cin >> N >> D;
        forn(i, N) e[i].clear();
        i64 s0, as, cs, rs, m0, am, cm, rm;
        cin >> s0 >> as >> cs >> rs >> m0 >> am >> cm >> rm;
        sal[0] = s0;
        forn(i, rs + 10) ans[i] = 0;
        for1(i, N - 1) {
            s0 = (s0 * as + cs) % rs;
            m0 = (m0 * am + cm) % rm;
//            cerr << i << ' ' << s0 << ' ' << m0 % i << '\n';
            sal[i] = s0;
            e[m0 % i].pb(i);
        }
        dfs(0, 0, 1e9);
        int res = -1;
        forn(i, rs + 10) {
            uax(res, ans[i]);
            ans[i + 1] += ans[i];
        }
        cout << "Case #" << tn << ": " << res << '\n';
    }

#ifdef LOCAL_DEFINE
    cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
#endif
    return 0;
}
