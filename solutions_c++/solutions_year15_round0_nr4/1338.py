#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

#define FILENAME "D-small-attempt0.in"

void solve() {
    int X, R, C;
    string G("GABRIEL"), RICH("RICHARD");

    cin >> X >> R >> C;

    if (R < C) {
        std::swap(R, C);
    }

    if (X == 1) {
        cout << G;
        return;
    }

    if (X == 2) {
        if (R * C % 2) {
            cout << RICH;
        } else {
            cout << G;
        }
        return;
    }

    if (X == 3) {
        if (R * C % 3 || C == 1) {
            cout << RICH;
        } else {
            cout << G;
        }
        return;
    }

    if (X == 4) {
        if (C > 3) {
            if (R * C % 4) {
                cout << RICH;
            } else {
                cout << G;
            }
        } else {
            if (C == 3 && R == 4) {
                cout << G;
            } else {
                cout << RICH;
            }
        }
        return;
    }

    if (X == 5) {
        if (C > 4) {
            if (R * C % 5) {
                cout << RICH;
            } else  {
                cout << G;
            }
        } else {
            if (R == 5 && (C == 4)) {
                cout << G;
            } else {
                cout << RICH;
            }
        }
        return;
    }

    if (X == 6) {
        if (C > 4) {
            if (R * C % 6) {
                cout << RICH;
            } else {
                cout << G;
            }
        } else {
            if (R == 6 && C == 4) {
                cout << G;
            } else {
                cout << RICH;
            }
        }
        return;
    }

    if (X > 6) {
        cout << RICH;
        return;
    }

}

int main()
{
    freopen("E:\\contest\\" FILENAME, "r", stdin);
    freopen("E:\\contest\\output", "w", stdout );

    int cases = 0, T;
    cin >> T;

    while (T--) {
        cout << "Case #" << ++cases << ": ";
        solve();

        cout << endl;
    }


    return 0;
}

