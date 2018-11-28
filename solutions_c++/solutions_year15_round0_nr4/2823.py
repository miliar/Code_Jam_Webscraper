#include <stdio.h>

FILE *out = fopen("output.txt", "w");
int t;
int x;
int r;
int c;
int flag = 0;
void input();
void process();

int main(void)
{
	input();
	return 0;
}

void input()
{
	int k;
	int i;
	char temp[10001];
	scanf("%d", &t);
	for (k = 1; k <= t; k++) {
		flag = 0;
		x = 0;
		r = 0;
		c = 0;
		scanf("%d %d %d", &x, &r, &c);
		process();
		if (flag == 1)
			fprintf(out,"Case #%d: GABRIEL\n", k);
		else
			fprintf(out,"Case #%d: RICHARD\n", k);
	}
}

void process()
{
	int i;
	if (x == 1)
	{
		flag = 1;
	} 
	else if (x == 2)
	{
		if ((r * c) % 2 == 0)
		{
			flag = 1;
		}
	}
	else if (x == 3)
	{
		if (r == 3)
		{
			if (c >= 2)
			{
				flag = 1;
			}
		}
		else if (c == 3) {
			if (r >= 2)
			{
				flag = 1;
			}
		}
	}
	else if (x == 4)
	{
		if (r == 4)
		{
			if (c >= 3)
			{
				flag = 1;
			}
		}
		else if (c == 4) {
			if (r >= 3)
			{
				flag = 1;
			}
		}
	}
}