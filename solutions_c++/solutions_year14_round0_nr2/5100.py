#include <string>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <vector>
#include <set>
#include <cstdio>
#include <cstring>
#include <limits>

using namespace std;

double cps, farmCost, total, ppf, bestTime, totalSeconds;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int cases;
    scanf("%d", &cases);
    for(int i = 1; i <= cases; ++i) {
        cps = 2.0, bestTime = numeric_limits<double>::infinity(), totalSeconds = 0.0;
        scanf("%lf %lf %lf", &farmCost, &ppf, &total);
        while(1) {
            double tempTime = (total / cps) + totalSeconds;
            if(tempTime < bestTime) {
                bestTime = tempTime;
                totalSeconds += farmCost/cps;
                cps += ppf;
            } else {
                printf("Case #%d: %.7f\n", i, bestTime);
                break;
            }
        }
    }
    return 0;
}
