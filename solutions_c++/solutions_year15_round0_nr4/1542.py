//
// Created by Morteza on 2015-04-11.
//

#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

#define toDigit(c) (c-'0')

int main(int argc, const char *argv[]) {

    ios_base::sync_with_stdio(false);

    int num_cases;
    bool winner;

    cin >> num_cases;

    for (int i = 0; i < num_cases; ++i) {
        int X, R, C;
        cin >> X >> R >> C;

        if (X > R && X > C)
            winner = false;
        else if (ceil(X / 2.0) > R || ceil(X / 2.0) > C)
            winner = false;
        else if ((R * C % X) > 0)
            winner = false;
        else if (X == 4 && R * C == 8)
            winner = false;
        else
            winner = true;

        cout << "Case #" << i + 1 << ": " << (winner ? "GABRIEL" : "RICHARD") << endl;

    }

    return 0;
}
