#include <iostream>

using namespace std;

int main()
{
    int T; cin >> T;
    for (int t = 1; t <= T; ++t) {
        int out;
        int X, r, c; cin >> X >> r >> c;
        int R = max(r, c);
        int C = min(r, c);

        if (X == 1) {
            out = 1;
        }
        if (X == 2) {
            if (R*C % 2) {
                out = 0;
            } else {
                out = 1;
            }
        }
        if (X == 3) {
            if  (R*C % 3 || (R == 3 && C == 1)) {
                out = 0;
            } else {
                out = 1;
            }
        }
        if (X == 4) {
            if ( ( (R >= 4 && C >= 3)) && R*C % 4 == 0) {
                out = 1;
            } else {
                out = 0;
            }
        }

        cout << "Case #" << t << ": ";
        if (out) {
            cout << "GABRIEL" << endl;
        } else {
            cout << "RICHARD" << endl;
        }


    }
    return 0;
}
