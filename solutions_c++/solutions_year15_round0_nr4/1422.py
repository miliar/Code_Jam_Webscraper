#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("D.in", "r", stdin);
    freopen("D.out", "w", stdout);
    int T;
    cin >> T;
    string g = "GABRIEL";
    string r = "RICHARD";
    for (int test = 0; test < T; test++) {
        int X, R, C;
        cin >> X >> R >> C;
        string s;
        if (X == 1) {
            s = g;
        } else if (X == 2) {
            if (R * C % 2 == 0) {
                s = g;
            } else {
                s = r;
            }
        } else if (X == 3) {
            if (R * C % 3 != 0) {
                s = r;
            } else if (R == 1 || C == 1) {
                s = r;
            } else {
                s = g;
            }
        } else if (X == 4) {
            if (R * C > 10) {
                s = g;
            } else {
                s = r;
            }

        }
        cout << "Case #" << test + 1 << ": " << s << endl;
    }
    return 0;
}

