#include <stdio.h>
#include <vector>
#include <string>
#include <stack>
#include <map>
#include <iostream>
using namespace std;

int main()
{
	//freopen("B-large.in", "r", stdin);
	//freopen("B-large.out", "w", stdout);


	int nCase;
	double C, F, X;
	int t, i;
	scanf("%d", &nCase);
	for (t = 1; t <= nCase; ++ t)
	{
		scanf("%lf%lf%lf", &C, &F, &X);
		double starttime = 0;
		double curv = 2;
		double anstime = X;
		double curtime;
		while (true)
		{
			curtime = X / curv + starttime;
			if (curtime < anstime)
			{
				anstime = curtime;
			}
			starttime += C/curv;
			if (starttime >= anstime)
			{
				break;
			}
			curv += F;
		}
		
		printf("Case #%d: %.7lf", t, anstime);
		
		if (t < nCase)
		{
			printf("\n");
		}
	}

	//system("pause");
	return 0;
}

