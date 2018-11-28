#include <stdio.h>
#include <stdlib.h>
char s[1000000];
char multiplication(char c1, char c2, int &semn)
{
	if (c1 == '1')
	{
		return c2;
	}
	if (c2 == '1')
	{
		return c1;
	}
	if (c1 == 'i' && c2 == 'i')
	{
		semn = 1 - semn;
		return '1';
	}
	if (c1 == 'i' && c2 == 'j')
	{
		return 'k';
	}
	if (c1 == 'i' && c2 == 'k')
	{
		semn = 1 - semn;
		return 'j';
	}
	if (c1 == 'j' && c2 == 'i')
	{
		semn = 1 - semn;
		return 'k';
	}
	if (c1 == 'j' && c2 == 'j')
	{
		semn = 1 - semn;
		return '1';
	}
	if (c1 == 'j' && c2 == 'k')
	{
		return 'i';
	}
	if (c1 == 'k' && c2 == 'i')
	{
		return 'j';
	}
	if (c1 == 'k' && c2 == 'j')
	{
		semn = 1 - semn;
		return 'i';
	}
	if (c1 == 'k' && c2 == 'k')
	{
		semn = 1 - semn;
		return '1';
	}
}
int main()
{
	FILE *f, *g;
	f = fopen("fis.in", "r");
	g = fopen("fis.out", "w");
	int T, ind, ok1, ok2, ok3, semn,ok;
	long long X, L, i, j, nr;
	char c1, c2, rez;
	fscanf(f, "%d", &T);
	for (ind = 1; ind <= T; ind++)
	{
		semn = 0;
		ok1 = ok2 = ok3 = 0;
		i = 0;
		fscanf(f, "%lld %lld", &L, &X);
		fscanf(f, "%s", &s);
		nr = 0;
		if (L*X >= 3 && L != 1)
		{
			c1 = s[0];
			i = 1;
			ok = 0;
			if (c1 == 'i')
			{
				ok = 1;
			}
			while (ok == 0)
			{
				c1 = multiplication(c1, s[i], semn);
				i++;
				if (i == L)
				{
					i = 0;
					nr++;
				}
				if (nr == X || (c1 == 'i' && semn == 0))
				{
					ok = 1;
				}
			}
			if (c1 == 'i' && semn==0)
			{
				ok1 = 1;
				c1 = s[i];
				i++;
				if (i == L)
				{
					i = 0;
					nr++;
				}
			}
			ok = 0;
			if (c1 == 'j' && semn == 0)
			{
				ok = 1;
			}
			semn = 0;
			while (ok == 0)
			{
				c1 = multiplication(c1, s[i], semn);
				i++;
				if (i == L)
				{
					i = 0;
					nr++;
				}
				if(nr == X || (c1 == 'j' && semn == 0))
				{
					ok = 1;
				}
			}
			if (c1 == 'j' && semn==0)
			{
				ok2 = 1;
				c1 = s[i];
				i++;
				if (i == L)
				{
					i = 0;
					nr++;
				}
			}
			ok = 0;
			semn = 0;
			while (nr < X)
			{
				c1 = multiplication(c1, s[i], semn);
				i++;
				if (i == L)
				{
					i = 0;
					nr++;
				}
			}
			if (c1 == 'k' && semn==0)
			{
				ok3 = 1;
			}
			if (ok1 == 1 && ok2 == 1 && ok3 == 1)
			{
				fprintf(g, "Case #%d: YES\n", ind);
			}
			else
			{
				fprintf(g, "Case #%d: NO\n", ind);
			}
		}
		else
		{
			fprintf(g, "Case #%d: NO\n", ind);
		}

	}
}