#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

using namespace std;

int k, c, s;

void read()
{
	scanf("%d%d%d", &k, &c, &s);
}

void solve()
{
	for (int i = 1; i <= s; ++i)
	{
		printf("%d ", i);
	}
	printf("\n");
}

int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int test_case = 1; test_case <= t; ++test_case)
	{
		printf("Case #%d: ", test_case);
		read();
		solve();
	}
}