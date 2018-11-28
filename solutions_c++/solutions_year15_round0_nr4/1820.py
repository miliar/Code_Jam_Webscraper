#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    int i, t, x, c, r, k;
    cin >> t;
    for(i=0; i<t; ++i) {
        cin >> x >> r >> c;
        k = 0;
        k = r*c;
        if ((k % x) == 0 && k/x >= 1) {
            if((x == 3) && ((r == 3 && c == 1) || (r == 1 && c == 3))) {
                cout << "Case #" << i+1 << ": RICHARD" << '\n';
            }
            else if((x == 4) && ((r == 4 && c == 1) || (r == 1 && c == 4))) {
                cout << "Case #" << i+1 << ": RICHARD" << '\n';
            }
            else if((x == 4) && (r == 2 && c == 2)) {
                cout << "Case #" << i+1 << ": RICHARD" << '\n';
            }
            else if((x == 4) && ((r == 4 && c == 2) || (r == 2 && c == 4))) {
                cout << "Case #" << i+1 << ": RICHARD" << '\n';
            }
            else {
                cout << "Case #" << i+1 << ": GABRIEL" << '\n';
            }
        }
        else {
            cout << "Case #" << i+1 << ": RICHARD" << '\n';
        }
    }
    return 0;
}
