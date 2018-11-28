//
//  main.cpp
//  Google CodeJam Qual
//

#include <iostream>
#include <string>

using std::cin;
using std::cout;

const int kN = 4;
const int kOWon = 1;
const int kXWon = 2;
const int kNoOneWon = 3;
const int kIncomplete = 4;

int FigureOutWinner(char matrix[][kN]);

int main(int argc, const char * argv[])
{
    int num_cases = 0;
    cin >> num_cases;
    char matrix[kN][kN];
    
    for (int i=1; i <= num_cases; i++) {
        // read matrix
        for (int r=0; r<kN; r++) {
            for (int c=0; c<kN; c++) {
                cin >> matrix[r][c];
            }
        }

        // figure out win
        cout << "Case #" << i << ": ";
        
        switch (FigureOutWinner(matrix)) {
            case kNoOneWon:
                cout << "Draw";
                break;
            case kOWon:
                cout << "O won";
                break;
            case kXWon:
                cout << "X won";
                break;
            case kIncomplete:
                cout << "Game has not completed";
                break;
        }
        
        cout << std::endl;
    }
    
    
    return 0;
}


int FigureOutWinner(char matrix[kN][kN]) {
    int countO = 0, countX = 0;
    bool empty_space = false;
    
    // check rows
    for (int r=0; r<kN; r++) {
        countO = countX = 0;
        for (int c=0; c<kN; c++) {
            if (matrix[r][c] == 'O' || matrix[r][c] == 'T') {
                countO++;
            };
            if (matrix[r][c] == 'X' || matrix[r][c] == 'T') {
                countX++;
            };
            if (matrix[r][c] == '.') {
                empty_space = true;
            }
        }
        if (countO == kN) {
            return kOWon;
        }
        if (countX == kN) {
            return kXWon;
        }
    }
    
    // check cols
    for (int c=0; c<kN; c++) {
        countO = countX = 0;
        for (int r=0; r<kN; r++) {
            if (matrix[r][c] == 'O' || matrix[r][c] == 'T') {
                countO++;
            };
            if (matrix[r][c] == 'X' || matrix[r][c] == 'T') {
                countX++;
            };
        }
        if (countO == kN) {
            return kOWon;
        }
        if (countX == kN) {
            return kXWon;
        }
    }

    // check main diagnoal
    countO = countX = 0;
    for (int c=0; c<kN; c++) {
            if (matrix[c][c] == 'O' || matrix[c][c] == 'T') {
                countO++;
            };
            if (matrix[c][c] == 'X' || matrix[c][c] == 'T') {
                countX++;
            };
    }
    if (countO == kN) {
        return kOWon;
    }
    if (countX == kN) {
        return kXWon;
    }
    
    // check secondary diagnoal
    countO = countX = 0;
    for (int c=0; c<kN; c++) {
        if (matrix[c][kN-c-1] == 'O' || matrix[c][kN-c-1] == 'T') {
            countO++;
        };
        if (matrix[c][kN-c-1] == 'X' || matrix[c][kN-c-1] == 'T') {
            countX++;
        };
    }
    if (countO == kN) {
        return kOWon;
    }
    if (countX == kN) {
        return kXWon;
    }
    
    
    if (!empty_space)
        return kNoOneWon;
    
    return kIncomplete;
}