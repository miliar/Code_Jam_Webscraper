#include <bits/stdc++.h>

using namespace std;

int main() {
    int t, k, c, s, tcase = 0;
    cin >> t;
    while (t--) {
        cin >> k >> c >> s;
        printf("Case #%d:", ++tcase);
        if (c == 1) {
            if (k == s) {
                for (int i = 1; i <= k; i++) {
                    printf(" %d", i);
                }
                cout << endl;
                continue;
            } else {
                cout << " IMPOSSIBLE" << endl;
                continue;
            }
        } else {
            if (k == s || s == k - 1) {
                if (k == 1) {
                    cout << " 1" << endl;
                    continue;
                }
                for (int i = 2; i <= k; i++) {
                    printf(" %d", i);
                }
                cout << endl;
                continue;
            } else {
                cout << " IMPOSSIBLE" << endl;
                continue;
            }
        }
    }
    return 0;
}