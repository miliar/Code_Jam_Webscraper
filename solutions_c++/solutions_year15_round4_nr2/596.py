#include <bits/stdc++.h>
using namespace std;

const int N = 100;
double r[N];
double c[N];

void solve(int test) {
    int n; cin >> n;
    double v; cin >> v;
    double x; cin >> x;
    double cool = 1000;
    double hot = -1000;
    for (int i = 0; i < n; ++i) {
        cin >> r[i] >> c[i];
        cool = min(cool, c[i]);
        hot = max(hot, c[i]);
    }
    if (cool > x + 1e-9 || hot + 1e-9 < x) {
        cout << "Case #" << test << ": IMPOSSIBLE\n";
        return;
    }
    if (n == 1) {
        cout << "Case #" << test << ": " << v / r[0] << '\n';
        return;
    }
    if (n == 2 && abs(c[0] - c[1]) <= 1e-9) {
        cout << "Case #" << test << ": " << v / (r[1] + r[0]) << '\n';
        return;
    }
    double xx = (x - c[1]) / (c[0] - c[1]);
    cout << "Case #" << test << ": " << max(xx / r[0], (1 - xx) / r[1]) * v << '\n';
    return;
    double low = 0;
    double high = 1e9;
    for (int run = 0; run < 100; ++run) {
        double mid = (low + high) / 2;
        double sum = 0;
        for (int i = 0; i < n; ++i) sum += mid * r[i] * c[i];
        if (sum >= x) high = mid;
        else low = mid;
    }
    cerr << low << endl;
    cout << "Case #" << test << ": " << low * v << '\n';
}

int main() {
    assert(freopen("B-small-attempt0.in", "r", stdin));
    assert(freopen("B-small-attempt0.out", "w", stdout));
    ios::sync_with_stdio(false);
    cout << fixed << setprecision(12);
    int numTests; cin >> numTests;
    for (int test = 1; test <= numTests; ++test) solve(test);
    return 0;
}
