// Willie Zhu
// 4-2-2013
// google code jam gcj
// tic-tac-toe-tomek

#include <iostream>
#include <fstream>

using namespace std;

int numCases;
char grid[4][4];
int count = 0;

int main() {

    ifstream inFile("tic-tac-toe-tomek.in");
    ofstream outFile("tic-tac-toe-tomek.out");

    inFile >> numCases;

    for (int cases = 0; cases < numCases; cases++) {

        int numXWins = 0, numOWins = 0, numEmpty = 0;

        for (int i = 0; i < 4; i++) {

            for (int j = 0; j < 4; j++) {

                char c;
                inFile >> c;
                grid[i][j] = c;

            }

        }

        // across, X

        for (int i = 0; i < 4; i++) {

            count = 0;

            for (int j = 0; j < 4; j++) {

                if (grid[i][j] == 'X' || grid[i][j] == 'T') count++;

            }

            if (count == 4) numXWins++;

        }

        // across, Y

        for (int i = 0; i < 4; i++) {

            count = 0;

            for (int j = 0; j < 4; j++) {

                if (grid[i][j] == 'O' || grid[i][j] == 'T') count++;

            }

            if (count == 4) numOWins++;

        }

        // down, X

        for (int i = 0; i < 4; i++) {

            count = 0;

            for (int j = 0; j < 4; j++) {

                if (grid[j][i] == 'X' || grid[j][i] == 'T') count++;

            }

            if (count == 4) numXWins++;

        }

        // down, Y

        for (int i = 0; i < 4; i++) {

            count = 0;

            for (int j = 0; j < 4; j++) {

                if (grid[j][i] == 'O' || grid[j][i] == 'T') count++;

            }

            if (count == 4) numOWins++;

        }

        // diagonal top left to lower right, X

        count = 0;

        for (int i = 0; i < 4; i++) {

            if (grid[i][i] == 'X' || grid[i][i] == 'T') count++;

        }

        if (count == 4) numXWins++;

        // diagonal top left to lower right, Y

        count = 0;

        for (int i = 0; i < 4; i++) {

            if (grid[i][i] == 'O' || grid[i][i] == 'T') count++;

        }

        if (count == 4) numOWins++;

        // diagonal top right to lower left, X

        count = 0;

        for (int i = 0; i < 4; i++) {

            if (grid[3 - i][i] == 'X' || grid[3 - i][i] == 'T') count++;

        }

        if (count == 4) numXWins++;

        // diagonal top right to lower left, X

        count = 0;

        for (int i = 0; i < 4; i++) {

            if (grid[3 - i][i] == 'O' || grid[3 - i][i] == 'T') count++;

        }

        if (count == 4) numOWins++;

        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (grid[i][j] == '.') numEmpty++;

            }
        }

        outFile << "Case #" << cases + 1 << ": ";

        if (numXWins > 0 && numOWins > 0 || numXWins == 0 && numOWins == 0 && numEmpty == 0) outFile << "Draw";
        else if (numXWins > 0) outFile << "X won";
        else if (numOWins > 0) outFile << "O won";
        else outFile << "Game has not completed";

        outFile << endl;

    }

}
