#include <iostream>
#include <cstdio>
#include <set>

using namespace std;

main () {
    freopen ("a.in", "r", stdin);
    freopen ("a.out", "w", stdout);
    int t;
    cin >> t;
    int p = 1;
    while (t--) {
        int a1, a2;
        cin >> a1;
        --a1;
        int a[4][4], b[4][4];
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                cin >> a[i][j];
            }
        }
        cin >> a2;
        --a2;
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                cin >> b[i][j];
            }
        }
        set <int> m;
        int ans = 0, x;
        for (int i = 0; i < 4; ++i) {
            m.insert(a[a1][i]);
        }
        for (int i = 0; i < 4; ++i) {
            if (m.count(b[a2][i])) {
                ++ans;
                x = b[a2][i];
            }
        }
        cout << "Case #" << p << ": ";
        if (ans == 1) cout << x << "\n";
        else if (ans == 0) cout << "Volunteer cheated!\n";
        else cout << "Bad magician!\n";
        ++p;
    }
}
