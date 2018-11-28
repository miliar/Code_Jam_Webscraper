#include <iostream>
#include <vector>
using namespace std;

int main() {
    int T;
    cin >> T;
    for(int t = 0;  t < T; t++) {
        int x, r, c;
        cin >> x >> r >> c;
        cout << "Case #" << t + 1 << ": ";
        // Always possible with x = 1.
        if(x == 1) {
            cout << "GABRIEL" << endl;
        }
        // The number of squares is not a multiple of x.
        else if((r * c) % x != 0) {
            cout << "RICHARD" << endl;
        }
        // There is some x-omino that doesn't fit either r or c.
        else if(x > 2 * min(r, c) + 1) {
            cout << "RICHARD" << endl;
        }
        // x is larger than both r and c.
        else if(x > r && x > c) {
            cout << "RICHARD" << endl;
        }
        else if((r == 1 || c == 1) && x > 2) {
            cout << "RICHARD" << endl;
        }
        else if(x == 2) {
            cout << "GABRIEL" << endl;
        }
        else if(x == 3 && min(r,c) == 2 && max(r,c) == 3) {
            cout << "GABRIEL" << endl;
        }
        else if(x == 3 && (r == 3 || c == 3)) {
            cout << "GABRIEL" << endl;
        }
        else if(x == 4 && min(r,c) == 2 && max(r,c) == 4) {
            cout << "RICHARD" << endl;
        }
        else if(x == 4 && (r == 4 || c == 4)) {
            cout << "GABRIEL" << endl;
        }
        else {
            cout << endl;
        }
    }
    return 0;
}
