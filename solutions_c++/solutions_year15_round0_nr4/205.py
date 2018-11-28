#include <cstdlib>
#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int X, R, C;
        int gab;
        cin >> X >> R >> C;
        if (X == 1) {
            gab = 1;
        } else if (X == 2) {
            if (R * C % 2 == 0) {
                gab = 1;
            } else {
                gab = 0;
            }
        } else if (X == 3) {
            if (R > 1 and C > 1 and R * C % 3 == 0) {
                gab = 1;
            } else {
                gab = 0;
            }
        } else if (X == 4) {
            if (R * C % 4 == 0 and R > 2 and C > 2) {
                gab = 1;
            } else {
                gab = 0;
            }
        } else if (X == 5) {
            if (R > C) swap(R, C);
            if (R * C % 5 == 0 and ((R >= 3 and C >= 10) or (R>=4 and C>=5))) {
                gab = 1;
            } else {
                gab = 0;
            }
        } else if (X == 6) {
            if (R > C) swap(R, C);
            if (R * C % 6 == 0 and (R >= 4 and C >= 6)) {
                gab = 1;
            } else {
                gab = 0;
            }
        } else if (X >= 7) {
            gab = 0;
        }
        cout << "Case #" << t << ": " << (gab ? "GABRIEL" : "RICHARD") << endl;
    }
}
