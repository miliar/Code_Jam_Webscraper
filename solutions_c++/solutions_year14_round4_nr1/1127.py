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
	freopen ("A-small.in", "r", stdin);
	freopen ("A-small.out", "w", stdout);

	int t;

	scanf ("%d", &t);
	
	for (int tc = 1; tc <= t; tc++)
	{
		int n, x;
		cin >> n >> x;
		int arr[n+5];
		for (int i=0;i<n;i++)
			cin >> arr[i];
		sort (arr, arr+n);

		int s, e;
		s = 0, e = n-1;

		int ret = 0;

		while (s<e)
		{
			if (arr[e]+arr[s] <= x)
			{
				e--;
				s++;
				ret++;
			}
			else
			{
				ret ++;
				e--;
			}
		}

		if (e == s)
			ret ++;

		printf ("Case #%d: %d\n", tc, ret);

	}

	return 0;
}



