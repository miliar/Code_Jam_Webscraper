//#ifdef QWERTYUIOP
#include <stdio.h>

FILE *in = fopen("input", "r");
FILE *out= fopen("output","w");

int max[3][105], mat[105][105], n, m;

bool solve()
{
	int i, j;
	int minim;
	fscanf(in, "%i %i", &n, &m);
	for(i = 0; i < n; i++)
		max[0][i] = 0;
	for(j = 0; j < m; j++)
		max[1][j] = 0;
	for(i = 0; i < n; i++)
		for(j = 0; j < m; j++)
		{
			fscanf(in, "%i", &mat[i][j]);

			if(mat[i][j] > max[0][i])
				max[0][i] = mat[i][j]; //maximum value of the line
			if(mat[i][j] > max[1][j])
				max[1][j] = mat[i][j]; //maximum value of the column
		}

	for(i = 0; i < n; i++)
		for(j = 0; j < m; j++)
		{
			minim = max[0][i];
			if(max[1][j] < minim)
				minim = max[1][j];

			if(mat[i][j] != minim)
				return false;
		}
	return true;
}

int main()
{
	int T, TC;

	fscanf(in, "%i", &T);

	for(TC = 1; TC <= T; TC++)
	{
		fprintf(out, "Case #%i: ", TC);
		if(solve())
			fprintf(out, "YES");
		else
			fprintf(out, "NO");
		fprintf(out, "\n");
	}
}

//#endif
