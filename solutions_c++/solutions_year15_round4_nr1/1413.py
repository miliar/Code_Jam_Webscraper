#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int kMaxN = 100 + 10;
const int dx[] = {0, 1, 0, -1};
const int dy[] = {1, 0, -1, 0};

char board[kMaxN][kMaxN];
int T, R, C;

bool check(int i, int j, int dir) {
    int r = i, c = j;
    while (r >= 0 && r < R && c >= 0 && c < C) {
        if (!(r == i && c == j)) {
            if (board[r][c] != '.') {
                return true;
            }
        }
        r += dx[dir];
        c += dy[dir];
    }
    return false;
}

int main() {
    scanf("%d", &T);
    for (int cas = 0; cas < T; ++cas) {
        scanf("%d%d", &R, &C);
        for (int i = 0; i < R; ++i) {
            scanf("%s", board[i]);
        }
        int ans = 0;
        bool failed = false;
        for (int i = 0; i < R && !failed; ++i) {
            for (int j = 0; j < C && !failed; ++j) {
                if (board[i][j] == '.') {
                    continue;
                }
                int dir = 0;
                if (board[i][j] == '>') {
                    dir = 0;
                } else if (board[i][j] == 'v') {
                    dir = 1;
                } else if (board[i][j] == '<') {
                    dir = 2;
                } else {
                    dir = 3;
                }
                if (check(i, j, dir)) {
                    continue;
                }
                if (check(i, j, 0) || check(i, j, 1) || check(i, j, 2) || check(i, j, 3)) {
                    ++ans;
                    continue;
                } else {
                    failed = true;
                    break;
                }
            }
        }
        
        if (!failed) {
            printf("Case #%d: %d\n", cas + 1, ans);
        } else {
            printf("Case #%d: IMPOSSIBLE\n", cas + 1);
        }
    }
    return 0;
}

