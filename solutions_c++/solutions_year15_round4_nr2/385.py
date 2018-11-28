#include <bits/stdc++.h>

using namespace std;

int N;
double V, X;
double R[100], C[100];

bool eq(double x, double y) {
    return abs(x-y) < 1e-9;
}

double solve() {
    cin >> N >> V >> X;
    for (int i = 0; i < N; i++)
        cin >> R[i] >> C[i];
    
    
    if (N == 2 && eq(C[0], C[1])) {
        R[0] += R[1];
        N = 1;
    }
    
    if (N == 1) {
        if (eq(C[0], X))
            return V / R[0];
        return -1;
    }
    
    if (C[0] > C[1])
        swap(R[0], R[1]), swap(C[0], C[1]);
    if (X < C[0] - 1e-8 || X > C[1] + 1e-8)
        return -1;
    
    
    double v0 = V * (C[1] - X) / (C[1] - C[0]);
    double v1 = V - v0;
    
    double t0 = v0 / R[0];
    double t1 = v1 / R[1];
    
    double cV = t0 * R[0] + t1 * R[1];
    double cT = (t0 * R[0] * C[0] + t1 * R[1] * C[1]) / (t0 * R[0] + t1 * R[1]);
    
    if (!eq(V, cV) || !eq(X, cT))
        printf("fail: %.6f %.6f\n", cV, cT);
    
    return max(t0, t1);
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        double x = solve();
        if (x == -1)
            cout << "IMPOSSIBLE";
        else
            cout << fixed << setprecision(6) << x;
        cout << endl;
    }
    
    return 0;
}
