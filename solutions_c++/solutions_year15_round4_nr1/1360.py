#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair <int,int> pii;
typedef vector <int> vi;

#define rep(i, n) for(int i = 0; i < (n); ++i)

#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define all(c) c.begin(), c.end()
#define mset(a, v) memset(a, v, sizeof(a))
#define sz(a) ((int)a.size())

#define gi(x) scanf("%d", &x)
#define pis(x) printf("%d ", x)
#define pin(x) printf("%d\n", x)
#define pnl printf("\n")
#define dbn cerr << "\n"
#define dbg(x) cerr << #x << " : " << (x) << " "
#define dbs(x) cerr << (x) << " "

string grid[111];

int n, m;

inline bool isInside(int x, int y) {
    return x >= 0 and x < n and y >= 0 and y < m;
}

inline bool checkCell(int x, int y, int dx, int dy) {
    x += dx;
    y += dy;
    while (isInside(x, y)) {
        if (grid[x][y] != '.') return true;
        x += dx;
        y += dy;
    }
    return false;
}

inline void solve() {

    cin >> n >> m;

    rep (i, n) cin >> grid[i];

    bool impossible = false;
    int ans = 0;

    rep (i, n) {
        rep (j, m) if (grid[i][j] != '.') {
            bool found = false;
            if (grid[i][j] == '^') {
                if (!checkCell(i, j, -1, 0)) {
                    if (checkCell(i, j, +1, 0) or checkCell(i, j, 0, -1) or checkCell(i, j, 0, +1)) {
                        found = true;
                    }
                } else {
                    continue;
                }
            } else if (grid[i][j] == '>') {
                if (!checkCell(i, j, 0, +1)) {
                    if (checkCell(i, j, +1, 0) or checkCell(i, j, 0, -1) or checkCell(i, j, -1, 0)) {
                        found = true;
                    }
                } else {
                    continue;
                }
            } else if (grid[i][j] == 'v') {
                if (!checkCell(i, j, +1, 0)) {
                    if (checkCell(i, j, -1, 0) or checkCell(i, j, 0, -1) or checkCell(i, j, 0, +1)) {
                        found = true;
                    }
                } else {
                    continue;
                }
            } else if (grid[i][j] == '<') {
                if (!checkCell(i, j, 0, -1)) {
                    if (checkCell(i, j, +1, 0) or checkCell(i, j, 0, +1) or checkCell(i, j, -1, 0)) {
                        found = true;
                    }
                } else {
                    continue;
                }
            }

            if (found) {
                ++ans;
            } else {
                impossible = true;
                break;
            }
        }
    }

    if (impossible) {
        cout << "IMPOSSIBLE\n";
        cerr << "IMPOSSIBLE\n";
    } else {
        cout << ans << "\n";
        cerr << ans << "\n";
    }
}

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int T;
    cin >> T;

    for (int tc = 1; tc <= T; ++tc) {
        cout << "Case #" << tc << ": ";
        fprintf(stderr, "Case #%d: ", tc);
        solve();
    }
    return 0;
}