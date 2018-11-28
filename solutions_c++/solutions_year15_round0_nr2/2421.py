#include <stdio.h>
#include <string.h>

#define MAXN 1100
#define MAXP 1100

int c[MAXP];

int main()
{
	FILE *infile, *outfile;
	infile = fopen("B-large.in", "r");
	outfile = fopen("output", "w");
	
	int tt;
	fscanf(infile, "%d\n", &tt);
	for (int ca = 1; ca <= tt; ++ca)
	{
		fprintf(outfile, "Case #%d: ", ca);
		int n;
		fscanf(infile, "%d\n", &n);
		memset(c, '\0', sizeof(c));
		int max = 0, max2 = 0, ans = 0;
		for (int i = 0; i < n; ++i)
		{
		  int x;
		  fscanf(infile, "%d", &x);
		  ++c[x];
		  if (x > max) max = x;
		}
		ans = max;
		for (int li = max; li >= 1; --li)
		{
			//int cc[MAXP];
			//memset(cc, '\0', sizeof(cc));
			//for (int i = 0; i <= max; ++i) cc[i] = c[i];
			int tmp = 0;
			for (int i = max; i > li; --i)
			{
				tmp += (i / li) * c[i];
				if (i % li == 0) tmp -= c[i];
			}
			if (tmp + li < ans) ans = tmp + li;
		}
		fprintf(outfile, "%d\n", ans);
	}
	return 0;
}
