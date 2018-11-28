#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <climits>
#include <cctype>

#define inf (1<<30)
#define eps 1e-5
#define ll long long
#define all(v)  v.begin() , v.end()
#define sc(x) scanf("%d",&x)
#define me(t,val) memset( t , val , sizeof(t) )

#define N 105
#define MOD 1000000007

using namespace std;

int n , m , t = 0;
int a[N][N];

void doit()
{
	for( int i = 0 ; i < n ; ++i )
		for( int j = 0 ; j < m ; ++j )
		{
			int maxi = 0;
			for( int k = 0 ; k < n ; ++k )
				maxi = max( maxi , a[k][j] );
			int maxi2 = 0;
			for( int k = 0 ; k < m ; ++k )
				maxi2 = max( maxi2 , a[i][k] );
			if( !( maxi == a[i][j] || maxi2 == a[i][j] ) )
			{
				printf( "Case #%d: NO\n" , ++t );
				return;	
			}
		}
	printf( "Case #%d: YES\n" , ++t );
}
int main()
{
	int tc;
	cin >> tc;
	while( tc --)
	{
		cin >> n >> m ;
		for( int i = 0 ; i < n ; ++i )
			for( int j = 0 ; j < m ; ++j )
				cin >> a[i][j];
		doit();
	}
}
