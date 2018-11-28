#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

int N;
double V, X;
double R1, C1, R2, C2;

double solve() {
    if (N == 1) {
        if (X == C1) {
            return V / R1;
        } else {
            return -1;
        }
    } else { // N == 2
        if (C1 == X && C2 == X) {
            return V / (R1 + R2);
        } else if (C1 == X) {
            return V / R1;
        } else if (C2 == X) {
            return V / R2;
        } else if (C1 < X && C2 < X) {
            return -1;
        } else if (C1 > X && C2 > X) {
            return -1;
        } else {
            double t1 = V * (X - C2) / R1 / (C1 - C2);
            double t2 = V * (X - C1) / R2 / (C2 - C1);
            return max(t1, t2);
        }
    }
}

int main() {
    int T;
    cin >> T;
    cout.precision(30);
    for (int testcase = 1; testcase <= T; testcase++) {
        double ans = 0;
        cin >> N >> V >> X;
        cin >> R1 >> C1;
        if (N > 1) {
            cin >> R2 >> C2;
        }

        ans = solve();

        cout << "Case #" << testcase << ": ";
        if (ans < 0) {
            cout << "IMPOSSIBLE";
        } else {
            cout << ans;
        }
        cout << endl;
    }
    return 0;
}
