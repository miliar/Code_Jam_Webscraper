#include <iostream>
#include <string>
using namespace std;

int main() {
    int T, tc, i, j, cx, co, flag, e;
    string b[5];
    cin >> T;
    for (tc = 0; tc < T; ++tc) {
        flag = 0;
        for (i = 0; i < 4; ++i) {
            cin >> b[i];
        }

        // Rows
        for (i = 0; i < 4; ++i) {
            cx = co = 0;
            for (j = 0; j < 4; ++j) {
                if (b[i][j] == 'X') {
                    ++cx;
                }
                else if (b[i][j] == 'O') {
                    ++co;
                }
                else if (b[i][j] == 'T') {
                    ++cx;
                    ++co;
                }
            }
            if (cx == 4) {
                flag = 1;
                cout << "Case #" << tc + 1 << ": X won\n";
                break;
            }
            else if (co == 4) {
                flag = 1;
                cout << "Case #" << tc + 1 << ": O won\n";
                break;
            }
        }
        if (flag) {
            continue;
        }

        // Columns
        for (i = 0; i < 4; ++i) {
            cx = co = 0;
            for (j = 0; j < 4; ++j) {
                if (b[j][i] == 'X') {
                    ++cx;
                }
                else if (b[j][i] == 'O') {
                    ++co;
                }
                else if (b[j][i] == 'T') {
                    ++cx;
                    ++co;
                }
            }
            if (cx == 4) {
                flag = 1;
                cout << "Case #" << tc + 1 << ": X won\n";
                break;
            }
            else if (co == 4) {
                flag = 1;
                cout << "Case #" << tc + 1 << ": O won\n";
                break;
            }
        }
        if (flag) {
            continue;
        }

        // Main Diagonal
        cx = co = 0;
        for (i = 0; i < 4; ++i) {
            if (b[i][i] == 'X') {
                ++cx;
            }
            else if (b[i][i] == 'O') {
                ++co;
            }
            else if (b[i][i] == 'T') {
                ++cx;
                ++co;
            }
        }
        if (cx == 4) {
            cout << "Case #" << tc + 1 << ": X won\n";
            continue;
        }
        else if (co == 4) {
            cout << "Case #" << tc + 1 << ": O won\n";
            continue;
        }

        // Second Diagonal
        cx = co = 0;
        for (i = 0; i < 4; ++i) {
            if (b[i][3 - i] == 'X') {
                ++cx;
            }
            else if (b[i][3 - i] == 'O') {
                ++co;
            }
            else if (b[i][3 - i] == 'T') {
                ++cx;
                ++co;
            }
        }
        if (cx == 4) {
            cout << "Case #" << tc + 1 << ": X won\n";
            continue;
        }
        else if (co == 4) {
            cout << "Case #" << tc + 1 << ": O won\n";
            continue;
        }

        e = 0;
        for (i = 0; i < 4; ++i) {
            for (j = 0; j < 4; ++j) {
                if (b[i][j] == '.') {
                    ++e;
                }
            }
        }
        cout << "Case #" << tc + 1 << ": ";
        if (e != 0) {
            cout << "Game has not completed\n";
        }
        else {
            cout << "Draw\n";
        }
    }
    return 0;
}
