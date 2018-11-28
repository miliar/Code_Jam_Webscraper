#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <algorithm>
using namespace std;
const int MAXN = 100000;
int d[MAXN];
bool used[MAXN];
/*int bin_search(int w, int l, int r)
{
	if (l == r)
	if (d[l] <= w )


}*/
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, i, n, x, j, c, temp;
	scanf("%d", &t);
	for (i = 1; i <= t; i++)
	{
		scanf("%d%d", &n, &x);
		c = 0;
		for (j = 0; j < n; j++)
		{
			scanf("%d", &d[j]);
			used[j] = false;
		}
		sort(d, d + n);
		for (j = 0; j < n - 1; j++)
		if (!used[j])
		{
			used[j] = true;
			int *temp = upper_bound(d + j + 1, d + n, x - d[j]) - 1;
			while (used[temp - d] && temp > d)
				temp--;
			if (temp > d)
				used[temp - d] = true;
			c++;
		}
		if (!used[n - 1])
			c++;
		printf("Case #%d: %d\n", i, c);
	}
	return 0;
}