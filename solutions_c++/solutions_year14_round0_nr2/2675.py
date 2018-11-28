#include <stdio.h>

using namespace std;

int T;

int main() {
    double C, F, X;

    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    scanf("%d", &T);

    for (int t = 1;t <= T;t++) {
        scanf("%lf %lf %lf", &C, &F, &X);

        if (X <= C) {
            printf("Case #%d: %.20lf\n", t, X/2);
            continue;
        }

        int N = double(double(X/C) - double(double(2)/F));

        double res = X/(2 + F * N);

        double v = 2;

        for (int i = 0;i < N;i++, v += F) {
            res += C/v;
        }

        printf("Case #%d: %.20lf\n", t, res);
    }
    return 0;
}
