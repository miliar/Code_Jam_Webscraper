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
int n, a[1<<20];

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
	fscanf(fin, "%d", &ntest);
	for ( itest = 0; ++itest <= ntest; )
	{
		int st, best;
		fscanf(fin, "%d%d", &st, &n);
		best = n;
		for ( i = 0; i < n; ++i )
			fscanf(fin, "%d", a+i);
		sort(a, a+n);
		for ( i = 0; ++i <= n; )
		{
			int t = st, cur = n - i;
			for ( j = 0; j < i; ++j )
			{
				while ( t <= a[j] )
				{
					if ( ++cur >= best )
						break;
					t += t-1;
				}
				t += a[j];
			}
			if ( cur < best )
				best = cur;
		}
		fprintf(fout, "Case #%d: %d\n", itest, best);
	}
	return 0;
}
