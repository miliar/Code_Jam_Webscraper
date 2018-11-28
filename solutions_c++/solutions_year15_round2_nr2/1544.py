#include<cstring>
#include<cstdio>
#include<algorithm>
using namespace std;
const int N = 15;

int n, m, p, ans;
bool bz[N][N];

void Dfs( int x, int y, int p )
{
	if ( x==n ) 
	{
		if ( p ) return;
		int c = 0;
		for (int i = 0 ; i < n ; i ++) for (int j = 0 ; j < m ; j ++)
		{
			if ( i ) c += ( bz[ i-1 ][j] && bz[i][j] );
			if ( j ) c += ( bz[i][ j-1 ] && bz[i][j] );
		}
		ans = min( ans , c );
		return;
	}
	Dfs( x + ( y+1 )/m, ( y+1 )%m, p );
	bz[x][y] = 1;
	Dfs( x + ( y+1 )/m, ( y+1 )%m, p - 1 );
	bz[x][y] = 0;
}

int main()
{
	//freopen("b.in" , "r" , stdin);freopen("b.out" , "w" , stdout);
	
	int T;scanf("%d" , &T);
	
	for (int vp = 1 ; vp <= T ; vp ++)
	{
		scanf("%d%d%d" , &n , &m , &p);
		ans = 0x7FFFFFFF;
		Dfs(0 , 0 , p);
		printf("Case #%d: %d\n" , vp , ans);
	}
}
