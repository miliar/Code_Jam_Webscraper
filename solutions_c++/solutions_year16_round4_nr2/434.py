#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std ;

#define MAXN 200 + 10

int a[MAXN] ;
double P[MAXN] , P_[MAXN] , f[MAXN][MAXN] ;
int T ;
int N , K ;
double ans ;

/*void DP() {
	memset( f , 0 , sizeof(f) ) ;
	f[0][0] = 1 ;
	for (int i = 1 ; i <= K ; i ++ ) {
		int k = a[i] ;
		for (int j = 1 ; j <= K ; j ++ ) {
			f[i][j] = (1.0 - P[k]) * f[i-1][j] + P[k] * f[i-1][j-1] ;
		}
		f[i][0] = (1.0 - P[k]) * f[i-1][0] ;
	}
}*/

/*void BF( int k , int Cnt ) {
	if ( Cnt > K ) return ;
	if ( k > N ) {
		if ( Cnt == K ) {
			DP() ;
			if ( f[K][K/2] > ans ) ans = f[K][K/2] ;
		}
		return ;
	}
	BF( k + 1 , Cnt ) ;
	a[Cnt+1] = k ;
	BF( k + 1 , Cnt + 1 ) ;
}*/

void Solve( int nn ) {
	a[0] = 0 ;
	for (int i = 1 ; i <= nn ; i ++ ) a[++a[0]] = i ;
	for (int i = N - (K - nn) + 1 ; i <= N ; i ++ ) a[++a[0]] = i ;
	memset( f , 0 , sizeof(f) ) ;
	f[0][0] = 1 ;
	for (int i = 1 ; i <= K ; i ++ ) {
		int k = a[i] ;
		for (int j = 1 ; j <= K ; j ++ ) {
			f[i][j] = (1.0 - P[k]) * f[i-1][j] + P[k] * f[i-1][j-1] ;
		}
		f[i][0] = (1.0 - P[k]) * f[i-1][0] ;
	}
}

int main() {
	freopen( "B.in" , "r" , stdin ) ;
	freopen( "B.out" , "w" , stdout ) ;
	scanf( "%d" , &T ) ;
	for (int Case = 1 ; Case <= T ; Case ++ ) {
		printf( "Case #%d: " , Case ) ;
		if ( Case == 8 ) {
			Case ++ ;
			Case -- ;
		}
		ans = 0 ;
		memset( P , 0 , sizeof(P) ) ;
		scanf( "%d%d" , &N , &K ) ;
		for (int i = 1 ; i <= N ; i ++ ) {
			scanf( "%lf" , &P[i] ) ;
		}
		sort( P + 1 , P + N + 1 ) ;
		//BF( 1 , 0 ) ;
		for (int i = 0 ; i <= K ; i ++ ) {
			Solve( i ) ;
			if ( f[K][K/2] > ans ) ans = f[K][K/2] ;
		}
		printf( "%.8lf\n" , ans ) ;
	}
	return 0 ;
}
