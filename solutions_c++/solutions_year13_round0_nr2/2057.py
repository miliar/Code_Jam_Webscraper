#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>
#include <list>
#include <set>
#include <iostream>

using namespace std;
int field[101][101];

int main()
{
	freopen( "data.in", "r", stdin );
	freopen( "data.out", "w", stdout );
	
	int t;
	cin >> t;
	for(  int k = 0; k < t; k++ ) {
		bool hasSol = true;

		int n, m;
		cin >> n >> m;
		for( int i = 0; i < n; i++ ) {
			for( int j = 0; j < m; j++ ) {
				cin >> field[i][j];
			}
		}

		for( int i = 0; i < n; i++ ) {
			for( int j = 0; j < m; j++ ) {
				bool hasLocal = true;
				for( int k = 0; k < m; k++ ) {
					if( field[i][k] > field[i][j] ) {
						hasLocal = false;
						break;
					}
				}
				if( hasLocal ) {
					continue;
				}

				hasLocal = true;
				for( int k = 0; k < n; k++ ) {
					if( field[k][j] > field[i][j] ) {
						hasLocal = false;
						break;
					}
				}
				hasSol &= hasLocal;
			}
		}
		if( hasSol ) {
			printf( "Case #%d: YES\n", k + 1 );
		} else {
			printf( "Case #%d: NO\n", k + 1 );
		}
	}



	return 0;
}