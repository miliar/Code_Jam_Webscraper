#pragma warning(disable:4996)
#include<stdio.h>
#include<string.h>
#define MAX 1106

int testcase, l;
int n, now, res;
char data[MAX];

void process()
{
	int i = 1;
	
	n = now = res = 0;
	do{ n = n * 10 + data[i++] - '0'; } while (data[i] >= '0' && data[i] <= '9');
	for (int j = 0; j <= n; j++)
	{
		if (now >= j) now = now + data[j + i + 1] - '0';
		else
		{
			res = res + (j - now);
			now = j + data[j + i + 1] - '0';
		}
	}
}

void output(int k)
{
	printf("Case #%d: %d\n", k, res);
}

void input()
{
	scanf("%d\n", &testcase);
	for (int i = 1; i <= testcase; i++)
	{
		gets(data + 1);
		l = strlen(data + 1);
		process();
		output(i);
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	input();
	return 0;
}