#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>
#include <iostream>
#include <cstdlib>

using namespace std;

const int SZ = 1003;

int N;
double a[SZ], b[SZ];

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, T;
	int i, j, k;
	int r, d;
	scanf("%d", &T);
	for (t = 1; t <= T; t++)
	{
		scanf("%d", &N);
		for (i = 0; i < N; i++)
			scanf("%lf", &a[i]);
		for (i = 0; i < N; i++)
			scanf("%lf", &b[i]);
		sort(a, a + N);
		sort(b, b + N);
		r = 0;
		for (i = 0, j = 0; i < N && j < N; )
		{
			while (j < N && b[j] < a[i]) j++;
			if (j >= N) break;
			i++;
			j++;
		}
		r += N - i;
		d = 0;
		for (i = 0, j = N - 1, k = 0; i < N && j >= 0 && k < N; )
		{
			if (a[i] > b[k])
			{
				i++;
				k++;
				d++;
			}
			else if (a[i] < b[j])
			{
				i++;
				j--;
			}
			else
				break;
		}
		d += N - i;
		printf("Case #%d: %d %d\n", t, d, r);
	}
	
	return 0;
}