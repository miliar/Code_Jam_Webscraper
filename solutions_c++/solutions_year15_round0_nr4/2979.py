#include <iostream>
#include <fstream>
#include <string>

using namespace std;

string resolve(int X, int R, int C) {
    if (X == 1) {
        return "GABRIEL";
    }
    if (X == 2) {
        if (R % 2 ==  1 && C % 2 == 1) {
            return "RICHARD";
        }
        return "GABRIEL";
    }
    if (X == 3) {
        if (R == 1 || C == 1) {
            return "RICHARD";
        }
        if (R % 3 == 0 || C % 3 == 0) {
            return "GABRIEL";
        }
        return "RICHARD";
    }
    if (X == 4) {
        if ((R == 3 && C == 4) || (R == 4 && C == 4) || (R == 4 && C == 3)) {
            return "GABRIEL";
        }
        return "RICHARD";
    }
}

int main() {
    ifstream fi("date.in");
    ofstream fo("out.txt");

    int T;
    fi >> T;

    for (int k = 1; k <= T; k++) {
        int X, R, C;
        fi >> X >> R >> C;
        fo << "Case #" << k << ": " << resolve(X, R, C) << endl;
    }

    return 0;
}
