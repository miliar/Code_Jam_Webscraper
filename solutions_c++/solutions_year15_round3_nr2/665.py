#include <bits/stdc++.h>
using namespace std;

int K, L, S;
string s1, s2;
int sum, tot, mx;

void bt( int x, string now )
{
	if( x == S )
	{
		int cc = 0, p;
		while( now.size() && ( p = now.find( s2 ) ) != now.npos )
			now = now.substr( p+1 ), cc ++;
		tot ++;
		sum += cc;
		mx = max( mx, cc );
		return;
	}
	for( int i = 0 ; i < s1.size() ; i ++ )
		bt( x+1, now + s1[i] );
}

int main()
{
	int t, cc = 0;
	cin >> t;
	while( t -- )
	{
		sum = tot = mx = 0;
		cin >> K >> L >> S;
		cin >> s1 >> s2;
		bt( 0, "" );
		printf( "Case #%d: %.9lf\n", ++ cc, mx - sum * 1. / tot );
	}
	return 0;
}
