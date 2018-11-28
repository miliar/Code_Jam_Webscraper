#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>

using namespace std;

int N;
double V, X;
double R[100], C[100];
double eps = 1e-10;

void solve_small() {
    if (N == 1) {
        if (abs(C[0] - X) > eps) {
            printf("IMPOSSIBLE\n");
            return;
        }
        double ret = V / R[0];
        printf("%.9lf\n", ret);
        return;
    }
    if (C[0] > eps + X && C[1] > eps + X) {
        printf("IMPOSSIBLE\n");
        return;
    }
    if (C[0] < X - eps && C[1] < X - eps) {
        printf("IMPOSSIBLE\n");
        return;
    }
    if (abs(C[0] - C[1]) <= eps) {
        double ret = V / (R[0] + R[1]);
        printf("%.9lf\n", ret);
        return;
    }
    double v0 = V * (X - C[1]) / (C[0] - C[1]);
    double v1 = V - v0;
    double ret = max(v0 / R[0], v1 / R[1]);
    printf("%.9lf\n", abs(ret));
}

int main() {
    int T;
    scanf("%d", &T);
    for (int test = 1; test <= T; ++ test) {
        scanf("%d%lf%lf", &N, &V, &X);
        for (int i = 0; i < N; ++ i)
            scanf("%lf%lf", &R[i], &C[i]);
        printf("Case #%d: ", test);
        solve_small();
    }
    return 0;
}
