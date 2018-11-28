#include <cstdio>

void testCase()
{
	int s;
	char input[1024];
	scanf("%d%s", &s, input);
	int sum = 0;
	int answer = 0;
	for (int i = 0; i <= s; i++)
	{
		if (sum < i)
		{
			answer += i - sum;
			sum = i;
		}
		sum += input[i] - '0';
	}
	printf("%d", answer);
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		printf("Case #%d: ", i);
		testCase();
		printf("\n");
	}
	return 0;
}