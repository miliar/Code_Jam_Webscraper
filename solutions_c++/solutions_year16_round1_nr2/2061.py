#include <cstdio>
#include <memory.h>
#include <algorithm>
using namespace std;

int main()
{
	int T, N, temp, i, j, maxSize, count = 0;
	bool table[2510];
	int ans[100], sizeOfAns;

	scanf("%d", &T);

	while (T--)
	{
		scanf("%d", &N);
		memset(table, 0, sizeof(table));
		for (i = 0, maxSize = (N << 1) - 1; i < maxSize; ++i)
		{
			for (j = 0; j < N; ++j)
			{
				scanf("%d", &temp);
				table[temp] = !table[temp];
			}
		}

		for (i = 1, sizeOfAns = 0; i <= 2500; ++i)
		{
			if (table[i])
			{
				ans[sizeOfAns++] = i;
			}
		}
		sort(ans, ans + sizeOfAns);

		printf("Case #%d:", ++count);
		for (i = 0; i < sizeOfAns; ++i)
		{
			printf(" %d", ans[i]);
		}
		putchar('\n');
	}
	return 0;
}