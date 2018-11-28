#include <cstdio>
#include <cstring>
#include <vector>
#include <set>
using namespace std;

vector<int> gt[2048];

void clearGraph()
{
	for ( int i = 0; i < 2010; i++ )
		gt[i].clear();
}

void addEdge( int a, int b )
{
//	if ( a && b )
//		printf( "%d < %d\n", a, b );
	gt[b].push_back( a );
}

int n, a[2048], b[2048];
int p[2048];
int x[2048];

int up[2048];

typedef pair<int,int> pii;
set<pii> S;

bool us[2048][2048];

void dfs( int st, int v )
{
	if ( v == 0 ) return;
	if ( us[st][v] )
		return;
	us[st][v] = 1;
	for ( int i = 0; i < (int) gt[v].size(); i++ )
	{
		int u = gt[v][i];
		dfs( st, u );
	}
}

int main()
{
	int i, j, k;
	int t, T;
	scanf( "%d", &T );
	for ( t = 1; t <= T; t++ )
	{
		fprintf( stderr, "TE %d\n", t );
		scanf( "%d", &n );
		for ( i = 1; i <= n; i++ )
			scanf( "%d", &a[i] );
		for ( i = 1; i <= n; i++ )
			scanf( "%d", &b[i] );
		
		clearGraph();
		
		memset( p, 0, sizeof( p ) );
		for ( i = 1; i <= n; i++ )
		{
			j = a[i];
			addEdge( p[j-1], i );
			addEdge( i, p[j] );
			p[j] = i;
		}
		
//		printf( "FIRST_PASS\n" );
		
		memset( p, 0, sizeof( p ) );
		for ( i = n; i > 0; i-- )
		{
			j = b[i];
			addEdge( p[j-1], i );
			addEdge( i, p[j] );
			p[j] = i;
		}
		
		memset( us, 0, sizeof( us ) );
		for ( i = 1; i <= n; i++ )
			us[n+1][i] = 1;
		
		memset( up, -1, sizeof( up ) );
		up[n+1] = n+1;
		S.clear();
		S.insert( make_pair( n+1, n+1 ) );
		set<pii>::iterator it;
		for ( i = 1; i <= n; i++ )
		{
			dfs( i, i );
			k = 0;
			//printf( "US %d\n", i );
			//for ( j = 1; j <= n; j++ )
			//	printf( "%d ", us[i][j] );
			//printf( "\n" );
			for ( it = S.begin(); it != S.end(); it++ )
			{
				pii pp = (*it);
				int l = pp.second;
				for ( j = 1; j <= n; j++ )
				{
					if ( us[l][j] == 0 && us[i][j] )
						break;
				}
				//printf( "%d %d %d\n", i, l, j );
				if ( j <= n )
				{
					for ( j = 1; j <= n; j++ )
						us[i][j] = (us[i][j] | us[l][j]);
				}
				else
				{
					k = 0;
					for ( j = 1; j <= n; j++ )
						k += (us[i][j]);
					//printf( "END %d %d\n", i, k );
					break;
				}
			}
			
			x[i] = k;
			S.insert( make_pair( k, i ) );
		}
		
		printf( "Case #%d:", t );
		for ( i = 1; i <= n; i++ )
			printf( " %d", x[i] );
		printf( "\n" );
	}
	return 0;
}
