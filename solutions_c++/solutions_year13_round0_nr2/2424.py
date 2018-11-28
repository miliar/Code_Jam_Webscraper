#include <iostream>

using namespace std;

int board[100][100];

int max_rows[100]; // max of each row
int max_cols[100]; // max of each col

int main() {
    int T, N, M;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        // N rows, M cols
        cin >> N >> M;
        for (int row=0; row < N; ++row) {
            for (int col=0; col < M; ++col) {
                cin >> board[row][col];
            }
        }

        for (int row=0; row < N; ++row) {
            max_rows[row] = 0;
            for (int col=0; col < M; ++col) {
                if (board[row][col] > max_rows[row]) {
                    max_rows[row] = board[row][col];
                }
            }
        }


        for (int col=0; col < M; ++col) {
            max_cols[col] = 0;
            for (int row=0; row < N; ++row) {
                if (board[row][col] > max_cols[col]) {
                    max_cols[col] = board[row][col];
                }
            }
        }

        bool ok = true;
        for (int row=0; row < N; ++row) {
            for (int col=0; col < M; ++col) {
                int value = board[row][col];
                if ((value != max_rows[row]) && (value != max_cols[col])) {
                    ok = false;
                    break;
                }
            }
        }
        
        cout << "Case #" << t+1 << ": " << (ok? "YES":"NO") << endl;

    }
}



