#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;

int n;
int dp[1024][1024];
int a[1024];
int b[1024];
int before[1024], after[1024];

int rec(int left, int side1)
{
	if(dp[left][side1] != -1)
		return dp[left][side1];
	if(left == 0)
		return dp[left][side1] = 0;

	int ret = 0;
	int next = n - left;

	ret = min(
				rec(left - 1, side1 + 1) + before[next], 
				rec(left - 1, side1) + after[next]);

	return dp[left][side1] = ret;
}

void solve()
{
	scanf ("%d", &n);
	int i, j; 
	for(i = 0; i < n; i++)
	{
		scanf ("%d", &a[i]);
		b[i] = a[i];
	}

	sort(b, b + n);
	memset (before, 0 , sizeof(before));
	memset (after, 0, sizeof (after));
	memset (dp, -1, sizeof(dp));

	for(i = 0; i < n; i ++)
	{
		a[i] = lower_bound(b, b+n, a[i]) - b;
	}

	for(i = 0; i < n; i ++)
	{
		for(j = 0; j < n; j ++)
		{
			if(a[j] > a[i])
			{
				if(j > i)
					after[a[i]] ++;
				else
					before[a[i]] ++;
			}
		}
	}

	printf ( "%d\n", rec(n, 0) );
	
}

int main ()
{

	int tt;
	scanf ("%d", &tt);

	int i;
	for(i = 0; i < tt; i ++)
	{
		printf ("Case #%d: ", i+1);
		solve();
	}

	return 0;
}