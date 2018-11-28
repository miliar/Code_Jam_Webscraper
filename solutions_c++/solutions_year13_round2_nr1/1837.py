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

int N, a[110];
map < PII , int > dp;

int calc( int A , int x , int &AA )
{
	int ret = 0;
	while( A <= a[x] )
	{
		A += A-1;
		ret ++;
	}
	AA = A + a[x];
	return ret;
}

int f( int pos , int A )
{
	if( pos == N )
		return 0;
	if( dp.count( PII( pos , A ) ) )
		return dp[ PII( pos , A ) ];
	int ret = 1 + f( pos+1 , A ), cur = 0, p = pos;
	while( A <= a[p] )
		A += A-1, cur ++;
	while( p < N && A > a[p] )
	{
		A += a[p];
		p ++;
	}
	ret = min( ret , cur + f( p , A ) );
	return dp[ PII( pos , A ) ] = ret;
}

int main()
{
	int tc, cc = 0;
	int A;
	cin >> tc;
	while( tc -- )
	{
		dp.clear();
		cin >> A >> N;
		for( int i = 0 ; i < N ; i ++ )
			cin >> a[i];
		sort( a , a+N );
		if( A == 1 )
			cout << "Case #" << ++ cc << ": " << N << endl;
		else
			cout << "Case #" << ++ cc << ": " << f( 0 , A ) << endl;
	}
	return 0;
}
