#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <algorithm>
using namespace std;
const int MAXN = 1000;
struct sd
{
	int index, value;
} d[MAXN];
bool compare(sd a, sd b)
{
	return a.value <= b.value;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, i, n, j, c;
	scanf("%d", &t);
	for (i = 1; i <= t; i++)
	{
		scanf("%d", &n);
		for (j = 0; j < n; j++)
		{
			scanf("%d", &d[j].value);
			d[j].index = j;
		}
		sort(d, d + n, compare);
		int res = 0, l = 0, r = n - 1;
		for (j = 0; j < n; j++)
		if (d[j].index - l <= r - d[j].index)
		{
			res += d[j].index - l;
			l++;
			for (int k = j + 1; k < n; k++)
			if (d[k].index < d[j].index)
				d[k].index++;
		}
		else
		{
			res += r - d[j].index;
			r--;
			for (int k = j + 1; k < n; k++)
			if (d[k].index > d[j].index)
				d[k].index--;
		}
		printf("Case #%d: %d\n", i, res);
	}
	return 0;
}