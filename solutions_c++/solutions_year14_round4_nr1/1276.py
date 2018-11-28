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

const int maxN = 10100;

int n, c;
int ar[maxN];
bool used[maxN];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int q;
	scanf("%d", &q);
	for (int t = 0; t < q; t++)
	{
		scanf("%d%d", &n, &c);
		for (int i = 0; i < n; i++)
		{
			used[i] = false;
			scanf("%d", &ar[i]);
		}
		sort(ar, ar + n);
		int ans = 0;
		for (int i = n - 1; i >= 0; i--)
		{
			if (used[i])
			{
				continue;
			}
			for (int j = i - 1; j >= 0; j--)
			{
				if (ar[j] + ar[i] <= c && !used[j])
				{
					used[i] = used[j] = true;
					break;
				}
			}
			used[i] = true;
			ans++;
		}
		printf("Case #%d: %d\n", t + 1, ans);
	}
	return 0;
}