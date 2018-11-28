#include <stdio.h>
#include <set>
#include <vector>
int main(){
    freopen("B-large.in","r",stdin);
    freopen("output.txt", "w", stdout);
    int nTest, iCurrentTest;
    double C, F, X, dTime, dTemp, dBest, dCookie, dTarget;
    scanf("%d", &nTest);
    for (iCurrentTest = 1; iCurrentTest <= nTest; iCurrentTest++)
    {
        scanf("%lf%lf%lf", &C, &F, &X);
        dTime = 0.0;
        dCookie = 2.0;
        dBest = X / dCookie;
        while ((dTemp = (dTime + C / dCookie + X / (dCookie + F))) < dBest)
        {
            dBest = dTemp;
            dTime = dTime + C / dCookie;
            dCookie = dCookie + F;
        }
        printf("Case #%d: %.7lf\n", iCurrentTest, dBest);
    }
    return 0;
}