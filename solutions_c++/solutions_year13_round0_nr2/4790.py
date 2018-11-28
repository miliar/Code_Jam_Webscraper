#include <cstdio>
#include <algorithm>
#include <cstring>
#include <map>

using namespace std;

int a[128][128];
int N, M;

bool chk( int x, int y, int i, int j )
{
	int t = a[x][y];
	while( 1 )
	{
		x += i, y += j;
		if( x < 0 || y < 0 || x >= N || y >= M )
			return 1;
		if( a[x][y] > t )
			return 0;
	}
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int T, cases = 1;
	int i, j, t;
	bool ok, k;

	scanf("%d", &T);
	while( T-- )
	{
		ok = 1;

		scanf("%d %d", &N, &M);
		for( i = 0; i < N; ++i )
			for( j = 0; j < M; ++j )
				scanf("%d", &a[i][j]);
		
		for( i = 0; i < N; ++i )
			for( j = 0; j < M; ++j )
			{
				k = 0;
				k |= (chk(i, j, 1, 0)&chk(i, j, -1, 0));
				k |= (chk(i, j, 0, 1)&chk(i, j, 0, -1));
				ok &= k;
			}

		if( ok )
			printf("Case #%d: YES\n", cases++);
		else
			printf("Case #%d: NO\n", cases++);
	}

	return 0;
}