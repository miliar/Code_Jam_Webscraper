#include <cstdio>

double C, F, X;
double best, tek;
double v, dt, t1, t2;

int main() {
    int tc;
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    scanf("%i", &tc);
    for(int tt=1; tt<=tc; ++tt) {
        scanf("%lf %lf %lf", &C, &F, &X);
        v    = 2.0;
        dt   = 0.0;
        best = X / v;
        for(int k=1; k<10000000; ++k) {
            t1  = C / v;
            t2  = X / (v + F);
            tek = dt + t1 + t2;
            if (dt > best) break;
            best = (best > tek) ? tek : best;
            v  += F;
            dt += t1;
        }
        printf("Case #%i: %.12f\n", tt, best);
    }
}