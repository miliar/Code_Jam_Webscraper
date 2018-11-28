#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
using namespace std;

const int N = 200200;
int n;
char s[N];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		scanf("%s", &s);
		n = strlen(s);
		int x = -1;
		int sz = 0;
		int ans = n / 2;
		for (int j = 0; j < n; j++)
		{
			int y = (s[j] == 'C' ? 0 : 1);
			if (x == -1)
			{
				x = y;
				sz++;
				continue;
			}
			if (x == y)
			{
				ans++;
				x ^= 1;
				sz--;
				if (sz == 0) x = -1;
			}
			else
			{
				x ^= 1;
				sz++;
			}
		}
		printf("Case #%d: %d\n", i, ans * 5);
	}

	return 0;
}