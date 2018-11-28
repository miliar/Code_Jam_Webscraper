#define LOCAL

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <algorithm>
#include <bitset>
#include <cassert>

using namespace std;

const int INF = 0x3f3f3f3f;
const double PI = 3.14159265358979323846;

//#define NAME "b"
#define NAME "B-large"
#define ABS( a ) ( (a) > 0 ? (a) : -(a) )
#define SIZE( a ) ( int( (a).size() ) )
#define LENGTH( a ) ( int( (a).length() ) )
#define SQR( a ) ( (a) * (a) )

double c, f, x;

double cnt( int m )
{
	double ret = 0.0;
	for( int i = 0; i < m; ++i ) 
		ret += c / ( 2.0 + i * f );
	ret += x / ( 2.0 + m * f );
	return ret;
}

int main()
{
  #ifdef LOCAL
  freopen( NAME".in", "rt", stdin );
  freopen( NAME".out", "wt", stdout );
  #endif
	
	int tests;
	scanf("%d", &tests);
	for( int test = 1; test < tests + 1; ++test )
	{
		scanf("%lf%lf%lf\n", &c, &f, &x);
		
		int l = 0, r = int(x) + 10;
		while( r - l > 1 )
		{
			int m = ( r + l ) >> 1;
			int m1 = ( l + m ) >> 1;
			int m2 = ( m + r ) >> 1;

			double t1 = cnt( m1 );
			double t2 = cnt( m2 );
			if( t1 < t2 ) r = m;
			else l = m;
		}

		double ans = INF;
		l -= 10;
		for( int i = 0; i < 20; ++i )
		{
			double cans = cnt( l + i );
			if( cans > 0 && ans > cans ) ans = cans;
		}
		printf("Case #%d: %.7lf\n", test, ans);
	}
	
  #ifdef LOCAL
  fclose( stdin );
  fclose( stdout );
  #endif

  return 0;
}       
