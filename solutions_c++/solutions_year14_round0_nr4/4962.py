#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

int war ( vector<int> va, vector<int> vb )
{
	int res = 0, n = va.size();
	for ( int j = 0; j < n; ++j ) {
		int t = -1;
		for ( int i = 0; i < vb.size(); ++i ) {
			if ( vb[i] > va[0] ) {
				t = i;
				break;
			}
		}
		if ( t == -1 ) {
			t = 0;
		}
		res += va[0] > vb[t];
		vb.erase( vb.begin() + t );
		va.erase( va.begin() );
	}
	return res;
}

int deceitfulWar ( vector<int> va, vector<int> vb )
{
	int res = 0, n = va.size();
	sort( vb.rbegin(), vb.rend() );
	for ( int i = 0; i < n; ++i ) {
		res += va[i] > vb[i];
	}
	return res;
}

int main( void )
{
	int T;
	cin >> T;

	for ( int t = 1; t <= T; ++t ) {
		int n;
		cin >> n;

		vector<int> va( n ), vb( n );

		for ( int i = 0; i < n; ++i ) {
			double weight;
			cin >> weight;
			va[i] = weight * 1000;
		}
		for ( int i = 0; i < n; ++i ) {
			double weight;
			cin >> weight;
			vb[i] = weight * 1000;
		}

		sort( va.begin(), va.end() );
		sort( vb.begin(), vb.end() );

		int dw = n - war( vb, va ),
			w = war( va, vb );

/*
		for ( int i = 0; i < n; ++i ) {
			printf( "%4d ", va[i] );
		}
		printf( "\n" );
		for ( int i = 0; i < n; ++i ) {
			printf( "%4d ", vb[i] );
		}
		printf( "\n" );
*/
		printf( "Case #%d: %d %d\n", t, dw, w );
	}
	return 0;
}
