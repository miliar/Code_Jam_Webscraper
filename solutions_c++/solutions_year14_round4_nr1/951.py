#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

const int maxn = 10010;

int n, cap;
int dat[maxn];

int mincount()
{
	sort(dat, dat + n);
	int res = 0;
	int right = n - 1;
	int i;
	for (i = 0; i < right; i++)
	{
		while (i < right && dat[right] + dat[i] > cap)
		{
			right--;
			res++;
		}
		res++;
		right--;
	}
	
	if (i == right) res++;
	
	return res;
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		scanf("%d%d", &n, &cap);
		for (int j = 0; j < n; j++) scanf("%d", &dat[j]);
		printf("Case #%d: %d\n", i, mincount());
	}
	
	return 0;
}
