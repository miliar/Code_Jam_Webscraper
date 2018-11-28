#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

main () {
    freopen ("b.in", "r", stdin);
    freopen ("b.out", "w", stdout);
    int t;
    cin >> t;
    int p = 1;
    while (t--) {
        long double c, f, x;
        cin >> c >> f >> x;
        long double ans = 1000000000;
        long double cur = 0;
        long double d = 2;
        for (int i = 0; i < x; ++i) {
            if (cur + x / d > ans) break;
            else ans = cur + x / d;
            cur += c / d;
            d += f;
        }
        cout.precision(6);
        cout << "Case #" << p << ": " << fixed << ans << "\n";
        ++p;
    }
}
