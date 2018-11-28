#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

template <typename T>
T abs(T x) {
    return x < 0 ? -x : x;
}

const double EPS = 1e-9;

void solve() {
    int n;
    double v, x;
    cin >> n >> v >> x;
    vector<double> r(n), c(n);
    for (int i = 0; i < n; ++i)
        cin >> r[i] >> c[i];

    if (n == 1) {
        if (c[0] != x) {
            //cerr << "case 1" << endl;
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << v / r[0] << endl;
        }
    } else if (n == 2) {
        if (c[0] == c[1]) {
            if (c[0] != x) {
                //cerr << "case 2" << endl;
                cout << "IMPOSSIBLE" << endl;
            } else {
                cout << v / (r[0] + r[1]) << endl;
            }
            return;
        }
        double v1 = v * (x - c[1]) / (c[0] - c[1]);
        double v2 = v - v1;
        if (abs(v1) < EPS)
            v1 = +0.0;
        if (abs(v2) < EPS)
            v2 = +0.0;
        //cout << "v: " << v1 << ' ' << v2 << endl;
        if (v1 < 0 || v2 < 0) {
            //cerr << "case 3" << endl;
            cout << "IMPOSSIBLE" << endl;
            return;
        }
        cout << max(v1 / r[0], v2 / r[1]) << endl;
    } else {
        throw exception();
    }
}

int main() {
    int tests;
    cin >> tests;
    cout << fixed << setprecision(10);
    for (int t = 1; t <= tests; ++t) {
        cout << "Case #" << t << ": ";
        solve();
    }

    return 0;
}

