#include <bits/stdc++.h>
using namespace std;
#define sz(x) ((int) (x).size())
#define forn(i,n) for (int i = 0; i < int(n); ++i)
typedef long long ll;
typedef long long i64;
typedef long double ld;
typedef pair<int, int> pii;
const int inf = int(1e9) + int(1e5);
const ll infl = ll(2e18) + ll(1e10);

const int maxn = 105;
int n, m;

int to[maxn * 4];

int cellId(int x, int y) {
    if (x == -1)
        return y;
    if (y == m)
        return m + x;
    if (x == n)
        return m + n + (m - y - 1);
    if (y == -1)
        return m + n + m + (n - x - 1);
    return -1;
}

const int dx[] = {1, 0, -1, 0};
const int dy[] = {0, -1, 0, 1};

char a[maxn][maxn];
bool go(int x, int y, int dir, int toId) {
    if (cellId(x, y) != -1) {
        return cellId(x, y) == toId;
    }
    int ndir = -1;
    if (a[x][y] == '\\')
        ndir = 3 - dir;
    else
        ndir = dir ^ 1;
    int tx = x + dx[ndir], ty = y + dy[ndir];
    return go(tx, ty, ndir, toId);
}

bool check() {
    forn (i, m) {
        if (!go(0, i, 0, to[cellId(-1, i)]))
            return false;
        if (!go(n - 1, i, 2, to[cellId(n, i)]))
            return false;
    }
    forn (i, n) {
        if (!go(i, m - 1, 1, to[cellId(i, m)]))
            return false;
        if (!go(i, 0, 3, to[cellId(i, -1)]))
            return false;
    }
    return true;
}

bool rec(int id) {
    if (id == n * m) {
        return check();
    }
    int x = id / m, y = id % m;
    a[x][y] = '/';
    if (rec(id + 1))
        return true;
    a[x][y] = '\\';
    if (rec(id + 1))
        return true;
    return false;
}

int test = 1;
void solve() {
    cin >> n >> m;
    forn (i, (n + m)) {
        int a, b;
        cin >> a >> b;
        --a, --b;
        to[a] = b, to[b] = a;
    }
    cout << "Case #" << test++ << ":\n";
    if (rec(0)) {
        forn (i, n) {
            forn (j, m)
                cout << a[i][j];
            cout << '\n';
        }
    } else
        cout << "IMPOSSIBLE\n";
}

int main() {
    #ifdef LOCAL
    assert(freopen("c.in", "r", stdin));
    #else
    #endif
    int tn;
    cin >> tn;
    forn (i, tn) {
        solve();
    }
}
