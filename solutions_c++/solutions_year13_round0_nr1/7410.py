/* Tick Tack Toe Tock
 *
 * (c) 2013 James Redmond - james@exotime.com
 *
 * I forgot how to C++
 */

#include <iostream>
#include <string>
#include <curses.h>
#include <stdlib.h>

using namespace std;

bool debug = false;

void output(string message) {
   /* Output method for debugging */
    if (debug) {
        cout << message << endl;
    }
}

void sleepy() {
    /* Puse method for debugging */
    if (debug) {
        output("Press enter to quit...");
        getch();
    }
}

void printTable( char** table ) {
    int rows=3;
    printf("\n");
    for (int i = 0; i <= rows; i++) {
        for (int j = 0; j <= rows; j++) {
            printf("%c ", table[i][j]);
        }
        printf("\n");
    }
}

void printTableInt( int** table ) {
    int rows=3;
    printf("\n");
    for (int i = 0; i <= rows; i++) {
        for (int j = 0; j <= rows; j++) {
            printf("%i ", table[i][j]);
        }
        printf("\n");
    }
}

bool checkIncomplete( char** table ) {
    int rows=3;
    for (int i = 0; i <= rows; i++) {
        for (int j = 0; j <= rows; j++) {
            if ( table[i][j] == '.' ) {
                return true;
            }
        }
    }
    return false;
}

bool checkTable( int** table ) {
    int rows=3;

    // For every row
    for (int x = 0; x <= rows; x++) {
        for (int y = 0; y <= rows; y++) {
            if ( table[x][y] == 0 ) {
                break;
            }
            if (y == rows) {
                return true;
            }
        }
    }

    // For every column
    for (int x = 0; x <= rows; x++) {
        for (int y = 0; y <= rows; y++) {
            if ( table[y][x] == 0 ) {
                break;
            }
            if (y == rows) {
                return true;
            }
        }
    }

    // Diagonal Down
    for (int x = 0; x <= rows; x++) {
        if (table[x][x] == 0) {
            break;
        }
        if ( x == rows) {
            return true;
        }
    }

    // Diagonal Up
    for (int x = rows; x >= 0; x--) {
        if (table[x][rows-x] == 0) {
            break;
        }
        if ( x == 0) {
            return true;
        }
    }

    return false;
}


int main() {
    // Define variables
    string input, line, blank;
    int tests, result, rows;
    rows = 3;

    // Get the number of tests
    getline(cin, input);
    tests = atol(input.c_str());

    // Run each test
    for (int n = 1; n <= tests; n++) {

        // Create two dimensional arrays for each player.
        char** table = new char*[rows+1];
        int** playerX = new int*[rows+1];
        int** playerO = new int*[rows+1];

        for (int row = 0; row <= rows+1; row++) {
            table[row] = new char[rows+1];
            playerX[row] = new int[rows+1];
            playerO[row] = new int[rows+1];
            for (int column = 0; column <= rows+1; column++) {
                table[row][column] = 0;
                playerX[row][column] = 0;
                playerO[row][column] = 0;
            }
        }

        // Populate table with CIN data.
        for (int x = 0; x <= rows; x++) {
            getline(cin, line);
            for (int y = 0; y <= rows; y++) {
                char val = line.c_str()[y];
                table[x][y] = val;

                // Determine who it credits.
                if (val == 'X') {
                    playerX[x][y] = 1;
                } else if (val == 'O') {
                    playerO[x][y] = 1;
                } else if (val == 'T') {
                    playerX[x][y] = 1;
                    playerO[x][y] = 1;
                }

            }
        }


        // Print the table.
        if (debug) {
            printTable(table);
            printTableInt(playerX);
            printTableInt(playerO);
        }

        cout << "Case #";
        cout << n;
        cout << ": ";

        bool winX, winO;
        winX = checkTable(playerX);
        winO = checkTable(playerO);

        // Figure out who wins.
        if ( winX ) {
            cout << "X won";
        } else if ( winO ) {
            cout << "O won";
        } else if ( !winX && !winO ) {
            // Incomplete?
            if ( checkIncomplete(table) ){
                cout << "Game has not completed";
            } else {
                cout << "Draw";
            }
        }

        cout << "\n";

        // Read the blank line between responses
        getline(cin, blank);
    }

    sleepy();
    return 0;
}
