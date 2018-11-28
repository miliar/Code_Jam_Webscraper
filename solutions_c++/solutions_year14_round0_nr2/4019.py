#include <cstdio>
#include <cmath>

double solve(double c, double f, double x) {
    double v=2.0, ans=0.0;
    while (x*f>c*(v+f)) {
        ans += c/v;
        v += f;
    }
    return x/v+ans;
}

int main() {
    int N; scanf("%d", &N);
    for (int casei=1; casei<=N; ++casei) {
        double c, f, x;
        scanf("%lf%lf%lf", &c,&f,&x);
        printf("Case #%d: %0.7f\n", casei, solve(c,f,x));
    }
    return 0;
}
