#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream input;
    input.open("input.txt");
    ofstream cout;
    cout.open("output.txt");
    int t;
    input >> t;
    int anwsers[4][4];
    int poss[4];
    int row;
    for (int i = 0; i < t; i++) {
        input >> row;
        for (int x = 0; x < 4; x++) {
            for (int y = 0; y < 4; y++) {
                input >> anwsers[x][y];
            }
        }
        for (int j = 0; j < 4; j++) {
            poss[j] = anwsers[row - 1][j];
        }
        input >> row;
        for (int x = 0; x < 4; x++) {
            for (int y = 0; y < 4; y++) {
                input >> anwsers[x][y];
            }
        }
        int match = 0;
        int matchedval = 0;
        for (int j = 0; j < 4; j++) {
            for (int c = 0; c < 4; c++) {
                if (anwsers[row - 1][j] == poss[c]) {
                    match++;
                    matchedval = poss[c];
                }
            }
        }
        if (match == 0) {
            cout << "Case #" << i + 1 << ": Volunteer cheated!" << endl;
        } else if (match == 1) {
            cout << "Case #" << i + 1 << ": " << matchedval << endl;
        } else {
            cout << "Case #" << i + 1 << ": Bad magician!" << endl;
        }
    }
    return 0;
}
