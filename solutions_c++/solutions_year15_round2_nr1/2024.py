#include <stdio.h>

#define MAXN 1000010
int a[MAXN];
int pow[7];

int main()
{
	FILE *infile, *outfile;
	infile = fopen("A-small-attempt2.in", "r");
	outfile = fopen("outputA", "w");
	
	int t;
	pow[0] = 1;
	for (int i = 1; i < 7; ++i)
		pow[i] = pow[i-1]*10;
	
	fscanf(infile, "%d\n", &t);
	for (int ca = 1; ca <= t; ++ca)
	{
		fprintf(outfile, "Case #%d: ", ca);
		int n;
		fscanf(infile, "%d\n", &n);
		a[0] = 0;
		for (int i = 1; i <= n; ++i)
		{
			a[i] = a[i-1] + 1;
			if (i % 10 == 0) continue;
			int x = 0, tmp = i, k = 0;
/*			if (i == 10101)
			{
				tmp = i;
			} */
			for (int j = 6; j >= 0; --j)
				if (tmp - pow[j] >= 0)
				{
					x += (tmp / pow[j])*pow[k];
					++k;
					tmp = tmp % pow[j];
				}
				else if (k > 0) ++k;
			if (x < i && a[x] + 1 < a[i]) a[i] = a[x] + 1;
		}
		
		fprintf(outfile, "%d\n", a[n]);
	}
	
	return 0;
}