#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <bitset>
#include <cstdio>
#include <queue>

using namespace std;

void precalc() {

}

bool Equal(double a, double b) {
    return fabs(a - b) < 1e-9;
}

void solve() {
    int n;
    double v, x;
    cin >> n >> v >> x;

    vector<double> r(n), c(n);
    for (int i = 0; i < n; ++i) {
        cin >> r[i] >> c[i];
    }

    if (n == 1) {
        if (Equal(x, c[0])) {
            printf("%lf\n", v / r[0]);
        } else {
            cout << "IMPOSSIBLE" << endl;
        }
        return;
    }

    double ratio;
    if (Equal(c[0], c[1])) {
        if (!Equal(c[0], x)) {
            cout << "IMPOSSIBLE" << endl;
            return;
        }
        ratio = r[1] / (r[0] + r[1]);
    } else {
        ratio = (x - c[0]) / (c[1] - c[0]);
    }

    if (ratio < 0.0 && !Equal(ratio, 0.0)) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }
    if (ratio > 1.0 && !Equal(ratio, 1.0)) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }

    double v1 = v * (1.0 - ratio);
    double v2 = v * ratio;

    double t1 = v1 / r[0];
    double t2 = v2 / r[1];

    printf("%lf\n", max(t1, t2));
}

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    precalc();

    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        cout << "Case #" << test << ": ";
        cerr << test << endl;
        solve();
    }
    return 0;
}
