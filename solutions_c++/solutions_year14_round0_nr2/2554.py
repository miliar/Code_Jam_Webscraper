#include <iostream>

using namespace std;

double
calc(double C, double F, double X, double speed)
{
    if ((X - C) * F - C * speed > 0.0) {
        return calc(C, F, X, speed + F) + C / speed;
    } else {
        return X / speed;
    }
}

int main(int argc, char *argv[])
{
    int T;
    double C, F, X;

    scanf("%d", &T);
    for (int k = 1; k <= T; ++k) {
        scanf("%lf %lf %lf", &C, &F, &X);

        printf("Case #%d: %.10lf\n", k, calc(C, F, X, 2.0));
    }

    return 0;
}
