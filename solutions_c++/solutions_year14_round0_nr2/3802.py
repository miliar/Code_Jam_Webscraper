#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <math.h>
#include <memory.h>


using namespace std;

int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		double C, F, X;
		scanf("%lf%lf%lf", &C, &F, &X);
		double res = X / 2;
		double s = 0;
		for (int i = 0;  i <= 1000000; i++)
		{
			s += C / (F * i + 2);
			double r = s  + X / (F * (i+1) + 2);
			if (r < res)
				res = r;
		}
		printf("Case #%d: %.7lf\n", t+1, res);
	}

	return 0;
}