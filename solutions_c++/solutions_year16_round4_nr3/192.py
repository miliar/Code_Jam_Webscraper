#include <iostream>
#include <algorithm>

using namespace std;

int r, c;
int lover[1000];
int yard[150][150];

int find(int i, int j, int dir) {
    if (yard[i][j] > 0) {
        return yard[i][j];
        // '/'
    } else if (yard[i][j] == 0) {
        if (dir == 0) return find(i, j - 1, 1);
        if (dir == 1) return find(i + 1, j, 0);
        if (dir == 2) return find(i, j + 1, 3);
        if (dir == 3) return find(i - 1, j, 2);
        // '\'
    } else {
        if (dir == 0) return find(i, j + 1, 3);
        if (dir == 1) return find(i - 1, j, 2);
        if (dir == 2) return find(i, j - 1, 1);
        if (dir == 3) return find(i + 1, j, 0);
    }
    return -1;
}

int main() {
    int T, tc;
    int i, j;

    cin >> T;
    for (tc = 1; tc <= T; tc++) {
        cout << "Case #" << tc << ": " << endl;
        cin >> r >> c;
        for (int i = 1; i <= (r + c); i++) {
            int a, b;
            cin >> a >> b;
            lover[a] = b;
            lover[b] = a;
        }

        for (int i = 1; i <= c; i++) {
            yard[0][i] = i;
            yard[r + 1][i] = r + c + (c - i + 1);
        }
        for (int i = 1; i <= r; i++) {
            yard[i][c + 1] = c + i;
            yard[i][0] = r + 2 * c + (r - i + 1);
        }

        int found;
        found = 0;
        for (int wall = 0; wall < (1 << (r * c)); wall++) {
            int tmp = wall;
            for (i = 1; i <= r; i++) {
                for (j = 1; j <= c; j++) {
                    yard[i][j] = (tmp & 1) - 1;
                    tmp = tmp >> 1;
                }
            }

            for (i = 1; i <= 2 * (r + c); i++) {
                int res;
                if (i <= c) {
                    res = find(1, i, 0);
                } else if (i <= r + c) {
                    res = find(i - c, c, 1);
                } else if (i <= r + 2 * c) {
                    res = find(r, r + 2 * c - i + 1, 2);
                } else {
                    res = find(r * 2 + 2 * c - i + 1, 1, 3);
                }
                if (res != lover[i]) break;
            }
            if (i > 2 * (r + c)) {
                found = 1;
                break;
            }
        }
        if (found) {
            for (i = 1; i <= r; i++) {
                for (j = 1; j <= c; j++) {
                    if (yard[i][j] == 0)
                        cout << '/';
                    else
                        cout << '\\';
                }
                cout << endl;
            }
        } else {
            cout << "IMPOSSIBLE" << endl;
        }
    }
    return 0;
}
