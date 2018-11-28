#include <iostream>
#include <fstream>
using namespace std;

int T, R, C, M;
int arr[6][6];
bool mark[6][6];

bool valid[6][6][100];
int b[6][6][100][6][6];
ifstream fin( "C1.in" );
ofstream fout( "C1.out" );
#define cin fin
#define cout fout

int dx[3] = {-1, 0, 1};
int dy[3] = {-1, 0, 1};

bool check( int x, int y ){
	if( x < 0 || x >= R || y < 0 || y >= C )
		return false;
	return true;
}

int count( int x, int y ){
	int cnt = 0;
	for( int i = 0; i < 3; i++ )
		for( int j = 0; j < 3; j++ ){
			int nx = x + dx[i];
			int ny = y + dy[j];
			if( check( nx, ny ) == false || ( x == nx && y == ny ) )
				continue;
			if( arr[nx][ny] == 1 )
				cnt++;
		}
	return cnt;
}

int dfs( int x, int y ){
	int ret = 1, cnt = count( x, y );
	mark[x][y] = true;
	if( cnt == 0 ){
		for( int i = 0; i < 3; i++ )
		for( int j = 0; j < 3; j++ ){
			int nx = x + dx[i];
			int ny = y + dy[j];
			if( check( nx, ny ) == false || ( x == nx && y == ny ) )
				continue;
			if( mark[nx][ny] == false && arr[nx][ny] == 0 )
				ret += dfs( nx, ny );
		}
	}
	return ret;
}

int main()
{
	//cin >> T;
	int ret = 0;
	for(  R = 1; R <= 5; R++ )
		for(C = 1; C <= 5; C++ ){
			for( int a = 0; a < ( 1 << ( R * C ) ); a++ ){
				//cout << R << ' ' << C << ' ' << a << endl;
				int bomb = 0;
				memset( arr, 0, sizeof arr );
				for( int i = 0; i < R; i++ )
					for( int j = 0; j < C; j++ ){
						int idx = i * C + j;
						if( a & ( 1 << idx ) ){
							arr[i][j] = 1;
							bomb++;
						}
						else arr[i][j] = 0;
					}
				if( valid[R][C][bomb] )
					continue;
				memset( mark, 0, sizeof mark );
				int status = -1;
				for( int i = 0; i < R && status == -1; i++ )
					for( int j = 0; j < C && status == -1; j++ )
						if( arr[i][j] == 0 && count( i, j ) == 0 ){
							int u = dfs( i, j );
							/*if( R == 2 && C == 4 && a == 51 ){
								cout << a << ' ' << status << ' ' << u << ' ' << i << ' ' << j << endl;
								for( int k = 0; k < R; k++ ){
									for( int z = 0; z < C; z++ )
										cout << arr[k][z];
									cout << endl;
								}
							}*/
							status = (  u == ( R * C - bomb ) );
							arr[i][j] = 2;
						}
				
				if( status == -1 ){
					for( int i = 0; i < R && status == -1; i++ )
					for( int j = 0; j < C && status == -1; j++ )
						if( arr[i][j] == 0 ){
							int u =  dfs( i, j );
							
							status = ( u == ( R * C - bomb ) );
							arr[i][j] = 2;
						}
				}
				if( status == 1 ){
					//cout << R << ' ' << C << ' ' << bomb << endl;
					valid[R][C][bomb] = true;
					for( int i = 0; i < R; i++ )
						for( int j = 0; j < C; j++ )
							b[R][C][bomb][i][j] = arr[i][j];
				}
			}
		}
	int r, c;
	cin >> T;
	for( int tt = 1; tt <= T; tt++ ){
		cin >> r >> c >> M;	
		cout << "Case #" << tt << ":\n";
		if( valid[r][c][M] == false )
			cout << "Impossible" << endl;
		else{
			for( int i = 0; i < r; i++ ){
				for( int j = 0; j < c; j++ ){
					int cc = b[r][c][M][i][j];
					if( cc == 2 )
						cout << 'c';
					else if( cc == 1 )
						cout << '*';
					else cout << '.';
				}
				cout << endl;
			}
		}
	}
	return 0;
}