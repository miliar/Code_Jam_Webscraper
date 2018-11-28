#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <math.h>

using namespace std;

double R = 2.0;

double calc(double C, double F, double X, int p)
{
    double t = 0;
    double r = R;
    for (int i = 0; i < p; i++)
    {
        double ft = C / r;
        t += ft;
        r += F;
    }

    double dt = X / r;
    t += dt;
    return t;
}

void processCase(int n) 
{
    double C, F, X;
    cin >> C;
    cin >> F;
    cin >> X;
    double dp = (X * F / C - R) / F;
    int p = (int)dp;
    if (p < 0)
        p = 0;
    double t = calc(C, F, X, p);
    printf("Case #%d: %.7f\n", n, t);
}

            


int main(int argc, char **argv)
{
 
    int N = 0;
    cin >> N;
    for (int i = 0; i < N; i++)
        processCase(i + 1);

    return 0;
}