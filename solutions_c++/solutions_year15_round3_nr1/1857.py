#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int prob = 1; prob <= T; ++prob) {
        int R, C, W;
        cin >> R >> C >> W;
        cerr << R << ' ' << C << ' ' << W << endl;
        int shots;
        if (W == 1 || W >= C-1) shots = C;
        else if (C < 4) shots = C;
        else if (C == 4) {
            //            if (W == 2)
                shots = 3;
        }
        else if (C == 5) {
            if (W == 2) shots = 4;
            else shots = W+1;
        }
        else if (C == 6) {
            if (W == 2) shots = 4;
            else shots = W+1;
        }
        else if (C == 7) {
            if (W == 2) shots = 5;
            else if (W == 3) shots = 5;
            else shots = W+1;
        }
        else if (C == 8) {
            if (W == 2) shots = 5;
            else if (W == 3) shots = 5;
            else shots = W+1;
        }
        else if (C == 9) {
            if (W == 2) shots = 6;
            else if (W == 3) shots = 5;
            else if (W == 4) shots = 6;
            else
                shots = W+1;
        }
        else {
            if (W == 2) shots = 6;
            else if (W == 3) shots = 6;
            else if (W == 4) shots = 6;
            else
                shots = W+1;
        }
        cout << "Case #" << prob << ": " << shots
             << endl;
    }
}
