#include <stdio.h>
#include <string.h>
#include <math.h>
#include <cstdio>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <algorithm>
#include <time.h>
using namespace std;


int main ()
{
	int t;

	freopen ("B-small.in", "r", stdin);
	freopen ("B-small.out", "w", stdout);

	scanf ("%d", &t);

	for (int cc=1;cc<=t;cc++)
	{
		printf ("Case #%d: ", cc);

		double x, f, c;

		cin >> c >> f >> x;

		double ret = x;
		double sum = 0;

		for (int i=1;i<=x;i++)
		{
			double rate = ((double)(2)+(double)(i-1)*f);
			double time = sum + c/rate;
			ret = min (ret, min (time + x/(rate+f), sum + x/rate));
			sum = time;
		}
		printf ("%.7lf\n", ret);
	}

	return 0;
}
