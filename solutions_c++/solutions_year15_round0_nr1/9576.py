#include <cstdio>

void solution()
{
	int n;
	int friends = 0, acc = 0;
	scanf("%d ", &n);
	for (int s = 0; s <= n; s++)
	{
		if (acc < s)
		{
			friends += s - acc;
			acc = s;
		}
		acc += getchar() - '0';
	}
	getchar();
	printf("%d\n", friends);
}

int main()
{
	int testCases;
	scanf("%d\n", &testCases);
	for (int i = 1; i<= testCases; i++)
	{
		printf("Case #%d: ", i);
		solution();
	}
	return 0;
}
