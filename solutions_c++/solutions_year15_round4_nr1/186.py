#include <iostream>

using namespace std;

// R, D, L, U
int dr[] = {0, 1, 0, -1};
int dc[] = {1, 0, -1, 0};

const int MAXN = 100;

int m[MAXN][MAXN];
int R, C;

bool is_deadly(int r, int c) {
    int d = m[r][c];
    bool first = true;
    while (r >= 0 && r < R && c >= 0 && c < C) {
        if (!first && m[r][c] != -1) {
            return false;
        }
        first = false;
        r += dr[d];
        c += dc[d];
    }
    return true;
}

bool has_neighbors(int r, int c) {
    int d = m[r][c];
    bool has = false;

    for (int i = 0; i < 4; i++) {
        m[r][c] = i;
        if (!is_deadly(r, c)) {
            has = true;
        }
    }

    m[r][c] = d;

    return has;
}

int main() {
    int T;
    cin >> T;

    for (int tc = 1; tc <= T; tc++) {
        cin >> R >> C;

        for (int i = 0; i < R; i++)
            for (int j = 0; j < C; j++) {
                char dir;
                cin >> dir;
                switch (dir) {
                    case '>': m[i][j] = 0; break;
                    case 'v': m[i][j] = 1; break;
                    case '<': m[i][j] = 2; break;
                    case '^': m[i][j] = 3; break;
                    case '.': m[i][j] = -1; break;
                    default: cerr << "error!\n";
                }
            }

        int ans = 0;
        bool possible = true;

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (m[i][j] != -1 && is_deadly(i, j)) {
                    if (has_neighbors(i, j)) {
                        ans++;
                    } else {
                        possible = false;
                    }
                }
            }
        }

        cout << "Case #" << tc << ": ";

        if (possible) {
            cout << ans << '\n';
        } else {
            cout << "IMPOSSIBLE\n";
        }
    }

    return 0;
}
