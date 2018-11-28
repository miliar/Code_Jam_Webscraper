#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
using namespace std;
int n, x, a[10009];

int init()
{
	scanf("%d %d", &n, &x);
	for (int i = 0; i < n; i++)
		scanf("%d", &a[i]);
	return 0;
}

int work()
{
	int rtn = 0;
	sort(a, a + n);
	int k = n - 1;
	for (int i = 0; i <= k; i++)
	{
		while (i < k && a[i] + a[k] > x)
		{
			rtn++;
			k--;
		}
		rtn++;
		k--;
	}
	return rtn;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int test = 1; test <= T; ++test)
	{
		init();
		int ans = work();
		printf("Case #%d: %d\n", test, ans);
	}
	return 0;
}