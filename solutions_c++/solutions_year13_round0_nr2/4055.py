#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <vector>
#include <list>
#include <map>
#include <string>

using namespace std;

#define ProblemName "B"
#define InputSize   "large"

int check_ij( vector< vector<int> > &lawn, int N, int M, int i, int j )
{
	int ok = 1;

	for(int r = 0; r < N; r++)
	{
		if ( lawn[r][j] > lawn[i][j] )
			ok = 0;
	}

	if ( !ok )
	{
		ok = 1;
		for(int c = 0; c < M; c++)
		{
			if ( lawn[i][c] > lawn[i][j] )
				ok = 0;
		}
	}

	return ok;
}

char* check( vector< vector<int> > &lawn, int N, int M)
{
	for(int i = 0; i < N; i++)
	{
		for(int j = 0; j < M; j++)
		{
			if ( !check_ij(lawn, N, M, i, j) )
			{
				return "NO";
			}
		}
	}

	return "YES";
}

int main(int argc, char **argv)
{
	freopen(ProblemName "-" InputSize ".in", "rb", stdin);
	freopen(ProblemName "-" InputSize ".out", "wb", stdout);

	int T;
	scanf("%d", &T);
	for ( int t = 1; t <= T; t++ )
	{
		int N, M;
		scanf("%d %d", &N, &M);
		vector< vector< int > > lawn(N);
		for ( int l = 0; l < N; l++ )
		{
			lawn[l].resize(M);
			for(int i = 0; i < M; i++)
			{
				scanf( "%d", &lawn[l][i]);
			}
		}

		printf("Case #%d: %s\n", t, check(lawn, N, M));
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}