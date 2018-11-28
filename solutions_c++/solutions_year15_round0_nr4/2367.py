/*
*/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
using namespace std;

string Check(int X, int R, int C) {
    int s = R * C;
    if (0 != s % X) return "RICHARD";
    if (1 == X) return "GABRIEL";
    if (2 == X) { // 2*1
        if (0 == R % 2 || 0 == C % 2) return "GABRIEL";
        else return "RICHARD";
    }

    if (3 == X) {       // 3*2 or 1*3
        if (R * C >= 6 && (0 == R % 3 || 0 == C % 3)) return "GABRIEL";
        else return "RICHARD";
    }

    if (4 == X) {       // if: 1 <= X, R, C <= 4
        if (R * C >= 12) return "GABRIEL";
        else return "RICHARD";
    }
}

int main(int argc, char *argv[])
{
    int T, X, R, C;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        cin >> X >> R >> C;
        cout << "Case #" << i + 1 << ": " << Check(X, R, C) << endl;
    }
    return 0;
}
