#include <list>
#include <set>
#include <map>
#include <ctime>
#include <stack>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <queue>
#include <deque>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <iterator>
#include <cassert>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <complex>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
 
#define For(i,n) for( int i=0; i < n; i++)
#define FOR(i,a,b) for( __typeof(b) i=(a); i<=(b); i++)
#define ALL(c)  c.begin() , c.end()
#define LL long long
#define int64 LL
#define Set(t,v) memset((t), (v), sizeof(t))

typedef vector < int > VI;
typedef pair< int , int > PII;
#define fr first
#define se second
#define pi M_PI
#define rad(x) (x)*acos(-1)/180.0
#define EPS 1e-6
#define INF 10000*10000
stringstream ss;
#define two(x) ( 1LL<<x )
#define sq(x) ( (x)*(x) )
LL mod = 1000000007LL;

/**************************Code****************************/

LL R, t;
int ok( LL a )
{
	LL p = 1;
	int c1 = 0, c2 = 0;
	while( p < a )
		p *= 10, c1 ++;
	p = 1;
	while( p < R )
		p *= 10, c2 ++;
	if( c1 + c2 > 18 )
		return 0;
	LL x = 2LL * a * R + 2LL * a * a - a;
	return x <= t;
}

int main()
{
	int tc, cc = 0;
	cin >> tc;
	while( tc -- )
	{
		cin >> R >> t;
		LL l = 1, r = 100000LL * 10000LL;
		while( l+1 < r )
		{
			LL mid = ( l + r ) / 2;
			if( ok( mid ) )
				l = mid;
			else
				r = mid;
		}
		if( ok( l+1 ) )
			l ++;
		cout << "Case #" << ++ cc << ": " << l << endl;
	}
	return 0;
}
