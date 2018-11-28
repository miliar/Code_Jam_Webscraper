#include <stdlib.h>
#include <iostream>
#include <string>

using namespace std;

int main(int argc, char** argv)
{
    // Create lawn
    int cards [4][4];

    int tests;
    cin >> tests;
    string blank;
    getline(cin, blank);

    for (int t = 1; t <= tests; t++)
    {
        int answer;
        cin >> answer;
        answer--;
        getline(cin, blank);

        for (int r = 0; r < 4; r++) {
            for (int c = 0; c < 4; c++) {
                cin >> cards[r][c];
            }
            getline(cin, blank);
        }

        int candidates [4];
        for (int c = 0; c < 4; c++) {
            candidates[c] = cards[answer][c];
        }

        cin >> answer;
        answer--;
        getline(cin, blank);

        for (int r = 0; r < 4; r++) {
            for (int c = 0; c < 4; c++) {
                cin >> cards[r][c];
            }
            getline(cin, blank);
        }

        int result = -1;
        for (int c = 0; c < 4; c++) {
            for (int d = 0; d < 4; d++) {
                if (cards[answer][c] == candidates[d]) {
                    result = result == -1 ? cards[answer][c] : -2;
                }
            }
        }

        cout << "Case #" << t << ": ";
        string msg = "";
        switch (result) {
            case -1: {cout << "Volunteer cheated!"; break;}
            case -2: {cout << "Bad magician!"; break;}
            default: {cout << result; break;}
        }
        cout << "\n";
    }

    return 0;
}

