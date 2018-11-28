#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <fstream>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	scanf("%d", &n);
	for (int i = 1; i<=n; i++)
	{
		int x;
		int ans = 0;
		char s [10000];
		int kol = 0;
		scanf("%d%s", &x, s);
		for (int j = 0; j<=x; j++)
		{
            if (kol < j)
			{
				ans += j - kol;
				kol += s[j]-'0' + (j - kol);
			}
			else
				kol += s[j] - '0';
		}
	printf("Case #%d: %d\n", i, ans);
	}
	return 0;
}
