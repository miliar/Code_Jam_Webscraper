#include <iostream>

using namespace std;

int main() {
    freopen("d_small.in", "r", stdin);
    freopen("d_small.out", "w", stdout);
    int tt;
    cin >> tt;
    for (int t = 1; t <= tt; t++) {
        int x, r, c;
        cin >> x >> r >> c;
        string p1 = "RICHARD";
        string p2 = "GABRIEL";
        string winner = p2;
        if ((r*c) % x != 0)
            winner = p1;
        if (x >= 3 && min(r, c) == 1)
            winner = p1;
        if (x == 4 && min(r, c) == 2)
            winner = p1;
        cout << "Case #" << t << ": " << winner << endl;
    }
}
