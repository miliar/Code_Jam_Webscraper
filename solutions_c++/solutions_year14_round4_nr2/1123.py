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

int n;
int arr[15];
int pos[15];
int b;

int calc ()
{
	int sarr[15];
	int tarr[15];
	int tpos[15];
	for (int i=0;i<n;i++)
	{
		tpos[i] = pos[i];
		tarr[i] = sarr[i] = arr[i];
	}

	sort (sarr, sarr+n);

	int ret = 0;
	int lc, rc;
	lc = rc = 0;

	for (int i=0;i<n;i++)
	{
		int ind;
		for (int j=0;j<n;j++)
			if (tarr[j] == sarr[i])
			{
				ind = j;
				break;
			}
		if (!tpos[ind])
		{
			for (int j=ind-1;j>=lc;j--, ret++)
			{
				swap(tpos[j], tpos[j+1]);
				swap(tarr[j], tarr[j+1]);
			}
			lc++;
		}
		else
		{
			for (int j=ind+1;j<n-rc;j++, ret++)
			{
				swap(tpos[j], tpos[j-1]);
				swap(tarr[j], tarr[j-1]);
			}
			rc++;
		}
	/*	if (b == 938)
		{
			for (int j=0;j<n;j++)
				cout << tarr[j] << " ";
			cout << ret << endl;
		}*/
	}
	//if (b == 938)
	//	cout << ret << endl;
	return ret;
}

int sol (int ind)
{
	if (ind == n)
		return calc();
	pos[ind] = 0;
	int ret = sol (ind+1);
//	b += (1<<ind);
	pos[ind] = 1;
	ret = min (ret, sol (ind+1));
//	b -= (1<<ind);
	return ret;
}

int main ()
{
	freopen ("B-small.in", "r", stdin);
	freopen ("B-small.out", "w", stdout);

	int t;

	scanf ("%d", &t);
	
	for (int tc = 1; tc <= t; tc++)
	{
		cin >> n;
		for (int i=0;i<n;i++)
			cin >> arr[i];

		printf ("Case #%d: %d\n", tc, sol(0));
	}

	return 0;
}



