#include <iostream>
#include <string>

using namespace std;

int is( char x )
{
	return !( x == 'a' || x == 'e' || x == 'i' || x == 'o' || x == 'u' );
}
int f( string a )
{
	int mx = 0;
	for( int i = 0 ; i < a.size() ; i ++ )
	{
		int cc = 0;
		while( i < a.size() && is( a[i] ) )
			cc ++, i ++;
		mx = max( mx , cc );
	}
	return mx;
}

int main()
{
	int t, n, cc = 0;
	string s;
	cin >> t;
	while( t -- )
	{
		cin >> s >> n;
		int res = 0;
		for( int i = 0 ; i < s.size() ; i ++ )
			for( int j = 1 ; i+j <= s.size() ; j ++ )
				res += ( f( s.substr( i , j ) ) >= n );
		cout << "Case #" << ++ cc << ": " << res << endl;
	}
	return 0;
}
