#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std ;

int dr[] = { -1, -1, -1, 0, 0, 1, 1, 1 } ;
int dc[] = { -1 ,0 , 1, -1, 1, -1, 0,1 } ;
bool fin ;
int R, C, M ;

int ff( char grd[55][55], int r, int c ) {
	if( r<0 || r>=R || c<0 || c>=C || grd[r][c]=='*' || grd[r][c]=='c' )
		return 0 ;
	if( grd[r][c]=='X' ) {
		grd[r][c] = 'c' ;
		return 1 ;
	}
	grd[r][c] = 'c' ;
	int cnt = 1 ;
	for( int d=0; d<8; d++ ) 
		cnt += ff( grd, r+dr[d], c+dc[d] ) ;
	return cnt ;
}

bool vald( char grd[55][55] ) {
	for( int i=0; i<R; i++ ) {
		for( int j=0; j<C; j++ ) {
			if( grd[i][j]=='*' )
				continue ;
			bool fal = 0 ;
			for( int d=0, x, y; d<8; d++ ) {
				x = i+dr[d] ;
				y = j+dc[d] ;
				if( x<0 || x>=R || y<0 || y>=C )
					continue ;
				if( grd[x][y]=='*' ) {
					fal = 1  ;
					break ;
				}
			}
			if( fal ) 
				grd[i][j] = 'X' ; 
		}
	}
	for( int i=0; i<R; i++ ) {
		for( int j=0; j<C; j++ ) {
			if( grd[i][j]!='.' )
				continue ;
			if( ff(grd,i,j) + M == R*C )  {
				fin = 1 ;
				for( int x=0; x<R; x++ ) {
					for( int y=0; y<C; y++ ) {
						if( grd[x][y]!='*' )
							grd[x][y] = '.' ;
					}
				}
				grd[i][j] = 'c' ;
				for( int k=0; k<R; k++ ) 
					printf("%s\n", grd[k] ) ;
			}
			i = R ;
			break ;
		}
	}
	for( int i=0; i<R && !fin; i++ ) {
		for( int j=0; j<C; j++ ) {
			if( grd[i][j]!='X' )
				continue ;
			if( ff(grd,i,j) + M == R*C )  {
				fin = 1 ;
				for( int x=0; x<R; x++ ) {
					for( int y=0; y<C; y++ ) {
						if( grd[x][y]!='*' )
							grd[x][y] = '.' ;
					}
				}
				grd[i][j] = 'c' ;
				for( int k=0; k<R; k++ ) 
					printf("%s\n", grd[k] ) ;
			}
			i = R ;
			break ;
		}
	}
	if( !fin ) {
		for( int x=0; x<R; x++ ) {
			for( int y=0; y<C; y++ ) {
				if( grd[x][y]!='*' )
					grd[x][y] = '.' ;
			}
		}
	}
}

void test( char grd[55][55], int r, int c, int rem ) {
	if( rem==0 ) {
		vald( grd ) ;
		return ;
	}
	if( r>=R )
		return ;
	int r2=r, c2=c+1 ;
	if( c2==C ) {
		r2 ++ ;
		c2 = 0 ;
	}
	grd[r][c] = '*' ;
	test( grd, r2, c2, rem-1 ) ;
	if( fin )
		return ;
	grd[r][c] = '.' ;
	test( grd, r2, c2, rem ) ;
}

void tCase() {
	char grd[55][55] ;

	scanf("%d%d%d", &R, &C, &M ) ;
	if( M>=R*C ) {
		printf("Impossible\n" ) ;
		return ;
	}

	memset( grd, 0, sizeof(grd) ) ;
	for( int i=0; i<R; i++ ) 
		for( int j=0; j<C; j++ ) 
			grd[i][j] = '.' ;

	fin = 0 ;
	test( grd, 0, 0, M ) ;
	if( !fin )  {
		printf("Impossible\n" ) ;
		return ;
	}
}

int main() {
	int T ;

	scanf("%d", &T ) ;
	for( int i=1; i<=T; i++ ) {
		printf("Case #%d:\n", i ) ;
		tCase() ;
	}

	return 0 ;
}
