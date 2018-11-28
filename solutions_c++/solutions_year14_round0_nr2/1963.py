#include <bits/stdc++.h>
using namespace std;


void solve(int test) {
    long double c, f, x;
    cin >> c >> f >> x;
    long double ans = x / 2.0;
    long double tmpans = x / 2.0;
    if (c < x) {
        for (int i = 1; ; ++i) {
            tmpans -= x / (2.0 + (i - 1) * f);
            tmpans += x / (2.0 + i * f);
            tmpans += c / (2.0 + (i - 1) * f);
            if (tmpans > ans) {
                break;
            }
            ans = tmpans;
        }
    }
    cout << "Case #" << test << ": ";
    cout << setprecision(10) << fixed << ans << endl;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("out", "w", stdout);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        solve(i + 1);
    }
    return 0;
}
