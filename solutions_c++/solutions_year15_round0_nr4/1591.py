#include <bits/stdc++.h>

using namespace std;

void print(string res, int t) {
    cout << "Case #" << t << ": " << res << endl;
}

int main() {
    freopen("in", "r", stdin); freopen("out", "w", stdout);
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        int x, r, c;
        cin >> x >> r >> c;
        if (x > 6 || ((r * c) < x) || ((r * c) % x)) {
            print("RICHARD", i);
        } else if (x > 2 && min(r, c) <= (x + (x > 3)) / 2) {
            print("RICHARD", i);
        } else {
            print("GABRIEL", i);
        }
    }
    return 0;
}
