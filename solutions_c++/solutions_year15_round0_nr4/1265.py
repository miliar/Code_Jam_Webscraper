#include <iostream>

using namespace std;

int X, R, C, T;

int main() {
    cin >> T;
    for(int t = 1; t <= T; t++) {
        cin >> X >> R >> C;
        bool can;
        if(R < C) {
            int temp = C;
            C = R;
            R = temp;
        }
        if(X == 1) {
            can = true;
        } else if(X == 2) {
            can = ((R*C)%2) == 0;
        } else if(X == 3) {
            if((R == 3 && C == 3) ||
               (R == 4 && C == 3) ||
               (R == 3 && C == 2)) {
                can = true;
            } else {
                can = false;
            }
        } else {
            if((R == 4 && C == 3) ||
               (R == 4 && C == 4)) {
                can = true;
            } else {
                can = false;
            }
        }
        cout << "Case #" << t << ": ";
        if(can) {
            cout << "GABRIEL\n";
        } else {
            cout << "RICHARD\n";
        }
    }
}
