#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <list>
#include <map>
#include <algorithm>
#include <functional>
#include <string>
#include <math.h>

void solve();
int main()
{
	int t;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		printf("Case #%d: ", i + 1);
		solve();
		printf("\n");
	}
}

void solve()
{
	int r, c, w;
	scanf("%d %d %d", &r, &c, &w);
	int n = (ceil((float)c / w) + (w - 1));
	printf("%d", n);
}