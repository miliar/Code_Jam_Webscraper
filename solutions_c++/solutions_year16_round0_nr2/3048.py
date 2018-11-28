#include <cstdio>
#include <cstring>
#include <memory.h>

int main()
{
	int T, count = 0, num, ans;
	bool table[110];
	char c;
	scanf("%d", &T);
	getchar();
	while (T--)
	{
		num = 0;
		while ((c = getchar()) != '\n')
		{
			table[num++] = (c == '+');
		}
		ans = 0;
		for (int i = num - 1; i >= 0; --i)
		{
			if (table[i] == false)
			{
				for (int j = 0; j <= i; ++j) table[j] = !table[j];
				++ans;
			}
		}
		printf("Case #%d: %d\n", ++count, ans);

	}
	return 0;
}
