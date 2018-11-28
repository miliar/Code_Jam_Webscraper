
#include <algorithm>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <sstream>
#include <vector>

#include <stdio.h>
#include <string.h>

using namespace std;

double simulation(double C, double F, double X)
{
    double run_time = 0;
    double rate = 2.0;
    double cookies = 0.0;
    double fin_interval, buy_interval;
    while (cookies < X)
    {
        fin_interval = (X - cookies) / rate;
        buy_interval = (C - cookies) / rate;
        if (fin_interval < buy_interval)
            return run_time + fin_interval;
        cookies = C;
        run_time += buy_interval;
        if ((X - C)/rate > X/(rate + F))
        {
            cookies = 0;
            rate += F;
        }
        else
        {
            run_time += (X - cookies)/ rate;
            cookies = X;
        }
    }
    return run_time;
}

int main()
{
    int i, T;
    double C, F, X;
    
    cin >> T;
    for (i = 1; i <= T; i++)
    {
        cin >> C >> F >> X;
        fprintf(stdout, "Case #%d: %.7f\n", i, simulation(C, F, X));
    }
}

