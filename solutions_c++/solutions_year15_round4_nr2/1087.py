#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

double r[128];
double c[128];
double t[128];

double solve() {
    int n;
    double v, x;
    cin >> n >> v >> x;
    bool above = false, below = false;
    bool ay = false, by = false;
    for (int i = 0; i < n; ++i) {
        cin >> r[i] >> c[i];
        if (c[i] <= x) below = true;
        if (c[i] >= x) above = true;

        if (c[i] < x) ay = true;
        if (c[i] > x) by = true;
    }
    if (!(above && below)) return -1;

    if (!ay || !by) {
        // some are on the edge, no other below or above, must use those
        double rates = 0;
        for (int i = 0; i < n; ++i) {
            if (c[i] == x) {
                rates += r[i];
            }
        }
        return v / rates;
    }

    double total_heat = v * x;

    // SMALL INPUT
    if (n > 2) return -1;

    double result = 0.0f;

    t[1] = r[0] * (x - c[0]) / r[1] / (c[1] - x);
    t[0] = 1.0f;
    double vol = t[0] * r[0] + t[1] * r[1];
    double multiple = v / vol;

    return max(t[0] * multiple, t[1] * multiple);
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        //cout << "Case #" << i << ": " << solve() << "\n";
        double res = solve();
        if (res >= 0) {
            printf("Case #%d: %.6f\n", i, res);
        } else {

            printf("Case #%d: IMPOSSIBLE\n", i);
        }
    }
}
