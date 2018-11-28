#include<stdio.h>
#include<string.h>

int main(void)	{
	int test, T;
	int i, k, len;
	char str[1005];

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d", &T);

	for (test = 1; test <= T; test++)	{
		char ans[1005] = { 0 };

		scanf("%s", str);

		len = strlen(str);

		ans[0] = str[0];
		for (i = 1; i < len; i++)	{
			if (ans[0] <= str[i])	{
				for (k = i; k > 0; k--)
					ans[k] = ans[k - 1];
				ans[0] = str[i];
			}
			else
				ans[i] = str[i];
		}

		printf("Case #%d: %s\n", test, ans);
	}

	return 0;
}