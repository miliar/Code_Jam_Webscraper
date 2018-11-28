#include <iostream>
#include <cstdio>
#include <cstring>

#define X_WIN "X won"
#define O_WIN "O won"
#define DRAW "Draw"
#define N_COMPLETE "Game has not completed"

using namespace std;

int main(){
	int T;
	cin >> T;
	char maps[4][5];
	char result[128];
	for( int ca = 1; ca <= T; ca++) {

		bool has_empty = false;
		bool x_win = false, o_win = false;
		for( int i = 0;i < 4;i++) {
			scanf(" %s", maps[i]);
		}

		for( int i = 0;i < 4; i++) {
			int o = 0, t = 0, x = 0;
			for( int j = 0; j < 4;j++) {
				if( maps[i][j] == 'O') {
					o++;
				}
				if( maps[i][j] == 'X') {
					x++;
				}
				if( maps[i][j] == 'T') {
					t++;
				}
				if( maps[i][j] == '.') {
					has_empty = true;
				}
			}
			if( o == 4 or ( o == 3 && t == 1)) {
				o_win = true;
			}
			if( x == 4 or ( x == 3 && t == 1)) {
				x_win = true;
			}
		}

		for( int j = 0; j < 4;j++) {
			int o = 0, t = 0, x = 0;
			for( int i = 0;i < 4; i++) {
				if( maps[i][j] == 'O') {
					o++;
				}
				if( maps[i][j] == 'X') {
					x++;
				}
				if( maps[i][j] == 'T') {
					t++;
				}
			}
			if( o == 4 or ( o == 3 && t == 1)) {
				o_win = true;
			}
			if( x == 4 or ( x == 3 && t == 1)) {
				x_win = true;
			}
		}
		{
			int o = 0, t = 0, x = 0;
			for( int i = 0;i < 4; i++) {
				if( maps[i][i] == 'O') {
					o++;
				}
				if( maps[i][i] == 'X') {
					x++;
				}
				if( maps[i][i] == 'T') {
					t++;
				}
			}
			if( o == 4 or ( o == 3 && t == 1)) {
				o_win = true;
			}
			if( x == 4 or ( x == 3 && t == 1)) {
				x_win = true;
			}
		}
		{
			int o = 0, t = 0, x = 0;
			for( int i = 0;i < 4; i++) {
				if( maps[i][3-i] == 'O') {
					o++;
				}
				if( maps[i][3-i] == 'X') {
					x++;
				}
				if( maps[i][3-i] == 'T') {
					t++;
				}
			}
			if( o == 4 or ( o == 3 && t == 1)) {
				o_win = true;
			}
			if( x == 4 or ( x == 3 && t == 1)) {
				x_win = true;
			}
		}
		if( x_win) {
			strcpy( result, X_WIN);
		}
		else if ( o_win) {
			strcpy( result, O_WIN);
		}
		else if( has_empty) {
			strcpy( result, N_COMPLETE);
		}
		else {
			strcpy( result, DRAW);
		}

		printf("Case #%d: %s\n", ca, result);
		/*for( int i = 0;i < 4;i++) {
			printf(" %s\n", maps[i]);
		}*/
	}
}
