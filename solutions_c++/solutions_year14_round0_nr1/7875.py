#include <bits/stdc++.h>

using namespace std;

void Solve(int t) {
    int a;
    cin >> a;
    int aa = 0;
    for (int i = 1; i <= 4; i++) {
        for (int j = 1; j <= 4; j++) {
            int c;
            cin >> c;
            if (i == a) {
                aa |= 1 << c;
            }
        }
    }
    int b;
    cin >> b;
    int bb = 0;
    for (int i = 1; i <= 4; i++) {
        for (int j = 1; j <= 4; j++) {
            int c;
            cin >> c;
            if (i == b) {
                bb |= 1 << c;
            }
        }
    }
    int c = aa & bb;
    if (__builtin_popcount(c) == 0) {
        cout << "Case #" << t << ": Volunteer cheated!\n";
    } else if (__builtin_popcount(c) > 1) {
        cout << "Case #" << t << ": Bad magician!\n";
    } else {
        int res = 1;
        while ((1 << res & c) == 0) {
            res++;
        }
        cout << "Case #" << t << ": " << res << "\n";
    }
}

int main() {
#ifdef NOVACO
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
#endif
    ios_base::sync_with_stdio(false);
    cout.setf(cout.fixed);
    cout.precision(20);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        Solve(i);
    }
}