#include <stdio.h>
#include <stdlib.h>
int main()
{
	FILE *f = fopen("fis.in", "r");
	FILE *g = fopen("fis.out", "w");
	int t, k, c, s, ind = 0, i;
	fscanf(f, "%d", &t);
	while (t--)
	{
		ind++;
		fprintf(g, "Case #%d: ", ind);
		fscanf(f, "%d %d %d", &k, &c, &s);
		if (k == 1)
		{
			fprintf(g, "1\n");
			continue;
		}
		if (c == 1)
		{
			if (s < k)
			{
				fprintf(g, "IMPOSSIBLE\n");
			}
			else
			{
				for (i = 1; i <= k; i++)
				{
					fprintf(g, "%d ", i);
				}
				fprintf(g, "\n");
			}
		}
		else
		{
			if (s < (k - 1))
			{
				fprintf(g, "IMPOSSIBLE\n");
			}
			else
			{
				for (i = 2; i <= k; i++)
				{
					fprintf(g, "%d ", i);
				}
				fprintf(g, "\n");
			}
		}
	}
}