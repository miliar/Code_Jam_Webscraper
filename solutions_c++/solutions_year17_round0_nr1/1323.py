#include <iostream>
#include <string>

using namespace std;

int main()
{
	freopen( "A-large.in", "r", stdin );
	freopen( "A-large.out", "w", stdout );
	int T;
	cin >> T;
	for( int t = 1; t <= T; t++ )
	{
		string s;
		int k, flips = 0;
		cin >> s >> k;
		for( size_t i = 0; i < s.size(); i++ )
		{
			if( s[ i ] == '-' )
			{
				if( i + k > s.size() )
				{
					flips = -1;
					break;
				}
				flips++;
				for( size_t j = i; j < i + k; j++ )
				{
					s[ j ] = ( s[ j ] == '-' ) ? '+' : '-';
				}
			}
		}
		cout << "Case #" + to_string( t ) + ": " + (( flips == -1 ) ? "IMPOSSIBLE" : to_string( flips )) << endl;
	}
	return 0;
}
