#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<vector>
#include<string>
#include<queue>
#include<map>
#include<iostream>
#include<set>
#include<utility>
#include<algorithm>
using namespace std;

int f(int Y, int X, int M, vector<vector<int> > &ans){
	int m = X * Y - M;
	if( M == 0 || m == 1 || X == 1 || Y == 1 ){
		for( int y = 0; y < Y; y ++ ){
			for( int x = 0; x < X; x ++ ){
				ans[y][x] = (m > 0 ? '.' : '*');
				-- m;
			}
		}
		ans[0][0] = 'c';
		return 1;
	}

	for( int y = 0; y < Y; y ++ )
		for( int x = 0; x < X; x ++ )
			ans[y][x] = '*';

	for( int xx = 2; xx <= X; xx ++ ){
		if( m%xx != 1 && m/xx >= 2 && (m+xx-1)/xx <= Y ){
			for( int y = 0; y < Y; y ++ ){
				for( int x = 0; x < xx; x ++ ){
					ans[y][x] = (m > 0 ? '.' : '*');
					-- m;
				}
			}

			ans[0][0] = 'c';
			return 1;
		}
	}

	for( int yy = 2; yy <= Y; yy ++ ){
		if( m%yy != 1 && m/yy >= 2 && (m+yy-1)/yy <= X ){
			for( int x = 0; x < X; x ++ ){
				for( int y = 0; y < yy; y ++ ){
					ans[y][x] = (m > 0 ? '.' : '*');
					-- m;
				}
			}

			ans[0][0] = 'c';
			return 1;
		}
	}
	if( X == 5 && Y == 5 && M == 4 ){
		for( int y = 0; y < Y; y ++ )
			for( int x = 0; x < X; x ++ )
				ans[y][x] = '.';
		ans[2][2] = 'c';
		ans[0][0] = '*';
		ans[1][0] = '*';
		ans[3][4] = '*';
		ans[4][4] = '*';
		return 1;
	}
	if( X == 4 && Y == 4 && M == 3 ){
		for( int y = 0; y < Y; y ++ )
			for( int x = 0; x < X; x ++ )
				ans[y][x] = '.';
		ans[3][3] = 'c';
		ans[0][0] = '*';
		ans[1][0] = '*';
		ans[0][1] = '*';
		return 1;
	}
	if( m <= 3 || m == 5 || m == 7 ) return -1;
	return 0;
}

int main()
{
/*
	for( int Y = 1; Y <= 5; Y ++ ){
	for( int X = 1; X <= 5; X ++ ){
		vector< vector<int> > ans(Y, vector<int>(X, '@') );
		for( int M = 0; M < X*Y; M ++ ){
			int v = f(Y,X,M,ans);
			if( v == 0 ){
				printf( "NG: %d %d %d(%d)\n", Y, X, M,X*Y-M );
			}
		}
	}}
*/
	int T;
	cin >> T;
	for( int C = 1; C <= T; C ++ ){
		int Y, X, M;
		cin >> Y >> X >> M;
		vector< vector<int> > ans(Y, vector<int>(X, '@') );
		printf( "Case #%d:\n", C );
		if( f(Y, X, M, ans ) > 0 ){
			for( int y = 0; y < Y; y ++ ){
				for( int x = 0; x < X; x ++ ){
					printf( "%c", ans[y][x] );
				}
				printf( "\n" );
			}
		}
		else{
			printf( "Impossible\n" );
		}
	}
}
