#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std ;

#define MAXN 50 + 10

bool vis[MAXN] ;
int map[MAXN][MAXN] ;
int T ;
int N , K ;
int ans ;

bool Judge( int k , int s ) {
	if ( k > N ) return 1 ;
	else {
		for (int i = 1 ; i <= N ; i ++ ) {
			if ( s & ( 1 << (i - 1) ) ) continue ; // Exist
			bool flag = 0 ;
			for (int j = 1 ; j <= N ; j ++ ) {
				if ( !map[i][j] || vis[j] ) continue ; // Not Exist || Visited
				//TEST!!!!!
				//
				//
				if ( i == 2 && j == 2 ) {
					i ++ ;
					i -- ;
				}
				vis[j] = 1 ;
				flag = 1 ;
				if ( !Judge( k + 1 , s + (1 << (i - 1)) ) ) return 0 ;
				vis[j] = 0 ;
			}
			if ( flag ) continue ;
			else return 0 ;
		}
		return 1 ;
	}
}

void DFS( int x , int y , int Cnt ) {
	if ( Cnt > ans ) return ;
	if ( y > N ) { DFS( x + 1 , 1 , Cnt ) ; return ; }
	if ( x > N ) {
		memset( vis , 0 , sizeof(vis) ) ;
		if ( Judge( 1 , 0 ) ) ans = min( ans , Cnt ) ;
		return ;
	}
	if ( map[x][y] ) DFS( x , y + 1 , Cnt ) ;
	else {
		DFS( x , y + 1 , Cnt ) ;
		map[x][y] = 1 ;
		DFS( x , y + 1 , Cnt + 1 ) ;
		map[x][y] = 0 ;
	}
}

int main() {
	freopen( "D.in" , "r" , stdin ) ;
	freopen( "D.out" , "w" , stdout ) ;
	scanf( "%d" , &T ) ;
	for (int Case = 1 ; Case <= T ; Case ++ ) {
		printf( "Case #%d: " , Case ) ;
		if ( Case == 17 ) {
			Case ++ ;
			Case -- ;
		}
		scanf( "%d" , &N ) ;
		ans = 0x7FFFFFFF ;
		for (int i = 1 ; i <= N ; i ++ ) {
			scanf( "\n" ) ;
			for (int j = 1 ; j <= N ; j ++ ) {
				char ch ;
				scanf( "%c" , &ch ) ;
				map[i][j] = ch - '0' ;
			}
		}
		DFS( 1 , 1 , 0 ) ;
		printf( "%d\n" , ans ) ;
	}
	return 0 ;
}
