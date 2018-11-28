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

int test, n, x, i, now, ans, tt, a[10005];

int main()
{
	freopen("A-large.in", "r", stdin); freopen("output.txt", "w", stdout);
	scanf("%d", &test);
	while (test--)
	{
		scanf("%d %d", &n, &x);
		for (i = 1; i <= n; i++)
			scanf("%d", &a[i]);
		sort(a + 1, a + n + 1);
		now = n, ans = 0;
		for (i = 1; i <= n; i++)
		{
			while (now > i && a[now] + a[i] > x)
				now--, ans++;
			if (now >= i)
			{
				ans++;
				now--;
			}
			
			else
				break;
		}
		
		printf("Case #%d: %d\n", ++tt, ans);
	}
	
	return 0;
}
