#include <vector>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int t;
    scanf("%d", &t);
    int id = 1;
    while (t--)
	{
        double farmCost, farmCookieRate, goal;
        double cookieRate = 2.0f;
        scanf("%lf %lf %lf", &farmCost, &farmCookieRate, &goal);
        
        int farmOwned = 0;
        int cookieOwned = 0;
        double time = 0.0f;
        
        bool stop = false;
        while( !stop )
        {        
            if( goal/cookieRate < ( farmCost/cookieRate + goal/(cookieRate+farmCookieRate) ) )
            {
                time += goal/cookieRate;
                stop = true;
                break;
            }
            
            time += farmCost/cookieRate;
            cookieRate += farmCookieRate;
        }
		
		printf("Case #%d: %.7f\n", id++, time);

	}
	return 0;
}
