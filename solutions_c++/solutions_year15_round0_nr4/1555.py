#include <bits/stdc++.h>
using namespace std;

void solve() {
    int x, r, c;
    cin >> x >> r >> c;

    if (r > c)
        swap(r, c);

    if (x == 1) {
        cout << "GABRIEL\n";
    } else if (x == 2) {
        if (r * c % 2)
            cout << "RICHARD\n";
        else
            cout << "GABRIEL\n";
    } else if (x == 3) {
        if ((r % 3 == 0 && c % 2 == 0) || (r % 2 == 0 && c % 3 == 0) || (r == 3 && c == 3))
            cout << "GABRIEL\n";
        else
            cout << "RICHARD\n";
    } else if (x == 4) {
        if (c == 4 && r >= 3)
            cout << "GABRIEL\n";
        else
            cout << "RICHARD\n";
    }
}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        printf("Case #%d: ", i + 1);
        solve();
    }
}
