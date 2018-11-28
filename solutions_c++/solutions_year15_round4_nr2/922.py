#include <cstdio>
#include <algorithm>

long double solve()
{
    int N;
    long double V, X;
    long double R[2], C[2];

    scanf("%d %Lf %Lf", &N, &V, &X);

    bool all_less_than_x = true;
    bool all_more_than_x = true;
    for (int i = 0; i < N; ++i) {
        scanf("%Lf %Lf", &R[i], &C[i]);
        all_less_than_x = all_less_than_x && (C[i] < X);
        all_more_than_x = all_more_than_x && (C[i] > X);
    }

    if (all_less_than_x || all_more_than_x) return -1;

    if (N == 1) {
        return V / R[0];
    }

    // N == 2

    if (C[0] == C[1]) {
        return V / (R[0] + R[1]);
    }

    long double t0 = (V * (X - C[1])) / (R[0] * (C[0] - C[1]));
    long double t1 = (V * (C[0] - X)) / (R[1] * (C[0] - C[1]));
    return std::max(t0, t1);
}

int main() {
    int T;

    scanf("%d ", &T);
    for(int i = 1; i <= T; ++i) {
        long double s = solve();
        if (s < 0) {
            printf("Case #%d: IMPOSSIBLE\n", i);
        } else {
            printf("Case #%d: %.8Lf\n", i, s);
        }
    }

    return 0;
}
