#include <cstdio>

using namespace std;

int testsCount;

int i;

double C, F, X;

double speed;

int hasSenseToBuild();

int main()
{
    scanf("%d\n", &testsCount);
    for (i = 0; i < testsCount; i++) {
        scanf("%lf%lf%lf\n", &C, &F, &X);

        speed = 2;
        double time = 0.0;
        while (hasSenseToBuild()) {
            time = time + C / speed;
            speed = speed + F;
        }

        time = time + X / speed;

        printf("Case #%d: %0.7lf\n", (i + 1), time);
    }

    return 0;
}

int hasSenseToBuild()
{
    return (C / speed + X / (speed + F)) < (X / speed);
}
