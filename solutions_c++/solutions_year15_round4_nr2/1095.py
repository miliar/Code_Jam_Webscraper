#include <stdio.h>
#include <iostream>
#include <assert.h>

using namespace std;

struct src {
    double c, r;
};

int main() {
    int T, N;
    double V, X;
    src srcs[100];
    src& first = srcs[0];
    src& second = srcs[1];
    cin >> T;
    for(int i=0; i < T; i++) {
        cin >> N >> V >> X;;
        for(int s=0; s < N; s++) {
            cin >> srcs[s].r >> srcs[s].c;
        }
        assert(N <= 2);
        printf("Case #%d: ", i+1);
        if (first.c == second.c && N == 2) {
            N = 1;
            first.r = first.r + second.r;
        }
        if (N == 1) {
            if (first.c == X) {
                printf("%.15lf\n", V / first.r);
            } else {
                printf("IMPOSSIBLE\n");
            }
        } else if (N == 2) {
            if (first.c > X && second.c > X)
                printf("IMPOSSIBLE\n");
            else if (first.c < X && second.c < X)
                printf("IMPOSSIBLE\n");
            else {
                double v0 = V * (X - second.c) / (first.c - second.c);
                double v1 = V - v0;
                double t0 = v0 / first.r;
                double t1 = v1 / second.r;
                //printf("  %.10lf %.10lf\n", t0, t1);
                //printf("  %.10lf %.10lf\n", v0, v1);
                double t = max(t0, t1);
                printf("%.15lf\n", t);
            }
        }
    }
    return 0;
}
