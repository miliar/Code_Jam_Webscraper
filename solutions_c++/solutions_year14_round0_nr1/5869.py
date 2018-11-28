#include <iostream>
#include <fstream>

using namespace std;

int main() {
    int numCases;
    int row1;
    int row2;
    int array1[4][4];
    int array2[4][4];
    int possible[4];

    ifstream inFile("magic-trick.in");
    ofstream outFile("magic-trick.out");

    inFile >> numCases;

    for (int i = 0; i < numCases; ++i) {
        int matching = 0;
        int card = 0;

        inFile >> row1;
        for (int j = 0; j < 4; ++j)
        {
            for (int k = 0; k < 4; ++k)
            {
                inFile >> array1[j][k];
            }
        }

        inFile >> row2;
        for (int j = 0; j < 4; ++j)
        {
            for (int k = 0; k < 4; ++k)
            {
                inFile >> array2[j][k];
            }
        }

        for (int j = 0; j < 4; ++j)
        {
            possible[j] = array1[row1 - 1][j];
        }

        for (int j = 0; j < 4; ++j)
        {
            for (int k = 0; k < 4; ++k)
            {
                if (possible[j] == array2[row2 - 1][k]) {
                    matching++;
                    card = possible[j];
                }
            }
        }

        outFile << "Case #" << i + 1 << ": ";
        if (matching == 1) outFile << card;
        else if (matching == 0) outFile << "Volunteer cheated!";
        else outFile << "Bad magician!";

        outFile << endl;
    }

    return 0;
}