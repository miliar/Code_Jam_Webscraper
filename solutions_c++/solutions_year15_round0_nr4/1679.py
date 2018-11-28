#include <bits/stdc++.h>

using namespace std;

string richard("RICHARD");
string gabriel("GABRIEL");

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int X, R, C;
        cin >> X >> R >> C;

        string winner = richard;

        if (X == 1) {
            winner = gabriel;
        } else if (X > 1 && X < 6) {
            if ((R % X == 0 && C >= X - 1) || (C % X == 0 && R >= X - 1)) {
                winner = gabriel;
            }
        } else if (X == 6) {
            if ((R % X == 0 && C >= 4) || (C % X == 0 && R >= 4)) {
                winner = gabriel;
            }
        }

        cout << "Case #" << t << ": " << winner << endl;
    }

    return 0;
}
