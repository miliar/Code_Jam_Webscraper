#include <cassert>
#include <cstdio>
#include <iostream>


double C, F, X;

double answer()
{
    double currCookies = 0;
    double finalTime = 0.0;
    double rate = 2.0;

    while (currCookies < X)
    {
        double currentTime = X / rate + finalTime;
        double newTime = (C / rate) + X / (rate + F) + finalTime;

        if (newTime < currentTime)
        {
            finalTime += C / rate;
            rate += F;
        }
        else
        {
            currCookies = X;
            finalTime += X / rate;
        }
    }

    return finalTime;
}

int main()
{
    int testCases = 0;

    FILE* fp = fopen("test_in_small.txt", "r");
    fscanf(fp, "%d\n", &testCases);
    
    for (int i = 0; i < testCases; i++)
    {
        fscanf(fp, "%lf %lf %lf\n", &C, &F, &X);
     
        double ans = answer();
        printf("Case #%d: %lf\n", i+1, ans);
    }

    return 0;
}