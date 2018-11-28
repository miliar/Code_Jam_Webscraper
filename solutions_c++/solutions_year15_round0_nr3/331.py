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

typedef pair < int, char > pic;

pic val( pic x, pic y )
{
	if( x.se == '1' )
		return pic( x.fr * y.fr, y.se );
	else if( x.se == 'i' )
	{
		if( y.se == '1' )
			return pic( x.fr * y.fr, 'i' );
		else if( y.se == 'i' )
			return pic( x.fr * y.fr * -1, '1' );
		else if( y.se == 'j' )
			return pic( x.fr * y.fr, 'k' );
		else if( y.se == 'k' )
			return pic( x.fr * y.fr * -1, 'j' );
	}
	else if( x.se == 'j' )
	{
		if( y.se == '1' )
			return pic( x.fr * y.fr, 'j' );
		else if( y.se == 'i' )
			return pic( x.fr * y.fr * -1, 'k' );
		else if( y.se == 'j' )
			return pic( x.fr * y.fr * -1, '1' );
		else if( y.se == 'k' )
			return pic( x.fr * y.fr, 'i' );
	}
	else if( x.se == 'k' )
	{
		if( y.se == '1' )
			return pic( x.fr * y.fr, 'k' );
		else if( y.se == 'i' )
			return pic( x.fr * y.fr, 'j' );
		else if( y.se == 'j' )
			return pic( x.fr * y.fr * -1, 'i' );
		else if( y.se == 'k' )
			return pic( x.fr * y.fr * -1, '1' );
	}
}

int large( string s, LL X )
{
	int N = s.size();
	if( X % 4 == 0 )
		return 0;
	pic now = pic( 1, '1' );
	for( int i = 0 ; i < s.size() ; i ++ )
		now = val( now, pic( 1, s[i] ) );
	if( X % 4 == 3 )
		now = val( now , val( now, now ) );
	else if( X % 4 == 2 )
		now = val( now , now );
	if( now != pic( -1, '1' ) )
		return 0;
	LL mx = N * 5;
	now = pic( 1, '1' );
	int ii = -1;
	for( int i = 0 ; i < mx ; i ++ )
	{
		now = val( now, pic( 1, s[ i % N ] ) );
		if( now == pic( 1, 'i' ) )
		{
			ii = i;
			break;
		}
	}
	if( ii == -1 )
		return 0;
	now = pic( 1, '1' );
	for( int i = 0 ; i < mx ; i ++ )
	{
		now = val( pic( 1, s[ N-1 + ( -i % N ) ] ), now );
		if( now == pic( 1, 'k' ) )
			if( ii + i +2 < X * N )
				return 1;
	}
	return 0;
}

int main()
{
	int tc, cc = 0;
	LL L, X;
	string s, t;
	cin >> tc;
	while( tc -- )
	{
		cin >> L >> X;
		cin >> s;
		cout << "Case #" << ++ cc << ": " << ( large( s, X ) ? "YES" : "NO" ) << endl;
	}
	return 0;
}
