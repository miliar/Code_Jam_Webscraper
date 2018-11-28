#include <cstdio>
#include <string>
#include <algorithm>
#include <cmath>
#include <vector>
#include <memory.h>
#include <set>
#include <map>
#include <stack>
#include <queue>

using namespace std;

int a[10005];

int main(void)
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int q = 1; q <= t; q++)
	{
		int n, v;
		scanf("%d%d", &n, &v);
		for (int i = 0; i < n; i++)
			scanf("%d", &a[i]);
		sort(a, a + n);
		int cnt = 0;
		int p1 = 0;
		int p2 = n - 1;
		while (p2 > p1)
		{
			cnt++;
			if (a[p1] + a[p2] <= v)
			{
				p2--;
				p1++;
			}
			else
				p2--;

		}
		if (p1 == p2)
			cnt++;
		printf("Case #%d: %d\n", q, cnt);
	}
	return 0;
}