#include <iostream>

using namespace std;

int main() {
    freopen("a1.in", "r", stdin);
    freopen("a1.out", "w", stdout);

    int t;
    cin >> t;
    for (int tt = 1; tt <= t; tt++) {
        cerr << tt << endl;
        string s;
        int k;
        cin >> s >> k;
        int n = s.length();
        int cnt = 0;
        for (int i = 0; i + k <= n; i++) {
            if (s[i] == '-') {
                cnt++;
                for (int j = 0; j < k; j++) {
                    if (s[i + j] == '-') {
                        s[i + j] = '+';
                    } else {
                        s[i + j] = '-';
                    }
                }
            }
        }

        for (int i = 0; i < n; i++) {
            if (s[i] == '-') {
                cnt = -1;
            }
        }

        cout << "Case #" << tt << ": ";
        if (cnt == -1) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << cnt << endl;
        }
    }

    return 0;
}