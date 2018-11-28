//#include "stdafx.h"

#include <iostream>
#include <cstring>

using namespace std;

int a[110][110] = {};


int main() {
	//cout <<"hello google2" << endl;
	int t, n, m;
	bool flagCU, flagCL, flagAns;
	cin >> t;
	for( int k = 0; k < t; k++ ) {

		flagAns = true;
		memset( a, 0, sizeof(a) );
		cin >> n >> m;
		for( int i = 1; i <= n; i++ ) {
			for( int j = 1; j <= m; j++ ) {
				cin >> a[i][j];
			}
		}

		for( int i = 1; i <= n; i++ ) {
			for( int j = 1; j <= m; j++ ) {
				

				flagCU = true;
				for( int k = 1; k <= n; k++ ) {
					if( a[i][j] < a[k][j] ) { flagCU = false; break; }
				}
				flagCL = true;
				for( int k = 1; k <= m; k++ ) {
					if( a[i][j] < a[i][k] ) { flagCL = false; break; }
				}

				if( ! ( flagCU || flagCL ) ) flagAns = false;
			}
		}

		
		if( flagAns ) cout << "Case #" << k+1 << ": YES" << endl;
		else cout << "Case #" << k+1 << ": NO" << endl;

	}
		


	return 0;
}
