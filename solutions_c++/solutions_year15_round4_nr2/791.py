#include <iostream>
#include <cstdio>

using namespace std;
int N;
double V, X;
double R[10], C[10];
int main() {
    freopen("B-small-attempt3.in", "r", stdin);
    freopen("B-small.out", "w", stdout);
    int T;
    cin>>T;
    for (int cc = 1; cc <= T; cc++) {
        cin>>N>>V>>X;
        for (int i = 0; i < N; i++)
            cin>>R[i]>>C[i];

        if (N == 1) {
            if (X == C[0]) {
                printf("Case #%d: %.11lf\n", cc, V / R[0]);
            } else {
                printf("Case #%d: IMPOSSIBLE\n", cc);
            }
            continue;
        }

        if (X == C[0] && X == C[1]) {
            printf("Case #%d: %.11lf\n", cc, V / (R[0] + R[1]));
            continue;
        }

        if (C[0] == C[1]) {
            printf("Case #%d: IMPOSSIBLE\n", cc);
            continue;
        }

        double c0 = C[0] - X, c1 = C[1] - X;
        double v0 = -c1 * V / (c0 - c1);
        double v1 = -c0 * V / (c1 - c0);
        if (v0 >= 0 && v1 >= 0) {
            double t1 = v0 / R[0], t2 = v1 / R[1];
            printf("Case #%d: %.11lf\n", cc, max(t1, t2));
        } else {
            printf("Case #%d: IMPOSSIBLE\n", cc);
        }
    }
    return 0;
}
