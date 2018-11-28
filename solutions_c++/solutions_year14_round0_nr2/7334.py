#include <cstdio>
double time(double C, double F, double X, double a) {
    if ((C / a + X / (a + F)) > (X / a))
        return (X / a);
    return ((C / a) + time(C, F, X, a + F));
}
int main()
{
    int T;
    double C, F, X, a;
    scanf("%d", &T);
    for (int n = 1; n <= T; n++) {
        a = 2;
        scanf("%lf%lf%lf", &C, &F, &X);
        printf("Case #%d: %.7f\n", n, time(C, F, X, a));
    }
    return 0;
}
