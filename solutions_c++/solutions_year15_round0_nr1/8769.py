#include <stdio.h>

int main(void)
{
	int t, testcase;
	int i;
	int max, count, op;
	char input[10000];

	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d", &testcase);
	for (t=1; t<=testcase; t++)
	{
		scanf("%d %s", &max, input);
		count = 0; op = 0;
		for (i=0; i<=max; i++)
		{
			if (count < i)
			{
				op += i - count;
				count += i - count;
			}
			count += input[i] - '0';
		}

		printf("Case #%d: %d\n", t, op);
	}

	return 0;
}