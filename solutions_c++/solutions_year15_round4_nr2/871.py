
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <string>
#define MAXN (100)
#define EPS (1e-9)

using namespace std;

// xi >= 0
// min max xi
// sum Ri * xi == V
// where sum (Ri * Ci * xi) / (sum Ri * xi) == X
// i.e. sum (Ri * Ci * xi) / V == X
// i.e. sum (Ri * Ci * xi) == V * X

int N;
long long V, X;
long long R[MAXN], C[MAXN];

bool check(double t) {
    // N == 2 for now
    long long RM = max(R[0], R[1]);
    if (RM * t < V)
        return false;
    return true;

}

double solve() {
    if (N == 1) {
        if (C[0] != X)
            return -1;
        return 1.0 * V / R[0];
    }
    // N == 2 for now
    //
    // R0*x0 + R1*x1 == V
    // R0*C0*x0 + R1*C1*x1 == V*X
    // x1 = (V - R0*x0) / R1
    // R0*C0*x0 + C1*(V - R0*x0) == V*X
    // x0 = (V*X-C1*V) / (R0*C0 - C1*R0)
    //    = V * (X - C1) / R0 / (C0 - C1)
    if (C[0] == C[1]) {
        if (C[0] != X)
            return -1;
        else
            return 1.0 * V / (R[0] + R[1]);
    }
    long long xnum = V * (X - C[1]);
    long long xden = R[0] * (C[0] - C[1]);
    if (xnum > 0 && xden < 0)
        return -1;
    if (xnum < 0 && xden > 0)
        return -1;
    double x0 = 1.0 * xnum / xden;

    xnum = V * (X - C[0]);
    xden = R[1] * (C[1] - C[0]);
    if (xnum > 0 && xden < 0)
        return -1;
    if (xnum < 0 && xden > 0)
        return -1;
    // double x1 = 1.0 * (V - R[0] * x0) / R[1];
    double x1 = 1.0 * xnum / xden;
    return max(x0, x1);
    /*
    double low = 0, high = 1.0 * V / min(R[0], R[1]);
    for (int iter = 0; iter < 1000; iter++) {
        double mid = 0.5 * (low + high);
        if (check(mid))
            high = mid;
        else
            low = mid;
    }
    return low;
    */
}

long long read_num() {
    double val;
    cin >> val;
    return (long long) (1e4 * val + 0.5);
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> N;
        V = read_num();
        X = read_num();
        for (int i = 0; i < N; i++) {
            R[i] = read_num();
            C[i] = read_num();
        }

        double r = solve();
        cout << "Case #" << t << ": ";
        if (r < EPS)
            cout << "IMPOSSIBLE" << endl;
        else
            cout << fixed << setprecision(10) << r << endl;
    }
}
