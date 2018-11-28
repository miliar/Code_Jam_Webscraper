#include <iostream>
#include <string>
using namespace std;

// true -> richard win
bool solve(int x, int r, int c) {
    // x == 1
    if (x == 1) {
        return false;
    }

    // x == 2
    if ((r*c) % x != 0)
        return true;


    // x == 3
    if (x == 3) {
        if (r == 3 && c >= 2)
            return false;
        if (c == 3 && r >= 2)
            return false;
        return true;
    }

    if (x == 4) {
        if (r == 4 && c == 4)
            return false;
        if (r == 4 && c == 3)
            return false;
        if (r == 3 && c == 4)
            return false;
        return true;
    }

    return false;
}

int main() {
    int N;
    cin >> N;
    for (int t = 1; t <= N; ++t) {
        int X, R, C;
        cin >> X >> R >> C;

        printf("Case #%d: %s\n", t, (solve(X, R, C) ? "RICHARD" : "GABRIEL"));
    }

    return 0;
}
