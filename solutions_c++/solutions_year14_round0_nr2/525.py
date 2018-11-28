#include <iostream>
#include <cstdio>
#include <math.h>

using namespace std;

int T;
double C, F, X;
int main() {
    //freopen("B-large.in", "r", stdin);
    //freopen("output.txt", "w", stdout);
    scanf("%d", &T);
    long n;
    double res;
    for (int i = 1; i <= T; i++) {
        scanf("%lf %lf %lf", &C, &F, &X);
        res = 0.0;
        n = ceil(X/C - 2/F - 2);
        if (n < 0) n = 0;
        for (int j = 0; j <= n; j++)
            res = res + C/(2 + j * F);
        res = res + X/(2 + (n + 1) * F);
        if (res > X/2) res = X/2;
        printf("Case #%d: %.7lf\n", i, res);
    }
}
