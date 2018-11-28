#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
    int testCase = 0;
    double C, F, X;
    double minTotalTime;
    double totalTime;
    double totalTimeForC;
    double timeForX;
    double production;
/*
freopen("B.in","r",stdin);
freopen("B.out","w",stdout);
*/
    scanf("%d", &testCase);
    for(int T = 1; T <= testCase; T++)
    {
        scanf("%lf %lf %lf", &C, &F, &X);
        totalTimeForC = 0.0;
        timeForX = 0.0;
        totalTime = 0.0;
        production = 2;
        minTotalTime = X / production;
        while(true)
        {
            totalTimeForC += (C / production);
            production += F;
            timeForX = (X / production);
            totalTime = totalTimeForC + timeForX;
            if(minTotalTime > totalTime)
                minTotalTime = totalTime;
            else
                break;
        }
        printf("Case #%d: %.7lf\n", T, minTotalTime);
    }
    return 0;
}
