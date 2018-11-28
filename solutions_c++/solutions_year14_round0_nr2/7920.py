//Google Code Jam Qualification Round 2014 - Problem B. Cookie Clicker Alpha

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
using namespace std;

bool ifEnd(double C, double F, double X, double rate)
{
    if( ((X-C) / rate ) < ( X / (rate+F) ) )
        return true;
    else
        return false;
}

double findAns(double C, double F, double X)
{
    double rate = 2.0, ans = 0.0, tmp;

    while(!ifEnd(C, F, X, rate))
    {
        tmp = C/rate;//time to buy a farm
        ans += tmp;
        //printf("%.7lf ", ans);
        rate += F;//rate add F
    }

    ans += (X/rate);

    return ans;
}

int main()
{
    FILE * pFile;
    pFile = fopen ("b_output.txt" , "w");

    int T;
    double C, F, X;

    scanf("%d", &T);

    for(int testCase = 1; testCase <= T; testCase++)
    {
        scanf("%lf %lf %lf", &C, &F, &X);
        fprintf(pFile, "Case #%d: ", testCase);

        if( X <= C)
        {
            fprintf(pFile, "%.7lf\n", X/2.0);
            continue;
        }

        fprintf(pFile, "%.7lf\n", findAns(C, F, X));
    }

    fclose (pFile);
    return 0;
}
