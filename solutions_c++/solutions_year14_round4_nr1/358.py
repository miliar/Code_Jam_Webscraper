#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <map>
#include <vector>
using namespace std;

int arr[10010], visit[10010];

int main()
{
	int i, j, n, sz, ret;
	int t, cas;
	scanf("%d", &t);
	for (cas = 1; cas <= t; cas++)
	{
		scanf("%d%d", &n, &sz);
		for (i = 0; i < n; i++)
			scanf("%d", &arr[i]);
		memset(visit, 0, sizeof visit);
		sort(arr, arr + n);
		for (i = n - 1, ret = 0; i >= 0; i--)
		{
			if (visit[i]) continue;
			visit[i] = 1;
			ret++;
			for (j = i - 1; j >= 0; j--)
			{
				if (visit[j]) continue;
				if (arr[i] + arr[j] <= sz)
				{
					visit[j] = 1;
					break;
				}
			}
		}
		printf("Case #%d: %d\n", cas, ret);
	}

	return 0;
}
