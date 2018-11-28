#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t, cc = 0;
	cin >> t;
	while( t -- )
	{
		string s;
		cin >> s;
		while( s.size() > 0 && s[ s.size()-1 ] == '+' )
			s = s.substr( 0, s.size()-1 );
		char c = s[0];
		int ans = ( s.find( '-' ) != s.npos );
		if( ans )
		{
			for( int i = 1 ; i < s.size() ; i ++ )
				if( c != s[i] )
					c = s[i], ans ++;
		}
		cout << "Case #" << ++ cc << ": " << ans << endl;
	}
	return 0;
}
