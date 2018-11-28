#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int a[1024];
int n;

int check(int o)
{
	int ret = 0;
	for(int i = 0; i < n; i ++)
	{
		ret += (a[i] + o - 1) / o - 1;
	}
	return ret + o;

}

int solve()
{
	scanf("%d", &n);

	int i;
	for(i =0; i < n; i ++)
	{
		scanf("%d", &a[i]);
	}

	int res = 1024;

	for(i = 1; i <=1024; i++)
	{
		res = min (res, check(i));
	}

	return res;
}
int main ()
{

	int t; 
	scanf ("%d", &t);

	for(int i = 1; i <= t; i++)
	{
		printf("Case #%d: %d\n", i, solve());
	}

	return 0;
}