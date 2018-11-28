#include <stdio.h>

int main()
{
	FILE * infile, *outfile;
	infile = fopen("D-small-attempt1.in", "r");
	outfile = fopen("output", "w");
	
	int tt;
	fscanf(infile, "%d\n", &tt);
	for (int ca = 1; ca <= tt; ++ca)
	{
		fprintf(outfile, "Case #%d: ", ca);
		int x, r, c;
		fscanf(infile, "%d %d %d\n", &x, &r, &c);
		// if x-ominoes cannot fit the the board
		if (r * c % x != 0)
		{
			fprintf(outfile, "RICHARD\n");
			continue;
		}
		if (x > r && x > c)
		{
			fprintf(outfile, "RICHARD\n");
			continue;
		}
		if (x > 2 && (r == 1 || c == 1))
		{
			fprintf(outfile, "RICHARD\n");
			continue;
		}
		if (x == 4 && (r <= 2 || c <= 2))
		{
			fprintf(outfile, "RICHARD\n");
			continue;
		}
		fprintf(outfile, "GABRIEL\n");
	}
	return 0;
}