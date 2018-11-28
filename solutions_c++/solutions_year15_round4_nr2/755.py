#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
using namespace std;

double eps = 1e-9;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        long N;
        double V, X;
        double R[N], C[N];
        cin >> N >> V >> X;
        for (int i = 0; i < N; i++) cin >> R[i] >> C[i];

        double time;
        int impossible = 0;
        if (N == 1) R[1] = 0, C[1] = C[0];
        if (fabs(C[0] - C[1]) <= eps) {
            if (fabs(C[0] - X) > eps) impossible = 1;
            else time = V / (R[0] + R[1]);
        } else {
            double v0 = V * (X - C[1]) / (C[0] - C[1]);
            double v1 = V - v0;
            double t0 = v0 / R[0];
            double t1 = v1 / R[1];
            if ((C[0]>X && C[1]>X) || (C[0]<X && C[1]<X)) impossible = 1;
            else time = max(t0, t1);
        }

        cout << "Case #" << t << ": ";
        if (impossible) cout << "IMPOSSIBLE" << endl;
        else printf("%.9f\n", time);
    }
}
