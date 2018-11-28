#include <iostream>

using namespace std;

string eval(char board[][4]) {
    //check rows for X
    bool x_wins = false;
    for (int r=0; r<4 && !x_wins; r++) {
        bool x_wins_t = true;
        for (int c=0; c<4; c++) {
            if (board[r][c] != 'X' && board[r][c] != 'T') x_wins_t = false;
        }
        if (x_wins_t) x_wins = true;
    }

    //check rows for O
    bool o_wins = false;
    for (int r=0; r<4 && !o_wins; r++) {
        bool o_wins_t = true;
        for (int c=0; c<4; c++) {
            if (board[r][c] != 'O' && board[r][c] != 'T') o_wins_t = false;
        }
        if (o_wins_t) o_wins = true;
    }

    //check cols for X
    for (int c=0; c<4 && !x_wins; c++) {
        bool x_wins_t = true;
        for (int r=0; r<4; r++) {
            if (board[r][c] != 'X' && board[r][c] != 'T') x_wins_t = false;
        }
        if (x_wins_t) x_wins = true;
    }

    //check cols for O
    for (int c=0; c<4 && !o_wins; c++) {
        bool o_wins_t = true;
        for (int r=0; r<4; r++) {
            if (board[r][c] != 'O' && board[r][c] != 'T') o_wins_t = false;
        }
        if (o_wins_t) o_wins = true;
    }

    //check diags for X
    bool x_wins_t = true;
    for (int i=0; i<4; i++) {
        if (board[i][i] != 'X' && board[i][i] != 'T') x_wins_t = false;
    }
    if (x_wins_t) x_wins = true;

    x_wins_t = true;
    for (int i=0; i<4; i++) {
        if (board[i][3-i] != 'X' && board[i][3-i] != 'T') x_wins_t = false;
    }
    if (x_wins_t) x_wins = true;

    //check diags for O
    bool o_wins_t = true;
    for (int i=0; i<4; i++) {
        if (board[i][i] != 'O' && board[i][i] != 'T') o_wins_t = false;
    }
    if (o_wins_t) o_wins = true;

    o_wins_t = true;
    for (int i=0; i<4; i++) {
        if (board[i][3-i] != 'O' && board[i][3-i] != 'T') o_wins_t = false;
    }
    if (o_wins_t) o_wins = true;

    //check for empties
    bool board_has_empties = false;
    for (int r=0; r<4 && !board_has_empties; r++) {
        for (int c=0; c<4 && !board_has_empties; c++) {
            if (board[r][c] == '.') board_has_empties = true;
        }
    }

    string retstr;
    if (x_wins && !o_wins) retstr = "X won";
    else if (!x_wins && o_wins) retstr = "O won";
    else {
        if (board_has_empties) retstr = "Game has not completed";
        else retstr = "Draw";
    }

    return retstr;
}

int main()
{
    int n;
    cin >> n;

    for (int i=0; i<n; i++) {
        char board[4][4];
        for (int r=0; r<4; r++) {
            for (int c=0; c<4; c++) {
                cin >> board[r][c];
            }
        }

        cout << "Case #" << (i+1) << ": " << eval(board) << endl;
    }

    return 0;
}
