
#include <iostream>
#include <cstdio>
#include <string.h>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
using namespace std;

#define fr( i , c , n ) for( int i = (c) ; i < (n) ;i++ )
#define clr( a , c ) memset( a , c , sizeof a )
#define P pair<int , int>
#define ULL unsigned long long

#define maxn 1000
int mine[maxn][maxn];
int his[maxn][maxn];
int main()
{

	int T; cin >> T;
	fr( t , 1 , T+1 )
	{
		int n , m; cin >> n >> m;
		fr( i , 0 , n )
		{
			int mx = 0;
			fr( j , 0 , m )
			{
				cin >> his[i][j];
				mx = max( mx , his[i][j] );
			}
			fr( j , 0 , m )
				mine[i][j] = mx;
		}

		fr( j , 0 , m )
		{
			int mx = 0;
			fr( i , 0 , n )
				mx = max( mx , his[i][j] );
			fr( i , 0 , n )
				mine[i][j] = min( mine[i][j] , mx );
		}

		bool ok = true;
		fr( i , 0 , n )
			fr( j , 0 , m )
			if( mine[i][j] != his[i][j] )
			{
				ok = false;
				break;
			}

			if( ok )
				printf("Case #%d: YES\n" , t );
			else
				printf("Case #%d: NO\n" , t );
	}
}