#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cctype>
using namespace std;
const double eps = 1e-9;
double C, F, X;
int main () {
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int Case;
    scanf("%d", &Case);
    for(int kase = 1; kase <= Case; ++kase) {
        scanf("%lf%lf%lf", &C, &F, &X);
        double tmp = ((X - C) * F) / C;
        double n = (floor)((tmp - 2.0) / F);
        double sum = 0.0;
        double s = 2.0;
        for(double i = 0.0; n + 1.0 - i > eps; i += 1.0){
            sum += C / s;
            s += F;
        }
        sum += X / s;
        printf("Case #%d: %.7lf\n", kase, sum);
    }
    return 0;
}

