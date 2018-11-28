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
	int arr[2][5][5];
	int ans[2];
	int t;

	freopen ("D-small.in", "r", stdin);
	freopen ("D-small.out", "w", stdout);

	scanf ("%d", &t);

	for (int c=1;c<=t;c++)
	{
		printf ("Case #%d: ", c);
		int ret, res;

		vector <double> v, k;
		int n;

		cin >> n;

		for (int i=0;i<n;i++)
		{
			double d;
			cin >> d;
			v.push_back(d);
		}

		for (int i=0;i<n;i++)
		{
			double d;
			cin >> d;
			k.push_back(d);
		}

		sort (v.begin(), v.end());
		sort (k.begin(), k.end());

		int cur = n-1;
		ret = res = 0;
		for (int i=n-1;i>=0&&cur>=0;i--)
		{
			if (k[i] > v[cur])
				continue;
			cur--;
			ret++;
		}

		int ks, ke, vs, ve;
		ks = vs = 0;
		ke = ve = n-1;

		while (ks <= ke)
		{
			if (v[ve] > k[ke])
			{
				res ++;
				ks ++;
				ve--;
			}
			else
			{
				ve--;
				ke--;
			}
		}
		cout << ret << " " << res << endl;
	}

	return 0;
}
