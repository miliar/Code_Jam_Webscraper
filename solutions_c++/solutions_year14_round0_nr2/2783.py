#include <cstdio>

// c is cost of farm
// f is rate of farm
// x is # required

double solve(double c, double f, double x)
{
    double time = 0.0;
    double rate = 2;

    while (true) {
        if ( x/rate < (c/rate + x/(f+rate))) {
            return time + x/rate;
        } else {
            time += c/rate;
            rate += f;
        }
    }
}

int main()
{
    int cases;
    scanf("%d", &cases);
    for(int i = 1; i <= cases; i++) {
        double c, f, x;
        scanf("%lf %lf %lf", &c, &f, &x);
        printf("Case #%d: %.7lf\n", i, solve(c,f,x));
    }
}
