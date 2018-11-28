#include <cstdlib>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

const int BOARD_SIZE = 4,
        WIN_COUNT = 4,
        WIN_COUNT_WITHOUT_T = 3;
const char X_CHARACTER = 'X',
        O_CHARACTER = 'O',
        T_CHARACTER = 'T',
        DOT_CHARACTER = '.';
const string STATUS_X_WON = "X won",
        STATUS_DRAW = "Draw",
        STATUS_GAME_NOT_COMPLETED = "Game has not completed",
        STATUS_O_WON = "O won";
const char* OUTPUT_FILE_NAME = "Tic-Tac-Toe-Tomek.out";

// Get status for specified test case.

string getStatus(string* testCase) {
    int xCount, oCount, tCount, dotCount;

    // Check board.
    for (int i = 0; i < BOARD_SIZE; i++) {
        xCount = 0, oCount = 0, tCount = 0, dotCount = 0;

        // Loop through all columns of row [i + 1].
        for (int j = 0; j < BOARD_SIZE; j++) {
            // Get current character.
            char currentCharacter = (testCase[i]).at(j);

            // Update counts.
            switch (currentCharacter) {
                case X_CHARACTER:
                    xCount++;
                    break;
                case O_CHARACTER:
                    oCount++;
                    break;
                case T_CHARACTER:
                    tCount++;
                    break;
                case DOT_CHARACTER:
                    dotCount++;
                    break;
            }

            // Check counts and return appropriate status.
            if (xCount == WIN_COUNT || (xCount == WIN_COUNT_WITHOUT_T &&
                    xCount + tCount == WIN_COUNT)) {
                return STATUS_X_WON;
            }
            if (oCount == WIN_COUNT || (oCount == WIN_COUNT_WITHOUT_T &&
                    oCount + tCount == WIN_COUNT)) {
                return STATUS_O_WON;
            }
        }

        xCount = 0, oCount = 0, tCount = 0;

        // Loop through all rows of column [i + 1].
        for (int j = 0; j < BOARD_SIZE; j++) {
            // Get current character.
            char currentCharacter = (testCase[j]).at(i);

            // Update counts.
            switch (currentCharacter) {
                case X_CHARACTER:
                    xCount++;
                    break;
                case O_CHARACTER:
                    oCount++;
                    break;
                case T_CHARACTER:
                    tCount++;
                    break;
            }

            // Check counts and return appropriate status.
            if (xCount == WIN_COUNT || (xCount == WIN_COUNT_WITHOUT_T &&
                    xCount + tCount == WIN_COUNT)) {
                return STATUS_X_WON;
            }
            if (oCount == WIN_COUNT || (oCount == WIN_COUNT_WITHOUT_T &&
                    oCount + tCount == WIN_COUNT)) {
                return STATUS_O_WON;
            }
        }
    }

    int xCountUp = 0, xCountDown = 0, oCountUp = 0, oCountDown = 0,
            tCountUp = 0, tCountDown = 0;

    // Go to all rows to check diagonal lines.
    for (int i = 0; i < BOARD_SIZE; i++) {
        // Get current characters for 2 diagonal lines.
        char currentCharacterUp = (testCase[i]).at(i),
                currentCharacterDown = (testCase[i]).at(BOARD_SIZE - i - 1);

        // Update counts.
        switch (currentCharacterUp) {
            case X_CHARACTER:
                xCountUp++;
                break;
            case O_CHARACTER:
                oCountUp++;
                break;
            case T_CHARACTER:
                tCountUp++;
                break;
        }
        switch (currentCharacterDown) {
            case X_CHARACTER:
                xCountDown++;
                break;
            case O_CHARACTER:
                oCountDown++;
                break;
            case T_CHARACTER:
                tCountDown++;
                break;
        }

        // Check counts and return appropriate status.
        if (xCountUp == WIN_COUNT || xCountDown == WIN_COUNT ||
                (xCountUp == WIN_COUNT_WITHOUT_T &&
                xCountUp + tCountUp == WIN_COUNT) ||
                (xCountDown == WIN_COUNT_WITHOUT_T &&
                xCountDown + tCountDown == WIN_COUNT)) {
            return STATUS_X_WON;
        }
        if (oCountUp == WIN_COUNT || oCountDown == WIN_COUNT ||
                (oCountUp == WIN_COUNT_WITHOUT_T &&
                oCountUp + tCountUp == WIN_COUNT) ||
                (oCountDown == WIN_COUNT_WITHOUT_T &&
                oCountDown + tCountDown == WIN_COUNT)) {
            return STATUS_O_WON;
        }
    }

    // Check if game is draw or not completed.
    if (dotCount == 0) {
        return STATUS_DRAW;
    }

    return STATUS_GAME_NOT_COMPLETED;
}

int main(int argc, char** argv) {
    int numberOfTestCases;
    string* testCase;
    string input;
    istringstream inputParser;
    ostringstream outputBuilder;

    // Get number of test cases.
    getline(cin, input);
    inputParser.str(input);
    inputParser >> numberOfTestCases;

    // Get test cases.
    for (int i = 0; i < numberOfTestCases; i++) {
        // Create new test case board.
        testCase = new string[BOARD_SIZE];

        // Get board rows.
        for (int j = 0; j < BOARD_SIZE; j++) {
            getline(cin, input);
            testCase[j] = input;
        }

        // Check game status and add to output.
        outputBuilder << "Case #" << (i + 1) << ": "
                << getStatus(testCase) << '\n';

        // Get blank line.
        getline(cin, input);
    }

    // Display output.
    cout << outputBuilder.str();

    // Save output to file.
    ofstream fileWriter;
    fileWriter.open(OUTPUT_FILE_NAME);
    fileWriter << outputBuilder.str();
    fileWriter.close();

    return EXIT_SUCCESS;
}

