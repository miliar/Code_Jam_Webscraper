#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

FILE *fin, *fout;
double c[1<<12][1<<12];

int main()
{
	int ntest, itest, i, j;
	char path[260];
	gets(path);
	if ( !*path )
	{
		fin = stdin;
		fout = stdout;
	}
	else
	{
		fin = fopen(path, "r");
		i = strlen(path);
		if ( i > 3 && !strcmp(path+i-3, ".in") )
			i -= 3;
		strcpy(path+i, ".out");
		fout = fopen(path, "w");
	}
	c[0][0] = 1;
	for ( i = 0; !(++i>>12); )
		for ( c[i][j = 0] = 1; !(++j>>12); )
			c[i][j] = c[i-1][j-1] + c[i-1][j];
	fscanf(fin, "%d", &ntest);
	for ( itest = 0; ++itest <= ntest; )
	{
		int n, x, y, level;
		fscanf(fin, "%d%d%d", &n, &x, &y);
		if ( x < 0 )
			x = -x;
		for ( level = 0; n > 0; level += 2 )
		{
			if ( x + y == level )
				break;
			n -= 2*level + 1;
		}
		fprintf(fout, "Case #%d: ", itest);
		if ( n > 0 )
		{
			if ( y + level < n )
				fprintf(fout, "1.0\n");
			else if ( !x )
				fprintf(fout, "0.0\n");
			else
			{
				double res = 1, sum = 1;
				for ( j = 0; j < n; ++j )
					sum *= 0.5;
				for ( j = 0; j < level; ++j )
					if ( j < level && n - j < level )
						res -= c[n][j] * sum;
				res *= 0.5;
				for ( j = 0; j < level; ++j )
					if ( j < level && n - j < level && y < j )
						res += c[n][j] * sum;
				fprintf(fout, "%.7f\n", res);
			}
		}
		else
			fprintf(fout, "0.0\n");
	}
	return 0;
}
