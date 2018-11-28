#include <iostream>

using namespace std;

const long double EPS = 1e-9;

int main() {
    ios_base::sync_with_stdio(false);
    cout.setf(ios::fixed);
    cout.precision(20);
    int t;
    cin >> t;
    for(int tt = 0; tt < t; tt++) {
        long double c, f, x;
        cin >> c >> f >> x;
        long double k = 2, b = 0, ans = x / 2;
        while(true) {
            long double k0 = k + f, b0 = (b - c) * k0 / k, ans0 = (x - b0) / k0;
            if(ans0 > ans - EPS)
                break;
            k = k0;
            b = b0;
            ans = ans0;
        }
        cout << "Case #" << tt + 1 << ": " << ans << '\n';
    }
    return 0;
}
