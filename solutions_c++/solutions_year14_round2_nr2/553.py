#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

int a, b, k;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int q;
	scanf("%d", &q);
	for (int t = 0; t < q; t++)
	{
		printf("Case #%d: ", t + 1);
		scanf("%d%d%d", &a, &b, &k);
		int ans = 0;
		for (int i = 0; i < a; i++)
		{
			for (int j = 0; j < b; j++)
			{
				ans += ((i & j) < k);
			}
		}
		printf("%d\n", ans);
	}
	return 0;
}