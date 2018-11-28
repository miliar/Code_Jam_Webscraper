#include <bits/stdc++.h>
using namespace std;
 
typedef pair< int , int > pii;
typedef long long LL;
#define fr first
#define se second
#define EPS 1e-8
#define INF 10000*10000*10000LL
stringstream ss;
#define two(x) ( 1LL<<x )
LL mod = 1000000007LL;

/**************************Code****************************/

int a[1<<21];

int r( int x )
{
	int ret = 0;
	while( x )
		ret = ret * 10 + x % 10, x /= 10;
	return ret;
}

int main()
{
	for( int i = 0 ; i < (1<<21) ; i ++ )
		a[i] = 1000000000;
	a[1] = 1;
	for( int i = 1 ; i+1 < (1<<21) ; i ++ )
	{
		a[i+1] = min( a[i+1], 1 + a[i] );
		int j = r(i);
		if( j < (1<<21) )
			a[j] = min( a[j], 1 + a[i] );
	}
	int t, n, cc = 0;
	cin >> t;
	while( t -- )
	{
		cin >> n;
		cout << "Case #" << ++ cc << ": " << a[n] << endl;
	}
	return 0;
}
