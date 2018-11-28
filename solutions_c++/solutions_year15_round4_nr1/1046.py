#include <bits/stdc++.h>

using namespace std;

const int MAXN = 100 + 10;
const int INF = (int)(1e9);
const int MOD = (int)(1e9) + 7;

int row[] = {-1, 0, 1, 0};
int col[] = {0, 1, 0, -1};

char a[MAXN][MAXN];
int m, n;

int convert(char c) {
    if (c == '^') return 0;
    if (c == '>') return 1;
    if (c == 'v') return 2;
    if (c == '<') return 3;
}

bool check(int u, int v, int d) {
    while (true) {
        u += row[d]; v += col[d];
        if ((u >= 1) && (u <= m) && (v >= 1) && (v <= n)) {
            if (a[u][v] != '.') return true;
        }
        else return false;
    }
}

void solve() {
    cin >> m >> n;
    for(int i = 1; i <= m; i++) {
        for(int j = 1; j <= n; j++) cin >> a[i][j];
    }

    int res = 0;
    for(int i = 1; i <= m; i++) {
        for(int j = 1; j <= n; j++) {
            if (a[i][j] != '.') {
                int d = convert(a[i][j]);
                if (!check(i, j, d)) {
                    bool ok = false;
                    for(int dir = 0; dir < 4; dir++) {
                        if (dir != d) {
                            if (check(i, j, dir)) {
                                ok = true;
                                break;
                            }
                        }
                    }
                    if (!ok) {
                        cout << "IMPOSSIBLE\n";
                        return;
                    }
                    res++;
                }
            }
        }
    }
    cout << res << endl;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("vuong.out", "w", stdout);

    int test;
    cin >> test;
    for(int tc = 1; tc <= test; tc++) {
        printf("Case #%d: ", tc);
        solve();
    }
}
