#include <bits/stdc++.h>

using namespace std;

char s[ 1005 ];

int main()
{
	int test;
	cin >> test;
	
	for( int t = 1; t <= test; )
	{
		int n;
		scanf( "%d %s", &n, s );
		n++;
		
		int up = 0, ans =  0;
		for( int i = 0; i < n; i++ )
		{
			if( up < i && s[ i ] != '0' )
				ans += i - up, up = i;
			
			up += s[ i ] - '0';
		}
		
		printf( "Case #%d: %d\n", t++, ans );
	}
	
	return 0;
}
