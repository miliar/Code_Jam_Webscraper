/** Libr@ries **/
//#include "bits/stdc++.h"
#include "stdio.h"
#include "string.h"
#include "cmath"
#include "iostream"
#include "algorithm"
#include "map"
#include "set"
#include "vector"

/** System **/
#define _ ios_base::sync_with_stdio(0);cin.tie(0);

/** System_Win_32 **/
#if ( WIN32 || __WIN32_ )
   #define lld I64d
#endif

/** Utilities **/
#define forit(i,v  )  for(__typeof((v).begin()) i = (v).begin(); i != (v).end(); i++)
#define fori( i,a,b)  for (int i = (int)(a); i < (int)(b); i++)
#define forn( i, n )  fori( i, 0, n )
#define zeros( a )    memset(a, 0,sizeof(a))
#define null( a )     memset(a,-1,sizeof(a))
#define all( a )      (a).begin() , (a).end()
#define sqr( a )      ( (a)*(a) )
#define sz( a )       (a).size()
#define pb            push_back
#define mp            make_pair
#define F             first
#define S             second
#define PI            2*acos(0.0)
using namespace std;
typedef long long LL;

const int maxn = 1009;
int m[ maxn ];
int sa[ maxn ];

int main(int argc, char const *argv[])
{
    int t;
    cin >> t;

    for (int caso = 0; caso < t; ++caso)
    {
    	int x=0, y=0, maxi=0;
    	int n;
    	cin >> n;
    	sa[ 0 ] = 0;
    	for (int i = 0; i < n; ++i)
    	{
    		cin >> m[ i ];
			maxi = max( maxi, m[i]);
    	}

    	m[ n ] = 1<<25;

    	for (int i = 0; i < n; ++i)
    	{
    		if ( m[i] > m [i+1] )	
    			x += m[ i ] - m[ i+1 ];
    	}


		m[ n ] = 0;
		y = 1 <<25;
    	for (int j = 0; j <= maxi; ++j)
    	{
    		int yaux = 0;
	    	for (int i = 0; i < n-1; ++i)
	    	{
	    		if ( m[i]-j > m[i+1] ){
	    			yaux = 1<<25;
	    			break;
	    		}
	    		yaux += min( j, m[i] );
	    	}
	    	y = min( y,  yaux );
    	}


    	printf("Case #%d: %d %d\n", caso+1, x, y );
    }
    return 0;
}

