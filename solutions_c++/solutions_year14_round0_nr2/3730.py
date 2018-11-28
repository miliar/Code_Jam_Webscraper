#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	freopen("B-small-attempt0.in.txt", "r", stdin);
	freopen("ou.txt", "w", stdout);		 
	int T; scanf("%d", &T);
	for (int ii=0; ii<T; ii++)
	{
		double c, f, x; 
		scanf("%lf %lf %lf", &c, &f, &x);
		
		
		double cost = 0;
		double pv = 2;
		double fins = x / pv;
		
		while (true)
		{
			double t1 = c / pv;
			double p1 = pv + f;
			if (cost + t1 + x / p1 < fins)
			{
				fins = cost + t1 + x / p1;
				cost += t1;
				pv = p1;
			}
			else
			{
				printf("Case #%d: %.7lf\n", ii+1, fins);
				break;
			}
		}
	}
}