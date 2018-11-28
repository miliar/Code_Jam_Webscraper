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

int n;

long long getBestRank(long long x)
{
	long long high = x, low = ( (long long) 1 << n ) - x - 1, rank = 0;
	for ( int i = 0; i < n; ++i )
	{
		rank <<= 1;
		if ( low )
			--low;
		else
			--high, ++rank;
		low >>= 1;
		high = high + 1 >> 1;
	}
	return rank;
}

long long getMax(long long p)
{
	long long low = 0, high = (long long) 1 << n;
	while ( low < high )
	{
		long long mid = low + high >> 1;
		if ( getBestRank(mid) < p )
			low = mid + 1;
		else
			high = mid;
	}
	return low - 1;
}

int main()
{
	int ntest, itest, i, j;
	char path[260];
	gets_s(path, sizeof(path));
	if ( !*path )
	{
		fin = stdin;
		fout = stdout;
	}
	else
	{
		if ( path[0] == '"' )
		{
			strcpy_s(path, sizeof(path), path+1);
			i = strlen(path);
			while ( --i > 0 && path[i] <= ' ' ) ;
			path[i] = 0;
		}
		fopen_s(&fin, path, "r");
		i = strlen(path);
		if ( i > 3 && !strcmp(path+i-3, ".in") )
			i -= 3;
		strcpy_s(path+i, sizeof(path)-i, ".out");
		fopen_s(&fout, path, "w");
	}
	fscanf_s(fin, "%d", &ntest);
	for ( itest = 0; ++itest <= ntest; )
	{
		long long p, size, res;
		fscanf_s(fin, "%d%lld", &n, &p);
		size = ( (long long) 1 << n );
		res = size-2 - getMax(size - p);
		if ( res < 0 )
			res = 0;
		fprintf(fout, "Case #%d: %lld %lld\n", itest, res, getMax(p));
	}
	return 0;
}

/*

3
3 4
3 5
3 3
 */
