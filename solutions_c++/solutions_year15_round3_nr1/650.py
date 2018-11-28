#include <stdio.h>
#include <algorithm>
#include <memory.h>
using namespace std;
int a,b,c, i, t;


int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("small_out.out", "w", stdout);
	scanf("%d", &t);
	for (i = 1; i <= t; i++)
	{
		scanf("%d%d%d", &a, &b, &c);
		printf("Case #%d: %d\n", i, a*((b + c - 1) / c) + c - 1);
	}
	return 0;
}