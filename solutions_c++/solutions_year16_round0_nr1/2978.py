#include <cstdio>
#include <memory.h>

bool judge(bool* table)
{
	for (int i = 0; i < 10; ++i)
	{
		if (table[i] == 0) return false;
	}
	return true;
}

int main()
{
	int T, n, count = 0, N, temp;
	bool table[10];
	scanf("%d", &T);
	while (T--)
	{
		memset(table, 0, sizeof(table));
		scanf("%d", &N);
		if (N == 0) printf("Case #%d: INSOMNIA\n", ++count);
		else
		{
			for (n = 1; !judge(table); ++n)
			{
				temp = n*N;
				while (temp)
				{
					table[temp % 10] = true;
					temp /= 10;
				}
			}
			--n;
			printf("Case #%d: %d\n", ++count, n*N);
		}
	}
	return 0;
}