#include <iostream>
#include <iomanip>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <list>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int main() {
	int TC, c = 1;
	int board[5][5][5];
	cin >> TC;
	for (int i = 1; i <= 4; i++) {
        for (int j = 1; j <= 4; j++) {
            board[1][i][j] = 1;
        }
    }
    for (int i = 1; i <= 4; i++) {
        for (int j = 1; j <= 4; j++) {
            if (i % 2 == 0) {
                board[2][i][j] = 1;
            } else {
                if (j % 2 == 0) {
                    board[2][i][j] = 1;
                } else {
                    board[2][i][j] = 0;
                }
            }
        }
    }

    board[3][1][1] = 0;
    board[3][1][2] = 0;
    board[3][1][3] = 0;
    board[3][1][4] = 0;

    board[3][2][1] = 0;
    board[3][2][2] = 0;
    board[3][2][3] = 1;
    board[3][2][4] = 0;

    board[3][3][1] = 0;
    board[3][3][2] = 1;
    board[3][3][3] = 1;
    board[3][3][4] = 1;

    board[3][4][1] = 0;
    board[3][4][2] = 0;
    board[3][4][3] = 1;
    board[3][4][4] = 0;

    board[4][1][1] = 0;
    board[4][1][2] = 0;
    board[4][1][3] = 0;
    board[4][1][4] = 0;

    board[4][2][1] = 0;
    board[4][2][2] = 0;
    board[4][2][3] = 0;
    board[4][2][4] = 0;

    board[4][3][1] = 0;
    board[4][3][2] = 0;
    board[4][3][3] = 0;
    board[4][3][4] = 1;

    board[4][4][1] = 0;
    board[4][4][2] = 0;
    board[4][4][3] = 1;
    board[4][4][4] = 1;

	while (TC--) {

        int X, R, C;
        cin >> X >> R >> C;
        cout << "Case #" << c++ << ": ";
        if (board[X][R][C]) {
            cout << "GABRIEL" << endl;
        } else {
            cout << "RICHARD" << endl;
        }

	}
	return 0;
}

