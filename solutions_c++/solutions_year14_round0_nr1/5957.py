#include <iostream>
using namespace std;

int pan1[16];
int pan2[16];

int main() {
    int tc;
    cin >> tc;

    for (int _tc=1; _tc<=tc; _tc++) {
        int row1, row2;

        cin >> row1;
        for (int i=0; i<16; i++)
            cin >> pan1[i];

        cin >> row2;
        for (int i=0; i<16; i++)
            cin >> pan2[i];

        int matches = 0;
        int lastMatch = 0;
        for (int i=0; i<4; i++) {
            for (int j=0; j<4; j++) {
                if (pan1[(row1-1)*4+i] == pan2[(row2-1)*4+j]) {
                    matches++;
                    lastMatch = pan1[(row1-1)*4+i];
                }
            }
        }

        cout << "Case #" << (_tc) << ": ";
        if (matches == 1) {
            cout << lastMatch << endl;
        } else if (matches > 1) {
            cout << "Bad magician!" << endl;
        } else {
            cout << "Volunteer cheated!" << endl;
        }
    }
    return 0;
}