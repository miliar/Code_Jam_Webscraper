#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

const double eps = 1e-7;
double C, F, X;

int main()
{
   // freopen("B-small-attempt0.in", "r", stdin);
   // freopen("B-small-attempt0.out", "w", stdout);
    int Cas, t = 1;
    scanf("%d", &Cas);
    while (Cas--) {
        scanf("%lf %lf %lf", &C, &F, &X);
        double s = 2.0, ans = 0;
        while (true) {
            double t1 = X / s, t2 = C / s + X / (s + F);
            if (t1 <= t2 + eps) break;
            ans += C / s;
            s += F;
        }
        ans += X / s;
        printf("Case #%d: %.7f\n", t++, ans);
    }
    return 0;
}

