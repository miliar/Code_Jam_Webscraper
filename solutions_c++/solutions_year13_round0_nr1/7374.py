
#include <string>
#include <vector>
#include <iostream>
using namespace std;

void print_status(vector<string>&board, int casenum) {
    bool full_board = true;
    bool o_won = false;
    bool x_won = false;
    int o, x, t;

    for (int i = 0; i < 4; ++i) {
        o = x = t = 0;
        for (int j = 0; j < 4; ++j) {
            char c = board[i][j];
            t |= c == 'T';
            o += c == 'O';
            x += c == 'X';
            full_board &= c != '.';
        }
        o_won |= (o == 3 && t == 1) || o == 4;
        x_won |= (x == 3 && t == 1) || x == 4;

        o = x = t = 0;
        for (int j = 0; j < 4; ++j) {
            char c = board[j][i];
            t |= c == 'T';
            o += c == 'O';
            x += c == 'X';
        }
        o_won |= (o == 3 && t == 1) || o == 4;
        x_won |= (x == 3 && t == 1) || x == 4;
    }

    o = x = t = 0;
    for (int i = 0; i < 4; ++i) {
        char c = board[i][i];
        t |= c == 'T';
        o += c == 'O';
        x += c == 'X';
    }
    o_won |= (o == 3 && t == 1) || o == 4;
    x_won |= (x == 3 && t == 1) || x == 4;

    o = x = t = 0;
    for (int i = 0; i < 4; ++i) {
        char c = board[i][4 - i - 1];
        t |= c == 'T';
        o += c == 'O';
        x += c == 'X';
    }
    o_won |= (o == 3 && t == 1) || o == 4;
    x_won |= (x == 3 && t == 1) || x == 4;

    string status;
    if (o_won) status = "O won";
    else if (x_won) status = "X won";
    else if (full_board) status = "Draw";
    else status = "Game has not completed";
    cout << "Case #" << casenum << ": " << status << endl;
}


int main() {
    int N;
    string devnull;

    cin >> N;

    for (int i = 0; i < N; ++i) {
        vector<string> board(4);
        getline(cin, devnull);
        for (int j = 0; j < 4; ++j) {
            cin >> board[j];
            getline(cin, devnull);
        }
        print_status(board, i + 1);
    }
    return 0;
}
