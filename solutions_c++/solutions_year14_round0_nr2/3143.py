#include <cstdio>

double solve()
{
    double C, F, X;
    double R = 2.0;

    scanf("%lf %lf %lf", &C, &F, &X);

    double time_spent = 0.0;
    double lower_b = X;

    while (time_spent < lower_b) {
        if ((time_spent + X/R) < lower_b) {
            lower_b = time_spent + X/R;
        }
        time_spent += C/R;
        R += F;
    }

    return lower_b;
}

int main()
{
    int T = 0;
    scanf("%d", &T);

    for (int i = 0; i < T; ++i) {
        printf("Case #%d: %.7lf\n", i+1, solve());
    }

    return 0;
}
