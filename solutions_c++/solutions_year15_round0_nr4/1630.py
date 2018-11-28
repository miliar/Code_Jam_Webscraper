#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("D-small-attempt1.in", "r", stdin);
    freopen("D-small-attempt1.out", "w", stdout);
    int T, x, r, c;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        cin >> x >> r >> c;
        bool win;
        if (r * c % x) {
            win = true;
        } else {
            if (r > c) {
                swap(r, c);
            }
            if (x == 1) {
                win = false;
            } else if (x == 2) {
                win = false;
            } else if (x == 3) {
                if (r == 1 && c == 3) {
                    win = true;
                } else {
                    win = false;
                }
            } else if (x == 4) {
                if (r == 1 && c == 4) {
                    win = true;
                } else if (r == 2 && c == 4) {
                    win = true;
                } else if (r == 2 && c == 2) {
                    win = true;
                } else {
                    win = false;
                }
            }
        }
        printf("Case #%d: %s\n", t, win ? "RICHARD" : "GABRIEL");
    }
    return 0;
}
