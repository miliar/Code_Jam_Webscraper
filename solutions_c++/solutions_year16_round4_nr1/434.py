#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std ;

#define MAXN 50000 + 10

char ans[MAXN] , tp[MAXN] ;
int tot[MAXN] ;
int Cnt ;
int T ;
int N , R , P , S ;

bool Check() {
	return tot['R'] == R && tot['P'] == P && tot['S'] == S ;
}

void Solve( int l1 , int r1 , int l2 , int r2 ) {
	bool Large = 0 ;
	for (int i = l1 ; i <= r1 ; i ++ ) {
		int j = l2 + i - l1 ;
		if ( tp[i] > tp[j] ) { Large = 1 ; break ; }
	}
	if ( !Large ) return ;
	for (int i = l1 ; i <= r1 ; i ++ ) {
		int j = l2 + i - l1 ;
		swap( tp[i] , tp[j] ) ;
	}
}

char Lose( char s ) {
	if ( s == 'P' ) return 'R' ;
	if ( s == 'R' ) return 'S' ;
	if ( s == 'S' ) return 'P' ;
}

void DFS( int l , int r , char s ) {
	if ( l + 1 == r ) {
		if ( s == 'P' ) tp[++Cnt] = 'P' , tp[++Cnt] = 'R' , tot['P'] ++ , tot['R'] ++ ;
		if ( s == 'S' ) tp[++Cnt] = 'P' , tp[++Cnt] = 'S' , tot['P'] ++ , tot['S'] ++ ;
		if ( s == 'R' ) tp[++Cnt] = 'R' , tp[++Cnt] = 'S' , tot['R'] ++ , tot['S'] ++ ;
		return ;
	}
	int mid = (l + r) / 2 ;
	DFS( l , mid , s ) ;
	DFS( mid + 1 , r , Lose(s) ) ;
	Solve( l , mid , mid + 1 , r ) ;
}

void Copy( int l , int r ) {
	for (int i = l ; i <= r ; i ++ ) ans[i] = tp[i] ;
}

int main() {
	freopen( "A.in" , "r" , stdin ) ;
	freopen( "A.out" , "w" , stdout ) ;
	scanf( "%d" , &T ) ;
	for (int Case = 1 ; Case <= T ; Case ++ ) {
		memset( ans , 0 , sizeof(ans) ) ;
		bool ex = 0 ;
		if ( Case == 12 ) {
			Case ++ ;
			Case -- ;
		}
		printf( "Case #%d: " , Case ) ;
		scanf( "%d%d%d%d" , &N , &R , &P , &S ) ;
		int m = 1 << N ;
		Cnt = 0 ;
		memset( tp , 0 , sizeof(tp) ) ;
		memset( tot , 0 , sizeof(tot) ) ;
		DFS( 1 , m , 'P' ) ;
		if ( Check() ) Copy( 1 , m ) , ex = 1 ;
		Cnt = 0 ;
		memset( tp , 0 , sizeof(tp) ) ;
		memset( tot , 0 , sizeof(tot) ) ;
		DFS( 1 , m , 'R' ) ;
		if ( Check() ) {
			if ( ex && strcmp( ans , tp ) < 0 ) Copy( 1 , m ) ;
			if ( !ex ) Copy( 1 , m ) ;
			ex = 1 ;
		}
		Cnt = 0 ;
		memset( tp , 0 , sizeof(tp) ) ;
		memset( tot , 0 , sizeof(tot) ) ;
		DFS( 1 , m , 'S' ) ;
		if ( Check() ) {
			if ( ex && strcmp( ans , tp ) < 0 ) Copy( 1 , m ) ;
			if ( !ex ) Copy( 1 , m ) ;
			ex = 1 ;
		}
		if ( ex ) printf( "%s\n" , ans + 1 ) ;
		else printf( "IMPOSSIBLE\n" ) ;
	}
	return 0 ;
}
