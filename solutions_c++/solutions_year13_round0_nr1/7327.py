//
//  main.cpp
//  qual
//
//  Created by Alexander Lim on 2013-04-13.
//  Copyright (c) 2013 Alexander Lim. All rights reserved.
//

#include <iostream>

enum {
    X,
    O,
    NEITHER
} typedef WINNER;

WINNER winnerOfRow(const char row[]) {
    char c = ' ';
    
    for (int i = 0; i < 4; i++) {
        if (row[i] == '.') {
            return NEITHER;
        } else if (row[i] != 'T') {
            if (c == ' ') {
                c = row[i];
            } else if (c != ' ' && row[i] != c) {
                return NEITHER;
            }
        }
    }
    
    if (c == 'X') return X;
    else if (c == 'O') return O;
    return NEITHER;
}

bool draw(char ** board) {
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (board[i][j] == '.') return false;
        }
    }
    
    return true;
}

char ** getDiagonals(char ** board) {
    char **diagonals = new char*[1];
    
    for (int i = 0; i < 2; i++) {
        diagonals[i] = new char[3];
        for (int j = 0; j < 4; j++) {
            diagonals[i][j] = board[i ? 3 - j : j][j];
        }
    }
    
    return diagonals;
}

char ** getColumns(char ** board) {
    char **columns = new char*[3];
    
    for (int i = 0; i < 4; i++) {
        columns[i] = new char[3];
        for (int j = 0; j < 4; j++) {
            columns[i][j] = board[j][i];
        }
    }
    
    return columns;
}

void printWinner(WINNER winner, int boardIndex) {
    std::cout << "Case #" << boardIndex + 1 << ": ";
    switch (winner) {
        case X:
            std::cout << "X won\n";
            break;
        case O:
            std::cout << "O won\n";
            break;
        default:
            std::cout << "Function should not be called here...\n";
    }
    
}

void printDraw(int boardIndex) {
    std::cout << "Case #" << boardIndex + 1 << ": Draw\n";
}

void printNotCompleted(int boardIndex) {
    std::cout << "Case #" << boardIndex + 1 << ": Game has not completed\n";
}

int main(int argc, const char * argv[]) {
    int t = 0;
    
    std::cin >> t;
    
    char ** board = new char*[3];
    
    for (int i = 0; i < 4; i++) {
        board[i] = new char[3];
    }
    
    for (int i = 0; i < t; i++) {
        std::cin >> board[0];
        std::cin >> board[1];
        std::cin >> board[2];
        std::cin >> board[3];
        
        char ** columns = getColumns(board);
        char ** diagonals = getDiagonals(board);
        
        bool hasWon = false;
        
        for (int j = 0; j < 4; j++) {
            if (winnerOfRow(board[j]) != NEITHER) {
                printWinner(winnerOfRow(board[j]), i);
                hasWon = true;
                break;
            } else if (winnerOfRow(columns[j]) != NEITHER) {
                printWinner(winnerOfRow(columns[j]), i);
                hasWon = true;
                break;
            } else if (j < 2 && winnerOfRow(diagonals[j]) != NEITHER) {
                printWinner(winnerOfRow(diagonals[j]), i);
                hasWon = true;
                break;
            }
        }
        
        if (!hasWon) {
            draw(board) ? printDraw(i) : printNotCompleted(i);
        }
    }
    
    return 0;
}