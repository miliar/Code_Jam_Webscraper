#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <map>
#include <queue>
#include <stack>
#include <iostream>
using namespace std;

int main ()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int re, ca = 1;
	double c, f, x, time, time1, time2;
	double ff;
	scanf("%d",&re);
	while(re--)
	{
		scanf("%lf%lf%lf",&c,&f,&x);

		time = 0;
		ff = 2;

		do{
			time2 = x / ff;
			time1 = (c / ff) + x / (ff + f);
			if(time1 < time2)
			{
				time += c / ff;
				ff += f;
			}
			else
			{
				time += time2;
				break;
			}
		}while(1);
		
		printf("Case #%d: %.7lf\n",ca++,time);
	}
	return 0;
}



