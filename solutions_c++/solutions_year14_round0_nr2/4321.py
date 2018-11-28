#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>

using namespace std;



int main()
{
    int n;
    double c, f, x, t, income;
    double timeWONewFarm, timeWNewFarm, timeToBuyFarm;

    scanf("%d", &n);
    for(int i = 1; i <= n; ++i)
    {
        t = 0.0;
        income = 2.0;

        scanf("%lf%lf%lf", &c, &f, &x);

        while(1)
        {
            timeWONewFarm = x / income;
            timeWNewFarm = (x / (income + f));
            timeToBuyFarm = (c / income);
            if(timeWONewFarm <= timeWNewFarm + timeToBuyFarm)
            {
                t += timeWONewFarm;
                break;
            }
            //advantageous to buy a farm
            t += timeToBuyFarm;
            income += f;
        }

        printf("Case #%d: %.7lf\n", i, t);
    }

    return 0;
}
