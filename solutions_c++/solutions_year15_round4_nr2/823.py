#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

template < typename T > T next() { T tmp; cin >> tmp; return tmp; }

double eps = 1e-8;

double abs(double a) { return a < 0 ? -a : a; }
bool eq(double a, double b) {
    return abs(a - b) < eps;
}



void solve() {
    int n = next< int >();
    double V = next< double >();
    double X = next< double >();

    vector< double > v(n);
    vector< double > x(n);
    for (int i = 0; i < n; ++i) {
        v[i] = next< double >();
        x[i] = next< double >();
    }
    std::cout.precision(20);
    if (n == 1) {
        if (eq(x[0], X)) {
            cout << V / v[0] << endl;
        } else {
            cout << "IMPOSSIBLE" << endl;
        }
        return;
    }
    if (eq(x[0], X) && eq(x[1], X)) {
        cout << V / (v[0] + v[1]) << endl;
    } else if (eq(x[0], X)) {
        cout << V / v[0] << endl;
    } else if (eq(x[1], X)) {
        cout << V / v[1] << endl;
    } else if ((X - x[0]) * (X - x[1]) < 0) {
        for (int i = 0; i < n; ++i) {
            x[i] = x[i] / X - 1.0;
        }
        double r0 = abs(x[1]);
        double r1 = abs(x[0]);
        double alpha = min(v[0] / r0, v[1] / r1);
        cout << V / (alpha * (r0 + r1)) << endl;
    } else {
        cout << "IMPOSSIBLE" << endl;
    }


}

int main() {
    int t = next< int >();
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        solve();
    }

    return 0;
}
