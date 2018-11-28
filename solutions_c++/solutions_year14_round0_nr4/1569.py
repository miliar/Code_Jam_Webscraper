#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int cmp(double* a, double* b, int N)
{
	int i = 0, j = 0;
	int ans = 0;
	while(i < N && j < N)
	{
		if (a[i] > b[j])
		{
			ans++;
			i++;
			j++;
		}
		else
		{
			i++;
		}
	}
	return ans;
}

int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	double a[2000];
	double b[2000];
	for (int nt = 1; nt <= T; ++nt)
	{
		int N;
		scanf("%d", &N);
		for (int i = 0; i < N; ++i)
			scanf("%lf", &a[i]);
		for (int i = 0; i < N; ++i)
			scanf("%lf", &b[i]);
		sort(a, a+N);
		sort(b, b+N);
		/*for (int i = 0; i < N; ++i)
			printf("%.3f ", a[i]);
		printf("\n");
		for (int i = 0; i < N; ++i)
			printf("%.3f ", b[i]);
			*/
		printf("Case #%d: %d %d\n", nt, cmp(a, b, N), N-cmp(b, a, N));
		
	}
	return 0;
}