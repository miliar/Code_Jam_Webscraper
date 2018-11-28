#include <stdio.h>
#include <memory.h>
#include <string.h>

#define N 100

void process(int p)
{
	int n, ans = 0;
	char data[N + 10];
	scanf("%s", &data);
	n = strlen(data);
	for (int i = n - 1; i >= 0; i--)
	{
		if (data[i] == '-')
		{
			ans++;
			for (int j = i; j >= 0; j--)
				data[j] = (data[j] == '-') ? '+' : '-';
		}
	}
	printf("Case #%d: %d\n", p, ans);
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