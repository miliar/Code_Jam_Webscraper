#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cctype>
#include <iostream>
#include <cstdio>

using namespace std;

double calculateTime(double c, double f, double x)
{
    double totalTime, timeToBuyAFirm, timeToGainAllCookies, timeToGainAllCookies2, rate, cookies;

    rate = 2.0;
    totalTime = 0.0;
    cookies = 0.0;

    while(true)
    {
        timeToBuyAFirm = c / rate;
        timeToGainAllCookies = x / rate;
        timeToGainAllCookies2 = timeToBuyAFirm + x / (rate + f);

        if(timeToGainAllCookies<=timeToGainAllCookies2)
        {
            totalTime += timeToGainAllCookies;
            return totalTime;
        }

        else
        {
            totalTime += timeToBuyAFirm;
            rate += f;
        }
    }
}

int main(int argc, const char *argv[])
{
	string inputFileName = "B-large.in";
	string outputFileName = "bigoutput.txt";
	freopen(inputFileName.c_str(), "r", stdin);
	freopen(outputFileName.c_str(), "w", stdout);

    int t, i, j;
    double c, f, x;

    cin>>t;

    for(i=1; i<=t; i++)
    {
        cin>>c>>f>>x;

        printf("Case #%d: %.7lf\n", i, calculateTime(c, f, x));
    }
}
