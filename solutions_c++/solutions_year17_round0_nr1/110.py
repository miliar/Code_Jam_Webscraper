#include <stdio.h>
#include <iostream>
#include <string>

void solve()
{
	std::string str;
	int K;

	std::cin >> str >> K;

	int count = 0;

	for (int i = 0; i < str.size(); i++)
	{
		if (str[i] == '+')
			continue;

		for (int j = i; j < i + K; j++)
		{
			if (j >= str.size())
			{
				printf("IMPOSSIBLE\n");
				return;
			}

			if (str[j] == '-')
				str[j] = '+';
			else
				str[j] = '-';
		}
		count++;
	}

	printf("%d\n", count);
}

int main()
{
	int T;
	scanf("%d", &T);

	for (int i = 1; i <= T; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}