#include <cstdio>
typedef double Real;

Real solve(Real c, Real f, Real x) {
    Real rate = 2.0;
    Real time = 0.0;
    while(1) {
        Real t1 = x / rate;
        Real t2 = (c / rate) + (x / (rate + f));
        if(t1 <= t2) return time + t1;
        time += c / rate;
        rate += f;
    }
    return time;
}

int main() {
    int t;
    scanf("%d", &t);
    for(int i = 0; i < t; ++i) {
        Real c, f, x;
        scanf("%lf %lf %lf", &c, &f, &x);
        printf("Case #%d: %.7lf\n", i + 1, solve(c, f, x));
    }
}
