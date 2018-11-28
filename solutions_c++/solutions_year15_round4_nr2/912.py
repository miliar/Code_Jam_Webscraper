#include <stdio.h>

int T;
int N;
double X;
double V;
double C1;
double C2;
double R1;
double R2;

int same(double a, double b) {
    double x = a - b;
    if (x < 0.0) {
        x = -x;
    }
    return x < 1e-6 ;
}

int main()
{
    scanf("%d", &T);
    for(int z= 1; z<=T;z++) {
        scanf("%d%lf%lf", &N, &V, &X);
        if (N == 1) {
            scanf("%lf%lf", &R1, &C1);
            if (same(C1, X)) {
                printf("Case #%d: %.20lf\n", z, V/R1);
            } else {
                printf("Case #%d: IMPOSSIBLE\n", z);
            }
        } else {
            scanf("%lf%lf%lf%lf", &R1, &C1, &R2, &C2);
            C1 -= X;
            C2 -= X;
            if (same(C1, 0.0) && same(C2, 0.0)) {
                printf("Case #%d: %.20lf\n", z, V/(R1+R2));
            } else if (same(C1, 0.0)) {
                    printf("Case #%d: %.20lf\n", z, V/R1);
            } else if (same(C2, 0.0)) {
                    printf("Case #%d: %.20lf\n", z, V/R2);
            } else if (C1 > 0.0 && C2 > 0.0) {
                printf("Case #%d: IMPOSSIBLE\n", z);
            } else if (C1 < 0.0 && C2 < 0.0) {
                printf("Case #%d: IMPOSSIBLE\n", z);
            } else {
                double V1 = V * C2 / (C2 - C1);
                double V2 = V * C1 / (C1 - C2);
                if (V1/R1 > V2/R2) {
                    printf("Case #%d: %.20lf\n", z, V1/R1);
                } else {
                    printf("Case #%d: %.20lf\n", z, V2/R2);
                }
            }
        }
    }

    return 0;
}

