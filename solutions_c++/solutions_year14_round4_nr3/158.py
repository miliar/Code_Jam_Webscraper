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

int test, w, h, n, i, j, tt, ans, sel, a[1005][5], b[1005][5];
int dis[1005];

int Dis(int a1, int a2)
{
	if (min(a[a1][1], a[a2][1]) >= max(a[a1][0], a[a2][0]))
		return max(b[a1][0], b[a2][0]) - min(b[a1][1], b[a2][1]) - 1;
	if (min(b[a1][1], b[a2][1]) >= max(b[a1][0], b[a2][0]))
		return max(a[a1][0], a[a2][0]) - min(a[a1][1], a[a2][1]) - 1;
	return max(max(a[a1][0], a[a2][0]) - min(a[a1][1], a[a2][1]), max(b[a1][0], b[a2][0]) - min(b[a1][1], b[a2][1])) - 1;
}

int main()
{
	freopen("C-large.in", "r", stdin); freopen("output.txt", "w", stdout);
	scanf("%d", &test);
	while (test--)
	{
		scanf("%d %d %d", &w, &h, &n);
		for (i = 1; i <= n; i++)
			scanf("%d %d %d %d", &a[i][0], &b[i][0], &a[i][1], &b[i][1]);
		for (i = 1; i <= n; i++)
			dis[i] = a[i][0];
		ans = w;
		for (i = 1; i <= n; i++)
		{
			sel = 1;
			for (j = 1; j <= n; j++)
				if (dis[j] < dis[sel])
					sel = j;
			ans = min(ans, dis[sel] + w - a[sel][1] - 1);
			for (j = 1; j <= n; j++)
			{
				if (dis[j] == OO || sel == j)
					continue;
				int now = Dis(sel, j);
				if (dis[sel] + now < dis[j])
					dis[j] = dis[sel] + now;
			}
			
			dis[sel] = OO;
		}
		
		printf("Case #%d: %d\n", ++tt, ans);
	}
	
	return 0;
}
