#include <iostream>
#include <fstream>
#include <string>

using namespace std;

const string kFilename = "A-small-attempt2.in";
const string kXWon = "X won";
const string kOWon = "O won";
const string kDraw = "Draw";
const string kGameNotCompleted = "Game has not completed";
const int kSizeOfBoard = 16;
const int kRowLength = 4;

void verifyBoard(string board) {
    if (board.size() == 0)
        return;


    static int board_number = 0;
    ++board_number;


    if (board.size() != kSizeOfBoard) {
        cout << "Case #" << board_number << ": " << kGameNotCompleted << endl;
        return;
    }

    int index = 0;

    int numX = 0;
    int numO = 0;
    int wild = 0;

    // check rows
    for (int i = 0; i < kRowLength; ++i) {
        for (int j = 0; j < kRowLength; ++j) {
            index = i * kRowLength + j;
            if (board[index] == 'X')
                ++numX;
            else if (board[index] == 'O')
                ++numO;
            else if (board[index] == 'T')
                ++wild;
            if (numX + wild == 4) {
                cout << "Case #" << board_number << ": " << kXWon << endl;
                return;
            } else if (numO + wild == 4) {
                cout << "Case #" << board_number << ": " << kOWon << endl;
                return;
            }
        }
        numX = 0;
        numO = 0;
        wild = 0;
    }

    // check cols
    for (int i = 0; i < kRowLength; ++i) {
        for (int j = 0; j < kRowLength; ++j) {
            index = j * kRowLength + i;
            if (board[index] == 'X')
                ++numX;
            else if (board[index] == 'O')
                ++numO;
            else if (board[index] == 'T')
                ++wild;
            if (numX + wild == 4) {
                cout << "Case #" << board_number << ": " << kXWon << endl;
                return;
            }
            else if (numO + wild == 4) {
                cout << "Case #" << board_number << ": " << kOWon << endl;
                return;
            }
        }
        numX = 0;
        numO = 0;
        wild = 0;
    }

    // check diag
    for (int i = 0; i < kRowLength; ++i) {
        index = i * kRowLength + i;

        if (board[index] == 'X')
            ++numX;
        else if (board[index] == 'O')
            ++numO;
        else if (board[index] == 'T')
            ++wild;
        if (numX + wild == 4) {
            cout << "Case #" << board_number << ": " << kXWon << endl;
            return;
        }
        else if (numO + wild == 4) {
            cout << "Case #" << board_number << ": " << kOWon << endl;
            return;
        }
    }

    numX = 0;
    numO = 0;
    wild = 0;

    // check diag 2
    int i = kRowLength - 1;
    int j = 0;

    while (i >= 0 && j < kRowLength) {
        index = i * kRowLength + j;

        if (board[index] == 'X')
            ++numX;
        else if (board[index] == 'O')
            ++numO;
        else if (board[index] == 'T')
            ++wild;
        if (numX + wild == 4) {
            cout << "Case #" << board_number << ": " << kXWon << endl;
            return;
        }
        else if (numO + wild == 4) {
            cout << "Case #" << board_number << ": " << kOWon << endl;
            return;
        }
        --i;
        ++j;
    }

    numX = 0;
    numO = 0;
    wild = 0;

    for (int i = 0; i < kSizeOfBoard; ++i) {
        if (board[i] == '.') {
            cout << "Case #" << board_number << ": " << kGameNotCompleted << endl;
            return;
        }
    }
    cout << "Case #" << board_number << ": " << kDraw << endl;
}

void solve() {
    ifstream file(kFilename.c_str());

    string board;
    string line;

    bool first_line = true;
    while (file.good()) {
        if (first_line) {
            first_line = false;
            continue;
        }
        getline(file, line);
        if ((line == "\n" || line == "")) {
            verifyBoard(board);
            board = "";
            continue;
        }

        board += line;
    }
    file.close();
}


int main() {
    solve();
}
