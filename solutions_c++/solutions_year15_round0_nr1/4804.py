#include <stdio.h>
#include <stdlib.h>
int main()
{
	FILE *f, *g;
	f = fopen("fis.in", "r");
	g = fopen("fis1.out", "w");
	int T, ind, s_max, suma[2000], k, i, rez;
	char c;
	fscanf(f, "%d", &T);
	for (ind = 0; ind < T; ind++)
	{
		rez = 0;
		fscanf(f, "%d", &s_max);
		s_max++;
		fscanf(f, "%c", &c);
		fscanf(f, "%c", &c);
		suma[0] = c - 48;
		for (i = 1; i < s_max; i++)
		{
			fscanf(f, "%c", &c);
			if (suma[i - 1] < i && c != '0')
			{
				rez = rez + i - suma[i - 1];
				suma[i - 1] = i;
			}
			suma[i] = suma[i - 1] + c - 48;
		}
		fprintf(g, "Case #%d: %d\n", ind + 1, rez);
	}
	fclose(f);
	fclose(g);
}