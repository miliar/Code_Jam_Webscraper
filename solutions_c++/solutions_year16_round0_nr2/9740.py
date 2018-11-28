#include <bits/stdc++.h>

using namespace std;

enum orientation { sad, happy };

int main()
{
	int test;
	scanf( "%d\n", &test );

	for( int t = 1; t <= test; t++ )
	{
		string st;
		cin >> st;

		reverse( st.begin(), st.end() );

		int n = st.size();
		int ans = 0;

		// cout << st << endl << endl;

		for( int i = 0; i < n; i++ )
		{
			if( st[ i ] == '+' )
			{
				continue;
			}

			ans++;

			for( int j = i, k = n-1; j <= k; j++, k-- )
			{
				swap( st[ j ], st[ k ] );

				st[ j ] = ( st[ j ] == '+' ) ? '-' : '+';
				st[ k ] = ( st[ k ] == '+' ) ? '-' : '+';

				if( j == k )
				{
					st[ k ] = ( st[ k ] == '+' ) ? '-' : '+';
				}
			}

			// cout << st << endl;

			if( st[ i ] == '-' )
			{
				ans++;

				while( i < n )
				{
					if( st[ i ] == '+' )
					{
						break;
					}

					st[ i++ ] = '+';
				}
			}
		}

		printf( "Case #%d: %d\n", t, ans );
	}

	return 0;
}