#include <iostream>
using namespace std;

double s[105][2];

int main () {
    int T;
    cin >> T;
    for (int tt = 1; tt <= T; ++tt) {
        int N;
        double V, X;
        cin >> N >> V >> X;
        for (int i = 0; i < N; ++i) {
            cin >> s[i][0] >> s[i][1];
        }

        bool le = false, be = false;
        bool isok = true;
        for (int i = 0; i < N; ++i) {
            if (s[i][1] <= X)  le = true;
            if (s[i][1] >= X)  be = true;
        }

        if (!le || !be) {
            isok = false;
        }

        double tim = 0.0;
        if (N == 1) {
            tim = V / s[0][0];
        } else if (s[0][1] == s[1][1]) {
            tim = V / (s[0][0] + s[1][0]);
        } else {
            double X0 = s[0][1], X1 = s[1][1];
            double V0 = V * (X1 - X) / (X1 - X0);
            double V1 = V - V0;
            tim = max(V0 / s[0][0], V1 / s[1][0]);
        }


        if (!isok) {
            printf("Case #%d: IMPOSSIBLE\n", tt);
        } else {
            printf("Case #%d: %lf\n", tt, tim);
        }
    }

    return 0;
}