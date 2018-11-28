#include <cstdio>

char board[110][110];
int n, m;

bool GoOut(int x, int y) {
    const int mov[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    int d = -1;
    if (board[x][y] == '^') d = 0;
    if (board[x][y] == '>') d = 1;
    if (board[x][y] == 'v') d = 2;
    if (board[x][y] == '<') d = 3;
    int k = d;
    int nx = x + mov[k][0];
    int ny = y + mov[k][1];
    while (true) {
        if (nx < 0 || nx >= n || ny < 0 || ny >= m) return true;
        if (board[nx][ny] != '.') break;
        nx += mov[k][0];
        ny += mov[k][1];
    }
    return false;
}

bool CanChange(int x, int y) {
    const int mov[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    int d = -1;
    if (board[x][y] == '^') d = 0;
    if (board[x][y] == '>') d = 1;
    if (board[x][y] == 'v') d = 2;
    if (board[x][y] == '<') d = 3;

    for (int k = 0; k < 4; k++) {
        if (k == d) continue;
        int nx = x + mov[k][0];
        int ny = y + mov[k][1];
        while (true) {
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
                break;
            }
            if (board[nx][ny] != '.') return true;
            nx += mov[k][0];
            ny += mov[k][1];
        }
    }
    return false;
}


int Solve() {
    int ans = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (board[i][j] == '.') continue;
            if (GoOut(i, j)) {
                if (CanChange(i, j)) ans++;
                else return -1;
            }
        }
    }
    return ans;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; i++)
            scanf("%s", board[i]);
        int ans = Solve();
        if(ans == -1) printf("Case #%d: IMPOSSIBLE\n", cas);
        else printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
