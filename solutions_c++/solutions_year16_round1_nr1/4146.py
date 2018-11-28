#include <stdio.h>
#include <string.h>

#define N 1000

void process(int c)
{
	char inp[N + 10];
	scanf("%s", &inp);
	int n = strlen(inp);
	char ans[N * 2 + 10];
	int st = N, ed = N;

	ans[st] = inp[0];

	for (int i = 1; i < n; i++)
	{
		if (ans[st] <= inp[i])
			ans[--st] = inp[i];
		else
			ans[++ed] = inp[i];
	}

	printf("Case #%d: ", c);
	for (int i = st; i <= ed; i++)
		printf("%c", ans[i]);
	printf("\n");
}

int main()
{
	int c;
	scanf("%d", &c);
	for (int i = 1; i <= c; i++)
	{
		process(i);
	}
}