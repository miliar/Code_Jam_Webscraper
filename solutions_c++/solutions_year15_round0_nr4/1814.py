#include <iostream>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int cn = 1; cn <= t; ++cn) {
        int x, r, c;
        bool rich = false;
        cin >> x >> r >> c;
        if (x == 2) {
            if (((r*c) % 2) == 1) {
                rich = true;
            }
        } else if (x == 3) {
            if ((r == 1) || (c == 1)) {
                rich = true;
            } else if (((r*c) % 3) != 0) {
                rich = true;
            }
        } else if (x == 4) {
            if (((r*c) % 4) != 0) {
                rich = true;
            } else if ((r <= 2) || (c <= 2)) {
                rich = true;
            }
        } else if (x == 5) {
            // todo
        } else if (x == 6) {
            // todo
        } else if (x >= 7) {
            rich = true;
        }
        if (rich) {
            cout << "Case #" << cn << ": " << "RICHARD" << endl;
        } else {
            cout << "Case #" << cn << ": " << "GABRIEL" << endl;
        }
    }
    return 0;
}
