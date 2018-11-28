#include <bits/stdc++.h>
using namespace std;

int mat[64][64];
long long ways[64];

#define two(x) (1LL<<(x))

int main()
{
	int t, tc = 0;
	cin >> t;
	while( t -- )
	{
		memset( mat, 0, sizeof mat );
		memset( ways, 0, sizeof ways );
		long long b, m;
		cin >> b >> m;
		ways[1] = 1;
		for( int i = 2 ; i < b ; i ++ )
		{
			for( int j = 1 ; j < i ; j ++ )
				mat[j][i] = 1, ways[i] += ways[j];
		}
		for( int i = b-1 ; i >= 0 ; i -- )
			if( m >= ways[i] )
			{
				m -= ways[i];
				mat[i][b] = 1;
			}
		cout << "Case #" << ++ tc << ": ";
		if( m )
			cout << "IMPOSSIBLE" << endl;
		else
		{
			cout << "POSSIBLE" << endl;
			for( int i = 1 ; i <= b ; i ++ )
			{
				for( int j = 1 ; j <= b ; j ++ )
					cout << mat[i][j];
				cout << endl;
			}
		}
	}
	return 0;
}