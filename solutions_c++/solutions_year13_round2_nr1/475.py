#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <cassert>

#define LL long long

using namespace std;

const int maxn = 105;

int a[maxn];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; test++)
	{
		int A, n, q;
		scanf("%d%d", &A, &n);
		for (q = 1; q <= n; q++)
			scanf("%d", &a[q]);
		sort(a + 1, a + n + 1);
		int done = 0;
		while((done < n) && (a[done + 1] < A))
		{
			A += a[done + 1];
			done++;
		}
		int best = n - done;
		if (A != 1)
		{
			int pl = 0; 
			while(done < n)
			{
				pl++;
				A += (A - 1);
				while((done < n) && (a[done + 1] < A))
				{
					A += a[done + 1];
					done++;
				}
				best = min(best, pl + (n - done));
			}
		}
		printf("Case #%d: %d\n", test, best);
	}
}