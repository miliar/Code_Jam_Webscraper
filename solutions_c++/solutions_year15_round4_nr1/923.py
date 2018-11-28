
#include <algorithm>
#include <iostream>
#include <string>
#define MAXN 100

using namespace std;

int R, C;
string g[MAXN];

bool hl[MAXN][MAXN], hr[MAXN][MAXN], hu[MAXN][MAXN], hd[MAXN][MAXN];

int solve() {
    for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++)
            hl[i][j] = hr[i][j] = hu[i][j] = hd[i][j] = false;

    for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++)
            if (g[i][j] != '.') {
                for (int k = 0; k < C; k++) {
                    if (k == j)
                        continue;
                    if (k < j)
                        hr[i][k] = true;
                    if (k > j)
                        hl[i][k] = true;
                }
                for (int k = 0; k < R; k++) {
                    if (k == i)
                        continue;
                    if (k < i)
                        hd[k][j] = true;
                    if (k > i)
                        hu[k][j] = true;
                }
            }
    for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++)
            if (g[i][j] != '.'
                    && !hl[i][j] && !hr[i][j] && !hu[i][j] && !hd[i][j])
                return -1;

    int cnt = 0;
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (g[i][j] == '<')
                cnt++;
            if (g[i][j] != '.')
                break;
        }
        for (int j = C - 1; j >= 0; j--) {
            if (g[i][j] == '>')
                cnt++;
            if (g[i][j] != '.')
                break;
        }
    }
    for (int j = 0; j < C; j++) {
        for (int i = 0; i < R; i++) {
            if (g[i][j] == '^')
                cnt++;
            if (g[i][j] != '.')
                break;
        }
        for (int i = R - 1; i >= 0; i--) {
            if (g[i][j] == 'v')
                cnt++;
            if (g[i][j] != '.')
                break;
        }
    }
    return cnt;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> R >> C;
        for (int i = 0; i < R; i++)
            cin >> g[i];

        int r = solve();
        cout << "Case #" << t << ": ";
        if (r == -1)
            cout << "IMPOSSIBLE";
        else
            cout << r;
        cout << endl;
    }
}
