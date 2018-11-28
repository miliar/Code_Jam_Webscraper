#include <iostream>
#include <fstream>
using namespace std;

ifstream fin( "B1.in" );
ofstream fout( "B1.out" );
#define cin fin
#define cout fout

int dr[2][2] = {{1, 0}, {0, 1}};
int r, c, k;
int b[100][100];

int count(){
	int s = 0;
	int ret = 0;
	for( int i = 0; i < r; i++ )
		for( int j = 0; j < c; j++ ){
			if( b[i][j] == 0 )
				continue;
			s++;
			for( int z = 0; z < 2; z++ ){
				int ni = i + dr[z][0];
				int nj = j + dr[z][1];
				if( ni >= 0 && ni < r && nj >= 0 && nj < c && b[ni][nj] == 1 )
					ret++;
			}
		}
	if( s != k )
		return 100000;
	return ret;
}

int main()
{
	int test;
	cin >> test;
	for( int T = 1; T <= test; T++ ){
		cin >> r >> c >> k;
		int ret = 1000000;
		for( int i = 0; i < ( 1 << ( r * c ) ); i++ ){
			for( int j = 0; j < ( r * c ); j++ ){
				int x = j / c;
				int y = j % c;
				if( i & ( 1 << j ) )
					b[x][y] = 1;
				else b[x][y] = 0;
				ret = min( ret, count() );
			}
		}
		cout << "Case #" << T << ": " << ret << endl;
	}
	return 0;
}