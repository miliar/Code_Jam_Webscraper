#include <iostream>


using namespace std;



int main() {
    // The number of cases
    int T;
    // The board
    char board[4][4];

//    freopen("/Users/Sean/1.in", "r", stdin);
//    freopen("/Users/Sean/1.out", "w", stdout);

    cin >> T;
    for (int k = 0; k < T; k++) {
        // input and judge horizontal
        int has_dot = 0;
        int has_found = 0;
        for (int i = 0; i < 4; i++) {
            cin >> board[i][0];
            int flag = 1;
            for (int j = 1; j <4; j++) {
                cin >> board[i][j];
                if (has_dot == 0 && board[i][j] == '.')
                    has_dot = 1;
                if (board[i][j] != board[i][j - 1] &&
                        board[i][j] != 'T' &&
                        board[i][j - 1] != 'T')
                    flag = 0;
                if (j > 1 && board[i][j - 1] == 'T')
                    if (board[i][j] != board[i][j - 2])
                        flag = 0;

            } // end for j
            if (0 == has_found && 1 == flag) {
                char c = (board[i][0] == 'T')? board[i][3]:board[i][0];
                if (c == 'X' || c == 'O') {
                    cout << "Case #" << k + 1 << ": " << c << " won" << endl;
                    has_found = 1;
                }
            }
        } // end for i
        if (1 == has_found)
            continue;
        // judge vertical
        for (int j = 0; j < 4; j++) {
            int flag = 1;
            for (int i = 1; i < 4; i++) {
                if (board[i][j] != board[i - 1][j] &&
                        board[i][j] != 'T' &&
                        board[i - 1][j] != 'T')
                    flag = 0;
                if (i > 1 && board[i - 1][j] == 'T')
                    if (board[i][j] != board[i - 2][j])
                        flag = 0;
            } // end for i
            if (0 == has_found && 1 == flag) {
                char c = (board[0][j] == 'T')? board[3][j]:board[0][j];
                if (c == 'X' || c == 'O') {
                    cout << "Case #" << k + 1 << ": " << c << " won" << endl;
                    has_found = 1;
                }
                break;
            }
        } // end for j
        if (1 == has_found)
            continue;
        // judge diagonal 1
        int flag = 1;
        for (int i = 1; i < 4; i++) {
            if (board[i][i] != board[i - 1][i - 1] &&
                    board[i][i] != 'T' &&
                    board[i - 1][i - 1] != 'T')
                flag = 0;
            if (i > 1 && board[i - 1][i - 1] == 'T')
                if (board[i][i] != board[i - 2][i - 2])
                    flag = 0;
        }
        if (1 == flag) {
            char c = (board[0][0] == 'T')? board[3][3]:board[0][0];
            if (c == 'X' || c == 'O') {
                cout << "Case #" << k + 1 << ": " << c << " won" << endl;
                has_found = 1;
            }
        }
        if (1 == has_found)
            continue;
        // judge diagonal 2
        flag = 1;
        for (int i = 1; i < 4; i++) {
            if (board[i][3 - i] != board[i - 1][4 - i] &&
                    board[i][3 - i] != 'T' &&
                    board[i - 1][4 - i] != 'T')
                flag = 0;
            if (i > 1 && board[i - 1][4 - i] == 'T')
            if (board[i][3 - i] != board[i - 2][5 - i])
                flag = 0;
        }
        if (1 == flag) {
            char c = (board[0][3] == 'T')? board[3][0]:board[0][3];
            if (c == 'X' || c == 'O') {
                cout << "Case #" << k + 1 << ": " << c << " won" << endl;
                has_found = 1;
            }
        }

        if (1 == has_found)
            continue;
        else {
            if (has_dot) {
                cout << "Case #" << k + 1 << ": Game has not completed" << endl;
            }
            else {
                cout << "Case #" << k + 1 << ": Draw" << endl;
            }
        }
   }

//    fclose(stdin);
//    fclose(stdout);
    return 0;
}