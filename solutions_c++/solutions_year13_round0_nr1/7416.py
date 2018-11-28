#include <iostream>

using namespace std;

char winner = '\0';

struct Pair {
    int x;
    int y;
};

void printBoard(char board[4][4]) {
    for(int j = 0, x(0), y(0); j < 4; j++, y++) {
        for(int k = 0; k < 4; k++, x++) {
            cout << board[y][x] << "";
        }
        cout << endl;
        x = 0;
    }
}

char letterFinder(int left, int right) {
    //cout << "checking " << left << " " << right << endl;
    if((left - (3*'X' + 'T') == 0) || ((left - 4*'X') == 0) ||
        (right - (3*'X' + 'T') == 0) || ((right - 4*'X') == 0)) {
        return 'X';
    } else if((left - (3*'O' + 'T') == 0) || ((left - 4*'O') == 0) ||
        (right - (3*'O' + 'T') == 0) || ((right - 4*'O') == 0)) {
        return 'O';
    }
    return '\0';
}

char letterFinder(int left) {
    //cout << "checking " << left << endl;
    if((left - (3*'X' + 'T') == 0) || ((left - 4*'X') == 0)) {
        return 'X';
    } else if((left - (3*'O' + 'T') == 0) || ((left - 4*'O') == 0)) {
        return 'O';
    }
    return '\0';
}

void diagonalCheck(char board[4][4]) {
    int left(0), right(0);
    for(int i(0); i < 4; i++) {
        left += board[i][i];
        right += board[i][3-i];
    }
    char temp = letterFinder(left, right);
    if(temp != '\0') winner = temp;
}

void columnCheck(char board[4][4]){
    int col(0);
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 4; j++) {
            col += board[j][i];
        }
        char answer = letterFinder(col);
        if(answer != '\0') winner = answer;
        col = 0;
    }
}

void rowCheck(char board[4][4]){
    int row(0);
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 4; j++) {
            row += board[i][j];
        }
        char answer = letterFinder(row);
        if(answer != '\0') winner = answer;
        row = 0;
    }
}

int main() {
    int input;
    cin >> input;
    char board[4][4];
    Pair temp;
    for(int i = 0; i < input; i++) {
        bool draw(true);
        for(int j = 0, x(0), y(0); j < 4; j++, y++) {
            string line;
            cin >> line;
            for(int k = 0; k < 4; k++, x++) {
                board[y][x] = line[x];
                if(line[x] == '.') draw = false;
            }
            x = 0;
        }
        rowCheck(board);
        columnCheck(board);
        diagonalCheck(board);
        cout << "Case #" << i + 1 << ": ";
        if(winner != '\0') cout << winner << " won";
        else if(draw) cout << "Draw";
        else cout << "Game has not completed";
        cout << endl;
        winner = '\0';
    }
    return 0;
}

//4X = 352
//3X + T = 348
//4O = 316
//3O + T = 321
