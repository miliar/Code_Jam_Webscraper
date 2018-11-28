#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <map>
#include <set>
#include <assert.h>

using namespace std;

typedef long long ll;
#define mp make_pair
#define mt(a, b, c) mp(a, mp(b, c))

int tests;

const int N = 1010;

int n;
double a[N], b[N];
bool was[N];

int slow(int t)
{
	int r = n - 1;
	int res = 0;
	for (int i = 0; i < t; i++)
	{
		if (b[r] < a[i])
			res++;
		r--;
	}
	for (int i = n - 1; i >= t; i--)
	{
		if (b[r] < a[i])
			res++;
		r--;
	}
	return res;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &tests);
	for (int q = 0; q < tests; q++)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%lf", a + i);
		for (int i = 0; i < n; i++)
			scanf("%lf", b + i);
		sort(a, a + n);
		sort(b, b + n);
		pair<int, int> res = mp(0, 0);
		int dw = 0, w = 0;

		fill(was, was + n, 0);
		for (int i = 0; i < n; i++)
		{
			int ind = -1;
			for (int j = 0; j < n; j++)
			{
				if (was[j])
					continue;
				if (b[j] > a[i] && (ind == -1 || b[ind] > b[j]))
				{
					ind = j;
				}
			}
			was[ind] = 1;
			if (ind == -1)
				res.second++;
		}
		w = res.second;
		
		for (int i = 0; i < n; i++)
			dw = max(dw, slow(i));
		printf("Case #%d: %d %d\n", q + 1, dw, w);
	}
	return 0;
}