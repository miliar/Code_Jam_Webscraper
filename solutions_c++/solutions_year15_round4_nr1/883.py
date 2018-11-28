#include <iostream>
#include <fstream>

using namespace std;

ifstream fin( "A2.in" );
ofstream fout( "A2.out" );
#define cin fin
#define cout fout

char b[200][200];
int r, c;

char ch[4] = { '>', '<', 'v', '^'};
int dir[4][2] = { {0, 1}, {0, -1}, {1, 0}, {-1, 0}};

int getId( char c ){
	for( int i = 0; i < 4; i++ )
		if( ch[i] == c )
			return i;
	return -1;
}

bool isIn( int x, int y ){
	return x >= 0 && y >= 0 && x < r && y < c;
}

bool go( int x, int y, int did ){
	int nx = x + dir[did][0];
	int ny = y + dir[did][1];
	while( isIn( nx, ny ) ){
		if( b[nx][ny] != '.' )
			break;
		nx = nx + dir[did][0];
		ny = ny + dir[did][1];
	}
	return !isIn( nx, ny );
}

int main()
{
	int test;
	cin >> test;
	for( int T = 1; T <= test; T++ ){
		cin >> r >> c;
		for( int i = 0; i < r; i++ )
			for( int j = 0; j < c; j++ )
				cin >> b[i][j];
		int res = 0;
		bool has = true;
		for( int i = 0; i < r; i++ )
			for( int j = 0; j < c; j++ ){
				if( b[i][j] != '.' ){
					if( go( i, j, getId( b[i][j] ) ) )
						res++;
					bool ff = true;
					for( int k = 0; k < 4; k++ )
						if( go( i, j, k ) == false )
							ff = false;
					if( ff )
						has = false;
				}
			}
		cout << "Case #" << T << ": ";
		if( !has )
			cout << "IMPOSSIBLE" << endl;
		else cout << res << endl;
	}

	return 0;
}