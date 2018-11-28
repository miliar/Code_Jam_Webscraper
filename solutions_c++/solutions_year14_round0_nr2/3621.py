#include <iostream>
#include <algorithm>
using namespace std;

double solve() {
    double c, f, x;
    cin >> c >> f >> x;

    int k = max(int(x / c - 2 / f), 0);
    double result = 0.0;
    for (int i = 0; i < k; ++i)
        result += c / (2 + i * f);
    result += x / (2 + k * f);

    return result;
}

int main() {
    int tests;
    cin >> tests;
    cout << fixed;
    cout.precision(7);
    for (int t = 1; t <= tests; ++t) {
        double ans = solve();
        cout << "Case #" << t << ": " << ans << '\n';
    }

    return 0;
}

