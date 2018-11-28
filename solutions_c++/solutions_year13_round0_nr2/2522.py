#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

// #define DEV 1
const int MAXN = 100;

int main() {
	#ifndef DEV
		freopen( "B-large.in", "r", stdin );
		freopen( "B-large.out", "w+", stdout );
	#endif

	int t;
	int A[ MAXN ][ MAXN ];
	int maxRow[ MAXN ];
	int maxCol[ MAXN ];

	cin>>t;
	
	for( int i = 0; i < t; ++i ) {
		bool f = true;
		int n, m;
		cin>>n>>m;

		memset( maxRow, 0, sizeof( maxRow ) );
		memset( maxCol, 0, sizeof( maxCol ) );

		for( int j = 0; j < n; ++j ) {
			for( int k = 0; k < m; ++k ) {
				cin>> A[ j ][ k ];
				maxRow[ j ] = max( maxRow[ j ], A[ j ][ k ] );
				maxCol[ k ] = max( maxCol[ k ], A[ j ][ k ] );
			}
		}

		for( int j = 0; j < n; ++j ) {
			for( int k = 0; k < m; ++k ) {
				if( A[ j ][ k ] < maxRow[ j ] && A[ j ][ k ] < maxCol[ k ] ) {
					f = false;
					break;
				}
			}
			if( !f )
				break;
		}

		cout<< "Case #" << i+1 << ": ";
		if( f )
			cout<< "YES";
		else
			cout<< "NO";
		cout<<endl;

	}

	#ifdef DEV
		system( "PAUSE" );
	#endif
	return 0;
}
