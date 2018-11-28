#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

const int MAXN = 16;

int n, m;
int board[MAXN][MAXN];
bool row[MAXN];
bool col[MAXN];

void precomp() {
    for (int i = 0; i < MAXN; i++) {
        row[i] = false;
        col[i] = false;
    }

    for (int i = 0; i < n; i++) {
        bool answ = true;
        for (int j = 0; j < m; j++) {
            if (board[i][j] != 1) {
                answ = false;
                break;
            }
        }
        row[i] = answ;
    }

    for (int j = 0; j < m; j++) {
        bool answ = true;
        for (int i = 0; i < n; i++) {
            if (board[i][j] != 1) {
                answ = false;
                break;
            }
        }

        col[j] = answ;
    }
}

bool isPossible(int r, int c) {
    return board[r][c] == 2 || row[r] || col[c];
}

bool solve() {
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> board[i][j];
        }
    }

    precomp();

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (!isPossible(i, j)) {
                return false;
            }
        }
    }

    return true;
}

int main() {
    int tests;
    cin >> tests;

    for (int i = 0; i < tests; i++) {
        cout << "Case #" << i + 1 << ": " << (solve() ? "YES" : "NO") << endl;
    }

    return 0;
}
