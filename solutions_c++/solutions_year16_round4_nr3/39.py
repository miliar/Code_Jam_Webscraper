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

int dx[4] = {1, 1, -1, -1};
int dy[4] = {1, -1, -1, 1};

const int maxn = 201;
int f[maxn][maxn];

int n, m;

bool can_pass(int x, int y, int d) {
    int xx = x + dx[d], yy = y + dy[d];
    if (min(xx, yy) < 0 || min(2 * n - xx, 2 * m - yy) < 0) return false;
    int nx = min(x, xx) / 2, ny = min(y, yy) / 2;
    if (d & 1) {
        if (f[nx][ny] == 0) return false;
        f[nx][ny] = 1;
        return true;
    } else {
        if (f[nx][ny] == 1) return false;
        f[nx][ny] = 0;
        return true;
    }
}

void getp(int i, int n, int m, int &x, int &y, int &d) {
    if (i < m) {
        x = 0;
        y = 2 * i + 1;
        d = 0;
        return;
    }
    i -= m;
    if (i < n) {
        x = 2 * i + 1;
        y = 2 * m;
        d = 1;
        return;
    }
    i -= n;
    if (i < m) {
        x = 2 * n;
        y = 2 * m - 1 - 2 * i;
        d = 2;
        return;
    }
    i -= m;
    x = 2 * n - 1 - 2 * i;
    y = 0;
    d = 3;
}

bool dfs(int x, int y, int d, int tx, int ty) {
    if (x == tx && y == ty) return true;
    forn(i, 3) {
        if (can_pass(x, y, d)) return dfs(x + dx[d], y + dy[d], (d + 3) % 4, tx, ty);
        else ++d, d %= 4;
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.precision(10);
    cout << fixed;

//    freopen("sample.in", "rt", stdin);

    int ttt;
    cin >> ttt;
    for1(tc, ttt) {
        cin >> n >> m;
        forn(i, n) forn(j, m) f[i][j] = -1;
        vi a(2 * (n + m));
        forn(i, n + m) {
            int x, y;
            cin >> x >> y;
            --x; --y;
            a[x] = y;
            a[y] = x;
        }
        vi used(a.size());
        int matched = 0;
        bool ok = true;
        while (ok && matched < n + m) {
            bool ch = false;
            forn(i, 2 * (n + m)) {
                if (used[i]) continue;
                int j = (i + 1) % a.size();
                while (used[j]) ++j, j %= a.size();
                if (j == a[i]) {
                    used[j] = used[i] = 1;
                    ++matched;
                    ch = 1;
                    int x, y, d, tx, ty, td;
                    getp(i, n, m, x, y, d);
                    getp(j, n, m, tx, ty, td);
                    ok &= dfs(x, y, d, tx, ty);
                }
            }
            if (!ch) ok = false;
        }
        cout << "Case #" << tc << ":\n";
        if (!ok) cout << "IMPOSSIBLE\n";
        else {
            forn(i, n) {
                forn(j, m) {
                    if (f[i][j] < 0) f[i][j] = 0;
                    cout << "\\/"[f[i][j]];
                }
                cout << '\n';
            }
        }
    }

#ifdef LOCAL_DEFINE
    cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
#endif
    return 0;
}
