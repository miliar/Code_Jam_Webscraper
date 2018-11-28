#include <iostream>
using namespace std;

bool caso() {
    int x, r, c;
    cin >> x >> r >> c;
    if ((r*c)%x != 0 or x >= 7) return true;
    if (x == 1 or x == 2) return false;
    if (x == 3 and min(r, c) > 1) return false;
    if (x == 3) return true;
    if (x == 4 and min(r, c) > 2) return false;
    if (x == 4) return true;
    if (x == 5 and min(r, c) > 2) return false;
    if (x == 5) return true;
    return true;
}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) 
        cout << "Case #" << i + 1 << ": " << (caso() ? "RICHARD" : "GABRIEL") << endl;
}