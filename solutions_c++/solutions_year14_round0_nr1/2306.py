#include <iostream>
#include <string>
#include <vector>
#include <set>

using namespace std;

namespace problemA {
    void start() {
        int T;
        cin >> T;

        for (int i = 0; i < T; i++) {
            int board[4][4], changed[4][4];
            int row1, row2;
            cin >> row1;
            row1 --;
            for (int j = 0; j < 4; j++) {
                for (int k = 0; k < 4; k++) {
                    cin >> board[j][k];
                }
            }
            cin >> row2;
            row2 --;
            for (int j = 0; j < 4; j++) {
                for (int k = 0; k < 4; k++) {
                    cin >> changed[j][k];
                }
            }

            set<int> found;
            for (int j = 0; j < 4; j++) {
                for (int k = 0; k < 4; k++) {
                    if (board[row1][j] == changed[row2][k]) {
                        found.insert(board[row1][j]);
                    }
                }
            }

            cout << "Case #" << (i+1) << ": ";
            if (found.size() == 0) {
                cout << "Volunteer cheated!" << endl;
            } else if (found.size() == 1) {
                cout << *(found.begin()) << endl;
            } else {
                cout << "Bad magician!" << endl;
            }
        }
    }
}

int main() {
    problemA::start();


    return 0;
}
