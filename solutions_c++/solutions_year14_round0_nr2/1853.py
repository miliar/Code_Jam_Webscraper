#include <cstdio>

int main()
{
    int caseCount;

    scanf(" %d", &caseCount);
    for(int caseIndex = 1; caseIndex <= caseCount; caseIndex++) {
        double C, F, X;
        double cps = 2;
        scanf(" %lf %lf %lf", &C, &F, &X);

        double total = 0;
        while(X / cps > C / cps + (X / (cps + F))) {
            total += (C / cps);
            cps += F;
        }
        total += (X / cps);

        printf("Case #%d: %.7lf\n", caseIndex, total);
    }

    return 0;
}
