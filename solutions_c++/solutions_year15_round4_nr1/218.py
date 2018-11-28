#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

string board[100];
int R, C;

bool pointing_outside(int i, int j) {
    int di[256], dj[256];
    di['^'] = -1; dj['^'] = 0;
    di['>'] = 0; dj['>'] = 1;
    di['v'] = 1; dj['v'] = 0;
    di['<'] = 0; dj['<'] = -1;

    int Di = di[board[i][j]], Dj = dj[board[i][j]];
    i += Di; j += Dj;

    while (i >= 0 && i < R && j >= 0 && j < C) {
        if (board[i][j] != '.')
            return false;
        i += Di; j += Dj;
    }

    return true;
}

int main() {
    int t;
    cin >> t;

    for (int z = 1; z <= t; z++) {
        cin >> R >> C;

        for (int i = 0; i < R; i++)
            cin >> board[i];

        int by_row[R], by_col[C];
        memset(by_row, 0, sizeof by_row);
        memset(by_col, 0, sizeof by_col);

        for (int i = 0; i < R; i++)
            for (int j = 0; j < C; j++)
                if (board[i][j] != '.') {
                    by_row[i]++;
                    by_col[j]++;
                }

        int ans = 0;
        for (int i = 0; i < R; i++)
            for (int j = 0; j < C; j++) {
                if (board[i][j] == '.')
                    continue;

                if (by_row[i] + by_col[j] == 2)
                    ans = -0x3f3f3f3f;
                else if (pointing_outside(i, j))
                    ans++;
            }

        if (ans < 0)
            cout << "Case #" << z << ": IMPOSSIBLE" << endl;
        else
            cout << "Case #" << z << ": " << ans << endl;

    }
}
