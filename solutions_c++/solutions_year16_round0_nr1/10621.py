#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <set>
using namespace std;
int T, n;

int main() {
	freopen( "A.in", "r", stdin );
	freopen( "A.out", "w", stdout );

	scanf( "%d", &T );
	for ( int cas = 1; cas <= T; cas ++ ) {
		scanf( "%d", &n );
		
		if ( n == 0 ) {
			printf( "Case #%d: %s\n", cas, "INSOMNIA" );
		} else {
			int ans = n;
			set <int> st;
			st.clear();
			for	( int i = 1; (int)st.size() != 10 ; i ++ ) {
				int x = ans;
				while ( x )	{
					st.insert( x % 10 );
					x /= 10;
				}
				ans += n;							
			}
			printf( "Case #%d: %d\n", cas, ans - n );
		}
	}

	return 0;
}












