#include <cstdio>
#include <climits>
#include <algorithm>

#define startRate 2

void findBestStrategy(double, double, double&);

double C, F, X;
main()
{
    int caseNum;
    int caseCounter = 1;

    double minTime, accumulateTime = 0;

    scanf("%d", &caseNum);
    while(caseNum--) {
        scanf("%lf%lf%lf", &C, &F, &X);
        minTime = INT_MAX;
        findBestStrategy(startRate, 0, minTime);
        printf("Case #%d: %.7lf\n", caseCounter++, minTime);
    }
}


void findBestStrategy(double currentRate, double accumulateTime, double& minTime) {
    double timeToFinal, timeToFarm;
    timeToFinal = accumulateTime + X/currentRate;
    timeToFarm = accumulateTime + C/currentRate;
    minTime = std::min(minTime, timeToFinal);

    if (minTime <= timeToFinal && minTime <= timeToFarm)
        return;
    findBestStrategy(currentRate + F, timeToFarm, minTime);
}
