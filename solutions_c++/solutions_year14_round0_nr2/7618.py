#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <iterator>
#include <algorithm>

using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t;
	int icase = 1;
	scanf("%d", &t);
	while( t-- )
	{
		double c, f, x;
		scanf("%lf%lf%lf", &c, &f, &x);
		double speed = 2.0;
		double ans = 0;
		bool flag = true;
		while ( flag )
		{
			double time1 = c / speed;
			double time2 = x / (speed + f);
			double time3 = x / speed;
			if( time1 + time2 < time3 )
			{
				ans += time1;
				speed += f;
			}
			else
			{
				ans += time3;
				flag = false;
			}
		}
		printf("Case #%d: %.7lf\n",icase++, ans); 
	}
	return 0;
}