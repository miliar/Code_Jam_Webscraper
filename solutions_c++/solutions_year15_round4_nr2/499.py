#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <climits>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int testcase = 0; testcase < T; testcase++) {
        cout << "Case #" << testcase+1 << ": ";

        int N;
        double V, X, R[100], C[100];
        double MAX = 0.0, MIN = 100.0;
        cin >> N >> V >> X;
        for (int i = 0; i < N; i++) {
            cin >> R[i] >> C[i];
            if (C[i] < MIN)
                MIN = C[i];
            if (C[i] > MAX)
                MAX = C[i];
        }

        if (X < MIN || MAX < X) {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }

        if (N == 1) {
            double T = V / R[0];
            printf("%lf\n", T);
        }
        else if (C[0] == C[1]) {
            double T = V / (R[0] + R[1]);
            printf("%lf\n", T);
        }
        else if (C[0] == X) {
            double T = V / R[0];
            printf("%lf\n", T);
        }
        else if (C[1] == X) {
            double T = V / R[1];
            printf("%lf\n", T);
        }
        else {
            double T0 = (X*V - V*C[1]) / (C[0] - C[1]) / R[0];
            double T1 = (X*V - V*C[0]) / (C[1] - C[0]) / R[1];
            printf("%lf\n", max(T0, T1));
        }

    }
    return 0;
}

// vim: set sw=4:
