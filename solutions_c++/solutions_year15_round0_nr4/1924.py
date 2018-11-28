// for "small" dataset
#include <iostream>
#include <string>
using namespace std;

int T;

int main() {
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int X, R, C;
        cin >> X >> R >> C;
        string w;

        if (X == 1) {
            w = "GABRIEL";
        } else if (X == 2) {
            if ((R*C) % 2 == 0) {
                w = "GABRIEL";
            } else {
                w = "RICHARD";
            }
        } else if (X == 3) {
            if ((R*C) % 3 != 0 || R == 1 || C == 1) {
                w = "RICHARD";
            } else {
                w = "GABRIEL";
            }
        } else if (X == 4) {
            if (R == 1 || C == 1 || (R <= 3 && C <= 3) || (R*C)%4 != 0
                || (R == 4 && C == 2) || (R == 2 && C == 4)) {
                w = "RICHARD";
            } else {
                w = "GABRIEL";
            }
        }
        
        cout << "Case #" << t << ": " << w << endl;
    }
}
