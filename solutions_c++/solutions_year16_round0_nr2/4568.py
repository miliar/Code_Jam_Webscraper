#include<stdio.h>
#include<string.h>

int main(void)	{
	int test, T;
	int i, k, len;
	char str[105];

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d", &T);

	for (test = 1; test <= T; test++)	{
		scanf("%s", str);

		len = strlen(str);
		k = 0;
		while (1)	{
			for (i = 1; i < len; i++)	{
				if (str[i] != str[i - 1])
					break;
			}

			if (i == len)	{
				if (str[0] == '-')
					k++;

				break;
			}

			for (i--; i >= 0; i--)	{
				if (str[i] == '+')
					str[i] = '-';
				else
					str[i] = '+';
			}

			k++;
		}

		printf("Case #%d: %d\n", test, k);
	}

	return 0;
}