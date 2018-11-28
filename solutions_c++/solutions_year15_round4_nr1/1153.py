#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

char a[123][123];

void solve() {
    int n, m;
    cin >> n >> m;
    for (int i = 1; i <= n; i++) {
        string s;
        cin >> s;
        for (int j = 1; j <= m; j++) {
            a[i][j] = s[j - 1];
        }
    }
    int dx[4] = {1, -1, 0,  0};
    int dy[4] = {0,  0, 1, -1};
    int ans = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (a[i][j] == '.') {
                continue;
            }
            int vx = 0, vy = 0;
            if (a[i][j] == '^') {
                vx = -1;
            } else if (a[i][j] == 'v') {
                vx = 1;
            } else if (a[i][j] == '>') {
                vy = 1;
            } else {
                vy = -1;
            }
            int x = i + vx, y = j + vy;
            bool ok = false;
            while (x > 0 && x <= n && y > 0 && y <= m) {
                if (a[x][y] != '.') {
                    ok = true;
                    break;
                }
                x += vx;
                y += vy;
            }
            if (!ok) {
                ans++;
                bool ok = false;
                for (int u = 0; u < 4; u++) {
                    vx = dx[u];
                    vy = dy[u];
                    x = i + vx;
                    y = j + vy;
                    ok = false;
                    while (x > 0 && x <= n && y > 0 && y <= m) {
                        if (a[x][y] != '.') {
                            ok = true;
                            break;
                        }
                        x += vx;
                        y += vy;
                    }
                    if (ok) {
                        break;
                    }
                }
                if (!ok) {
                    printf("IMPOSSIBLE\n");
                    return;
                }
            }
        }
    }
    printf("%d\n", ans);
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for (int test = 1; test <= tc; test++) {
        printf("Case #%d: ", test);
        cerr << test << endl;
        solve();
    }
    return 0;
}