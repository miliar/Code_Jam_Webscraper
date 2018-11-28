#include <iostream>
#include <algorithm>

using namespace std;

int T, n, x, y, p;
double a[1002], b[1002];

int main() {
    cin >> T;
    for (int ti = 1; ti <= T; ++ti) {
        cin >> n;
        for (int i = 1; i <= n; ++i)
            cin >> a[i];
        for (int i = 1; i <= n; ++i)
            cin >> b[i];
        sort(a + 1, a + n + 1);
        sort(b + 1, b + n + 1);

        // for (int i = 1; i <= n; ++i)
        //     cout << a[i] << " ";
        // cout << endl;
        // for (int i = 1; i <= n; ++i)
        //     cout << b[i] << " ";
        // cout << endl;

        p = n;
        x = 0;
        for (int i = n; i >= 1; --i) {
            if (a[p] > b[i]) {
                x++;
                p--;
            }
        }
        p = 1;
        y = n;
        for (int i = 1; i <= n && p <= n; ++i) {
            if (b[p] > a[i]) {
                y--;
                p++;
                // cout << "#" << p << endl;
            } else {
                while (p <= n && b[p] <= a[i])
                    p++;
                if (p <= n) {
                    y--;
                    p++;
                }
            }
        }

        cout << "Case #" << ti << ": " << x << ' ' << y << endl;
    }
    return 0;
}
