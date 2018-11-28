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

long long a, b, k;
long long dp[50][2][2][2];

long long sol (int ind, int pa, int pb, int pk)
{
	if (ind == -1)
	{
		if (!pk || !pa || !pb)
			return 0LL;
		return 1LL;
	}

	if (dp[ind][pa][pb][pk] != -1)
		return dp[ind][pa][pb][pk];

	long long ret = 0LL;

	if (pk || (((1LL<<ind) & k)!=0))
	{
		if ((pa || (((1LL<<ind) & a)!=0)) && (pb || (((1LL<<ind) & b)!=0)))
			ret += sol (ind-1, pa, pb, pk);
	}

	int npa=pa, npb=pb, npk=pk;

	if (((1LL<<ind)&k) != 0)
		npk = 1;
	if (((1LL<<ind)&a) != 0)
		npa = 1;
	if (((1LL<<ind)&b) != 0)
		npb = 1;

	ret += sol (ind-1, npa, npb, npk);

	if (pa || (((1LL<<ind) & a)!=0))
		ret += sol (ind-1, pa, npb, npk);
	if (pb || (((1LL<<ind) & b)!=0))
		ret += sol (ind-1, npa, pb, npk);
	return dp[ind][pa][pb][pk] = ret;
}

int main ()
{
	int t;

	freopen ("B-small.in", "r", stdin);
	freopen ("B-small.out", "w", stdout);
	cin >> t;

	for (int c=1;c<=t;c++)
	{
		printf ("Case #%d: ", c);

		cin >> a >> b >> k;

		memset (dp, -1, sizeof(dp));

		long long ret = sol (30, 0, 0, 0);

		cout << ret << endl;
	}
	return 0;
}



