#pragma warning(disable:4996)
#include<stdio.h>

int testcase;
int x, r, c, res;

void input()
{
	scanf("%d\n", &testcase);
	for (int i = 1; i <= testcase; i++)
	{
		scanf("%d %d %d", &x, &r, &c);
		if (x == 1) res = 1;
		else if (x == 2) res = (r*c) % 2 + 1;
		else if (x == 3)
		{
			if ((r*c) % 6 == 0 || (r == 3 && c == 3)) res = 1;
			else res = 2;
		}
		else
		{
			if ((r == 3 && c == 4) || (r == 4 && c == 4) || (r == 4 && c == 3)) res = 1;
			else res = 2;
		}

		if (res == 1) printf("Case #%d: GABRIEL\n", i);
		else printf("Case #%d: RICHARD\n", i);
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	input();
	return 0;
}