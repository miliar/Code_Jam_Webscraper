#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char s[105];
void change(int n)
{
	int i, k;
	char aux;
	if (n % 2 == 0)
	{
		k = n / 2;
	}
	else
	{
		k = n / 2 + 1;
	}
	for (i = 0; i < k; i++)
	{
		aux = s[i];
		s[i] = s[n - i - 1];
		s[n - i - 1] = aux;
	}
	for (i = 0; i < n; i++)
	{
		if (s[i] == '+')
		{
			s[i] = '-';
		}
		else
		{
			s[i] = '+';
		}
	}
}
int main()
{
	FILE *f = fopen("fis.in", "r");
	FILE *g = fopen("fis.out", "w");
	int t, n, i, j, ind = 1, last;
	fscanf(f, "%d", &t);
	while (t--)
	{
		fprintf(g, "Case #%d: ", ind);
		int ans = 0;
		fscanf(f, "%s", &s);
		n = strlen(s);
		while (true)
		{
			last = -1;
			for (i = n - 1; i >= 0; i--)
			{
				if (s[i] == '-')
				{
					last = i;
					break;
				}
			}
			if (last == -1)
			{
				break;
			}
			if (s[0] == '-')
			{
				change(last + 1);
				ans = ans + 1;
			}
			else
			{
				for (i = 0; i < n; i++)
				{
					if (s[i] == '-')
					{
						break;
					}
				}
				change(i);
				change(last + 1);
				ans = ans + 2;
			}
		}
		fprintf(g, "%d\n", ans);
		ind++;
	}
}