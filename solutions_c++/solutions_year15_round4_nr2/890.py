#include <bits/stdc++.h>
#define FOR(i, n) for (int i = 0; i < n; ++i)
using namespace std;

typedef long long ll;
void solve() {
    int N;
    double V, T;
    cin >> N >> V >> T;
    vector<double> speed(N), tt(N);
    FOR(i, N) cin >> speed[i] >> tt[i];
    assert(N <= 2);
    cout << fixed << setprecision(6);
    if (N == 1) {
        if (fabs(T - tt[0]) < 1e-8) { cout << V / speed[0] << endl; return; }
        else { cout << "IMPOSSIBLE" << endl; return; }
    }
    if (N == 2) {
        double mx = max(tt[0], tt[1]);
        double mn = min(tt[0], tt[1]);
        if (T - mn > 1e-8 && mx - T >= 1e-8) {
            double v1 = V * (T - tt[1]) / (tt[0] - tt[1]);
            double v2 = V * (tt[0] - T) / (tt[0] - tt[1]);
            double res = max(v1 / speed[0], v2 / speed[1]);
            cout << res << endl;
            return;
        }
        else if (fabs(T - mn) < 1e-8 && fabs(T - mx) < 1e-8) {
            cout << V / (speed[0] + speed[1]) << endl;
            return;
        }
        else if (fabs(T - tt[0]) < 1e-8) {
            cout << V / speed[0] << endl;
        }
        else if (fabs(T - tt[1]) < 1e-8) {
            cout << V / speed[1] << endl;
        }
        else {
            cout << "IMPOSSIBLE" << endl;
        }
        return;
    }
    return;
}

int main() {
    int TestCase;
    cin >> TestCase;
    FOR(caseID, TestCase) {
        cout << "Case #" << caseID + 1 << ": ";
        solve();
    }
    return 0;
}
