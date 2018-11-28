#include <iostream>
#include <vector>

using namespace std;

#define MAXN 50

int mines;
int grid[MAXN][MAXN];
int R, C, M;

void print() {
    bool c = false;
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (grid[i][j] == -1) {
                cout << "*";
            }
            else if (grid[i][j] == 1) {
                cout << ".";
            }
            else {
                if (!c) {
                    cout << "c";
                    c = true;
                }
                else {
                    cout << ".";
                }
            }
        }
        cout << "\n";
    }
}

bool DFS(int r, int c) {
    //cout << r << " " << c << endl;;
    //print();
    //cout << endl;
    if (mines == M)
        return true;

    if (mines < M)
        return false;

    // Sweep and save
    vector<int> state;
    for (int ro = -1; ro <= 1; ro++) {
        for (int co = -1; co <= 1; co++) {
            int i = r + ro, j = c + co;

            if (0 <= i && i < R && 0 <= j && j < C) {
                state.push_back(grid[i][j]);

                if (grid[i][j] == -1) {
                    grid[i][j] = 1;
                    mines--;
                }
            }
        }
    }
    grid[r][c] = 0;

    //print();
    //cout << endl;

    bool done = false;
    for (int ro = -1; ro <= 1; ro++) {
        for (int co = -1; co <= 1; co++) {
            int i = r + ro, j = c + co;

            if (0 <= i && i < R && 0 <= j && j < C && grid[i][j]) {
                done = DFS(i, j);
                if (done)
                    break;
            }
        }
        if (done)
            break;
    }
    if (done)
        return true;

    // Restore
    int counter = 0;
    for (int ro = -1; ro <= 1; ro++) {
        for (int co = -1; co <= 1; co++) {
            int i = r + ro, j = c + co;

            if (0 <= i && i < R && 0 <= j && j < C) {
                grid[i][j] = state[counter++];

                if (grid[i][j] == -1)
                    mines++;
            }
        }
    }
    //print();
    //cout << endl;

    return false;
}

void solve() {
    for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++)
            grid[i][j] = -1;
    mines = R * C;

    if (M == (mines-1)) {
        grid[0][0] = 0;
        print();
        return;
    }

    bool done = false;
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            done = DFS(i, j);
            if (done)
                break;
        }
        if (done)
            break;
    }

    if (done) {
        print();
    }
    else {
        cout << "Impossible\n";
    }
}

int main() {
    ios_base::sync_with_stdio(0);

    int t;
    cin >> t;

    for (int cn = 1; cn <= t; cn++) {
        cin >> R >> C >> M;
        cout << "Case #" << cn << ":\n";
        solve();
    }

    return 0;
}

