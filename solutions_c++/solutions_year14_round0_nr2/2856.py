#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <iostream>
using namespace std;

double getAns(double C, double F, double X) {
    double mini = X / 2;
    
    if (C >= X)
        return mini;
    
    double tim = 0, spd = 2;
    while (true) {
        double ntim = tim + X / spd;
        if (ntim > mini)
            break;
        mini = ntim;
        tim += C / spd;
        spd += F;
    }

    return mini;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int cas=1; cas<=T; ++cas) {
        double C, F, X, ans;
        scanf("%lf%lf%lf", &C, &F, &X);
        ans = getAns(C, F, X);
        printf("Case #%d: %lf\n", cas, ans);
    }
    return 0;
}
