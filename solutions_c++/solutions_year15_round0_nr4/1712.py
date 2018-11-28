#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <list>
#include <map>
#include <algorithm>
#include <functional>
#include <string>

int R[4][4][4] = {
	1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0,
	1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0,
	1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1,
	1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1
};
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
	int x, r, c;
	scanf("%d %d %d", &x, &r, &c);
	if (R[r-1][c-1][x-1])
	{
		printf("GABRIEL");
	}
	else
	{
		printf("RICHARD");
	}
}