#include <iostream>
#include <cstdio>

using namespace std;

int R, C;
string board[105];
int dr[] = {-1, 1, 0, 0};
int dc[] = {0, 0, -1, 1};

bool out_bound(int r, int c) {
    return r < 0 || r >= R || c < 0 || c >= C;
}

bool is_arrow(int r, int c) {
    return board[r][c] != '.';
}

int get_dir(char c) {
    if (c == '^')
        return 0;
    if (c == 'v')
        return 1;
    if (c == '<')
        return 2;
    if (c == '>')
        return 3;
    return -1;
}

bool has_outdegree(int r, int c, int dir) {
    int rr = r, cc = c;
    while (true) {
        rr += dr[dir], cc += dc[dir];
        if (out_bound(rr, cc))
            break;
        if (is_arrow(rr, cc)) {
            return true;
        }
    }
    return false;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    cin>>T;
    for (int cc = 1; cc <= T; cc++) {
        cin>>R>>C;
        for (int i = 0; i < R; i++)
            cin>>board[i];

        bool impossible = false;
        int res = 0;
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (board[i][j] != '.') {
                    bool ok = false;
                    for (int t = 0; t < 4; t++) {
                        if (has_outdegree(i, j, t)) {
                            ok = true;
                            break;
                        }
                    }
                    if (!ok) {
                        impossible = true;
                    }

                    int dir = get_dir(board[i][j]);
                    if (!has_outdegree(i, j, dir)) {
                        res++;
                    }
                }
            }
        }
        if (impossible) {
            printf("Case #%d: IMPOSSIBLE\n", cc);
        } else {
            printf("Case #%d: %d\n", cc, res);
        }
    }
    return 0;
}
