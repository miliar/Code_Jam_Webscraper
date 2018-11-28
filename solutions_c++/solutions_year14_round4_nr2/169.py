#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <bitset>
#include <string>
#define PQ priority_queue
#define OO 2147483647
#define Max(a, b) ((FASTBUFFER = ((a) - (b)) >> 31), ((b) & FASTBUFFER | (a) & ~FASTBUFFER))
#define Min(a, b) ((FASTBUFFER = ((a) - (b)) >> 31), ((a) & FASTBUFFER | (b) & ~FASTBUFFER))
#define Swap(a, b) (a ^= b, b ^= a, a ^= b)

int FASTBUFFER;

using namespace std;

int test, n, i, j, tt, ans;
pair <int, int> a[1005];
int f[1005][1005], s1[1005], s2[1005];

int main()
{
	freopen("B-large.in", "r", stdin); freopen("output.txt", "w", stdout);
	scanf("%d", &test);
	while (test--)
	{
		scanf("%d", &n);
		for (i = 1; i <= n; i++)
			scanf("%d", &a[i].first), a[i].second = i;
		sort(a + 1, a + n + 1);
		for (i = 1; i <= n; i++)
		{
			s1[i] = s2[i] = 0;
			for (j = i + 1; j <= n; j++)
				if (a[j].second > a[i].second)
					s1[i]++;
				else
					s2[i]++;
		}
		
		f[0][0] = 0;
		for (i = 1; i <= n; i++)
			for (j = 0; j <= i; j++)
			{
				if (j == 0)
					f[i][j] = f[i - 1][j] + s1[i];
				if (j == i)
					f[i][j] = f[i - 1][j - 1] + s2[i];
				if (j != 0 && j != i)
					f[i][j] = min(f[i - 1][j] + s1[i], f[i - 1][j - 1] + s2[i]);
			}
		
		ans = f[n][0];
		for (i = 1; i <= n; i++)
			ans = min(ans, f[n][i]);
		printf("Case #%d: %d\n", ++tt, ans);
	}
	
	return 0;
}
