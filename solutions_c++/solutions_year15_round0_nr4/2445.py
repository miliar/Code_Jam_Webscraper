#include <bits/stdc++.h>

using namespace std;

int main()
{
	int test;
	cin >> test;
	
	for( int t = 1; t <= test; t++ )
	{
		int x, r, c;
		cin >> x >> r >> c;
		
		if( r > c )
			swap( r, c );
			
		int area = r * c;
		string ans = "RICHARD";
		
		if( x == 1 )
			ans = "GABRIEL";
		
		if( x == 2 && area % 2 == 0 )
			ans = "GABRIEL";
		
		if( x == 3 )
		{
			if( r == 2 && c == 3 )
				ans = "GABRIEL";
			if( r == 3 && c == 3 )
				ans = "GABRIEL";
			if( r == 3 && c == 4 )
				ans = "GABRIEL";
		}
		
		if( x == 4 )
		{
			if( r == 3 && c == 4 )
				ans = "GABRIEL";
			if( r == c && c == 4 )
				ans = "GABRIEL";
		}
		
		printf( "Case #%d: %s\n", t, ans.c_str() );
	}
	
	return 0;
}
