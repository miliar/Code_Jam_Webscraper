#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

ifstream fin( "C1.in" );
ofstream fout( "C1.out" );
#define cin fin
#define cout fout

int bit[( 1 << 27 )];

struct trip{
	int a, b, c;
	trip(){}
	trip( int _a, int _b, int _c ){
		a = _a, b = _b, c = _c;
	}
};

int main()
{
	for( int i = 0; i < ( 1 << 27 ); i++ )
		bit[i] = ( i & 1 ) + bit[i >> 1];
	int test;
	cin >> test;
	for( int T = 1; T <= test; T++ ){
		cerr << T << endl;
		vector< trip > v, res;
		int a, b, c, k;
		cin >> a >> b >> c >> k;
		for( int i = 1; i <= a; i++ )
			for( int j = 1; j <= b; j++ )
				for( int z = 1; z <= c; z++ )
					v.push_back( trip( i, j, z ) );
		int sz = v.size();
		for( int mask = 0; mask < ( 1 << sz ); mask++ ){
			if( bit[mask] <= res.size() )
				continue;
			int g[3][3][10][10] = {0};
			vector< trip > sel;
			bool valid = true;
			for( int m = 0; m < sz; m++ )
				if( mask & ( 1 << m ) ){
					g[0][1][v[m].a][v[m].b]++;
					if( g[0][1][v[m].a][v[m].b] > k ){
						valid = false;
						break;
					}

					g[0][2][v[m].a][v[m].c]++;
					if( g[0][2][v[m].a][v[m].c] > k ){
						valid = false;
						break;
					}

					g[1][2][v[m].b][v[m].c]++;
					if( g[1][2][v[m].b][v[m].c] > k ){
						valid = false;
						break;
					}
					sel.push_back( v[m] );
				}
			if( valid && sel.size() > res.size() )
				res = sel;
		}
		cout << "Case #" << T << ": " << res.size() << endl;
		for( int i = 0; i < res.size(); i++ )
			cout << res[i].a << ' ' << res[i].b << ' ' << res[i].c << endl;
	}
	return 0;
}