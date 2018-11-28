#include <iostream>

using namespace std;

int main() {
    int t;
    cin >> t;
    for (int tc = 0; tc < t; tc++) {
        int x, r, c;
        cin >> x >> r >> c;
        if (x == 1)
            cout << "Case #" << tc + 1 << ": " << "GABRIEL" << endl;
        if (x == 2) {
            if (r == 2 || r == 4 || c == 2 || c == 4)
                cout << "Case #" << tc + 1 << ": " << "GABRIEL" << endl;
            else
                cout << "Case #" << tc + 1 << ": " << "RICHARD" << endl;
        }
        if (x == 3) {
            if ((r == 3 && c != 1) || (r != 1 && c == 3))
                cout << "Case #" << tc + 1 << ": " << "GABRIEL" << endl;
            else
                cout << "Case #" << tc + 1 << ": " << "RICHARD" << endl;
        }
        if (x == 4) {
            if ((r == 4 && c == 4) || (r == 4 && c == 3) || (r == 3 && c == 4))
                cout << "Case #" << tc + 1 << ": " << "GABRIEL" << endl;
            else
                cout << "Case #" << tc + 1 << ": " << "RICHARD" << endl;
        }
    }
return 0;
}