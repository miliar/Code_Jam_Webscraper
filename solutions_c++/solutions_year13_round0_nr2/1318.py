#include <iostream>
#include <algorithm>
#include <fstream>

using namespace std;

int test, T = 1;
int arr[200][200];
bool mark[200][200];
int st[200000];
int n, m;

ifstream fin( "B-large.in" );
ofstream fout( "B2.out" );
#define cin fin
#define cout fout

int main()
{
	for( cin >> test; test--; ){
		cin >> n >> m;
		for( int i = 0; i < n; i++ )
			for( int j = 0; j < m; j++ ){
				cin >> arr[i][j];
				st[i * m + j] = arr[i][j];
			}
		bool res = true;
		sort( st, st + n * m );
		for( int idx = 0; idx < n * m && res; idx++ ){
			if( idx && st[idx] == st[idx - 1] )
				continue;
			for( int i = 0; i < n; i++ ){
				for( int j = 0; j < m; j++ )
					if( arr[i][j] == st[idx] ){
						bool gg = true;
						for( int k = 0; k < m; k++ )
							if( arr[i][k] > st[idx] )
								gg = false;
						if( gg )
							continue;
						gg = true;
						for( int k = 0; k < n; k++ )
							if( arr[k][j] > st[idx] )
								gg = false;
						if( !gg ){
							res = false;
						}
					}
			}
		}
		if( res )
			cout << "Case #" << T++ << ": YES" << endl;
		else cout << "Case #" << T++ << ": NO" << endl;
	}
	return 0;
}