/**
 *  zoj_1446
 */

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

#define N	4
char map[10][10];

bool x_win(char ch='X') {
	int i, j;
	for ( i = 0; i < N; ++ i ) {
		for ( j = 0; j < N; ++ j ) {
			if ( !( map[i][j] == ch || map[i][j] == 'T' ) )
				break;		
		}
		if ( j >= N )
			return true;
	}

	for ( j = 0; j < N; ++ j ) {
		for ( i = 0; i < N; ++ i ) {
			if ( !( map[i][j] == ch || map[i][j] == 'T' ) )
				break;	
		}
		if ( i >= N )
			return true;
	}

	for ( i = 0; i < N; ++ i ) {
		if ( !( map[i][i] == ch || map[i][i] == 'T' ) )
			break;
	}
	if ( i >= N )
		return true;

	for ( i = 0; i < N; ++ i ) {
		if ( !( map[i][N-1-i] == ch || map[i][N-1-i] == 'T' ) )
			break;
	}
	if ( i >= N )
		return true;

	return false;
}

int main() 
{
	int  i, j, k, t;
	bool bFull;
	freopen( "out.txt", "w", stdout );

	scanf("%d", &t );
	for ( k = 1; k <= t; ++ k ) {
		for ( i = 0; i < N; ++ i )
			scanf("%s", map[i] );

		bFull = true;
		for ( i = 0; i < N; ++ i ) {
			for ( j = 0; j < N; ++ j ) {
				if ( '.' == map[i][j] ) {
					bFull = false;
					break;
				}
			if ( j < N )	break;
			}
		}

		printf("Case #%d: ", k );
		//ÅÐ¶ÏX win
		if ( x_win() ) {
			printf("X won\n");
		}
		else if ( x_win('O') ) {
			printf("O won\n");
		}
		else if ( bFull ) {
			printf("Draw\n");
		}
		else 
			printf("Game has not completed\n");
		
	}
	
	return 0;
}
