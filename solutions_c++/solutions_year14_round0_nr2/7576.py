#include <iostream>
#include <stdio.h>
using namespace std;

double solve(double c, double f, double x)
{
    double time = 0.0;
    double cps = 2.0;
    while (true)
    {
        if (x/cps < c/cps + x/(cps+f))
            return time + x / cps;
        time += c / cps;
        cps += f;
    }
}

int main()
{
    int tests;
    cin >> tests;
    for (int test=1;test<=tests;test++)
    {
        double c,f,x;
        cin >> c >> f >> x;
        printf("Case #%d: %.7lf\n",test,solve(c,f,x));
    }
}
