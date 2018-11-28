/*
    Title:
    Author: RudySnow
    Algorithm:
    Date:
    License: GNU GPL
    Quote: Night Gathers, and My Watch Begins, it shall Never End until My Death
*/

#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <memory.h>
#include <cstring>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <set>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>

using namespace std;

int t;
double c, f, x;
const double eps = 1e-6;

void Solve(int num)
{
    double totalTime = 0.0;
    double productive = 2.0;
    while(true)
    {
        double timeDirect = x / productive;
        double timeThroughFarm = c / productive +  x / (productive + f);
        if(timeDirect <= timeThroughFarm)
        {
            totalTime += timeDirect;
            break;
        }
        else
        {
            totalTime += c / productive;
            productive += f;
        }
    }

    cout << "Case #" << num << ": ";
    printf("%.7lf\n", totalTime);
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-1.out", "w", stdout);
    cin >> t;
    int tFirst = t;
    while(t--)
    {
        cin >> c >> f >> x;
        Solve(tFirst - t);
    }
    return 0;
}
