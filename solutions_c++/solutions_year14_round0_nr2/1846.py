#include <iostream>
#include <cstdio>

using namespace std;

int T;
double n, x, f, c, ans;

int main() {
    cin >> T;
    for (int ti = 1; ti <= T; ++ti) {
        cin >> c >> f >> x;
        n = (f * x - 2 * c) * 1.0 / (f * c);
        // cout << n << endl;
        ans = 0;
        int i;
        for (i = 1; i < n; ++i) {
            // cout << c * 1.0 / (2 + (i - 1) * f) << endl;
            ans += c * 1.0 / (2 + (i - 1) * f);
        }
        // cout << x * 1.0 / (2 + (i - 1) * f) << endl;
        ans += x * 1.0 / (2 + (i - 1) * f);
        // cout << "Case #" << ti << ": " << ans << endl;
        printf("Case #%i: %.7f\n", ti, ans);
    }
    return 0;
}
