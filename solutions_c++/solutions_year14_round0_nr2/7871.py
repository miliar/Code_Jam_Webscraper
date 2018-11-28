#include <bits/stdc++.h>

using namespace std;

double Time(int n, double c, double f, double x) {
    double res = x / (2 + n * f);
    for (int i = n - 1; i >= 0; i--) {
        res += c / (2 + i * f);
    }
    return res;
}

void Solve(int t) {
    double c, f, x;
    cin >> c >> f >> x;
    int l = 0, r = 1000000;
    while (r - l > 2) {
        int llr = (2 * l + r) / 3, lrr = (l + 2 * r) / 3;
        if (Time(llr, c, f, x) < Time(lrr, c, f, x)) {
            r = lrr;
        } else {
            l = llr;
        }
    }
    int m = 0;
    for (int i = l; i <= r; i++) {
        if (Time(m, c, f, x) > Time(i, c, f, x)) {
            m = i;
        }
    }
    cout << "Case #" << t << ": " << Time(m, c, f, x) << "\n";
}

int main() {
#ifdef NOVACO
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
#endif
    ios_base::sync_with_stdio(false);
    cout.setf(cout.fixed);
    cout.precision(20);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        Solve(i);
    }
}
