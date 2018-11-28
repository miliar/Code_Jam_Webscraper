#include <iostream>
#include <cstdio>
using namespace std;

int n, m, b[20];

void solve()
{
	memset(b, 0, sizeof(b));
	scanf("%d", &n);
	for (int i = 1; i <= 4; ++i)
		for (int j = 0; j < 4; ++j)
		{
			int k;
			scanf("%d", &k);
			if (i == n)
				++b[k];
		}
	scanf("%d", &n);
	for (int i = 1; i <= 4; ++i)
		for (int j = 0; j < 4; ++j)
		{
			int k;
			scanf("%d", &k);
			if (i == n)
				++b[k];
		}
	int ans = 0;
	for (int i = 1; i <= 16; ++i)
		if (b[i] > 1)
			if (ans == 0)
				ans = i;
			else
			{
				printf("Bad magician!\n");
				return;
			}
	if (ans == 0)
		printf("Volunteer cheated!\n");
	else
		printf("%d\n", ans);
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int times;
	scanf("%d", &times);
	for (int i = 1; i <= times; ++i)
	{
		printf("Case #%d: ", i);
		solve();
	}
}
