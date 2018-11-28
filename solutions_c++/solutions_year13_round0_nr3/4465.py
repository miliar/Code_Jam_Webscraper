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

LL A[1010], sz;

int pal( LL x )
{
	string a = "";
	while( x )
	{
		a = a + char( '0' + x%10 );
		x /= 10;
	}
	int l = a.size()-1;
	for( int i = 0 ; i <= l ; i ++ )
		if( a[i] != a[l-i] )
			return 0;
	return 1;
}

int f( LL x )
{
	int l = 0, r = sz;
	while( l+1 < r )
	{
		int mid = ( l + r ) / 2;
		if( A[mid] >= x )
			r = mid;
		else
			l = mid;
	}
	if( A[r] < x )
		r ++;
	return r;
}

int main()
{
	sz = 0;
	for( LL i = 0 ; i < 2000020 ; i ++ )
		if( pal( i ) && pal( i * i ) )
			A[ sz++ ] = i*i;
	LL a, b;
	int t, cc = 0;
	cin >> t;
	while( t -- )
	{
		cin >> a >> b;
		int l = f( a ), r = f( b );
		int cnt = 0;
		for( int i = l ; i <= r ; i ++ )
			if( a <= A[i] && A[i] <= b )
				cnt ++;
		cout << "Case #" << ++ cc << ": " << cnt << endl;
	}
	return 0;
}
