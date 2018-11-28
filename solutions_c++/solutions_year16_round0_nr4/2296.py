#include <iostream>
using namespace std;

int main() {
    int t, k, c, s;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cin >> k >> c >> s;
        cout << "Case #" << i << ": ";

        if (k == 1) {
            cout << "1" << endl;
            continue;
        }

        if (c == 1) {
            if (s < k) cout << "IMPOSSIBLE" << endl;
            else {
                for (int i = 1; i <= k; i++) {
                    if (i > 1) cout << " ";
                    cout << i;
                }
                cout << endl;

            }
            continue;
        }

        if (s < k - 1) cout << "IMPOSSIBLE" << endl;
        else {
            for (int i = 0; i < k - 1; i++) {
                if (i) cout << " ";
                cout << (i  * k + i + 2);
            }
            cout << endl;
        }
    }
    return 0;
}
