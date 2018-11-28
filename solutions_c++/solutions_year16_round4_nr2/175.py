#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std ;

int N , K ;

double P[209] , A[209] ;
double F[209][209] ;

double DP() {
	for ( int i = 0 ; i <= K ; i ++ )
		for ( int j = 0 ; j <= K ; j ++ )
			F[i][j] = 0.0 ;
	F[0][0] = 1.0 ;
	for ( int i = 1 ; i <= K ; i ++ ) {
		F[i][0] = 1.0 ;
		for ( int j = 1 ; j <= i ; j ++ ) F[i][0] *= (1.0 - A[j]) ;
		for ( int j = 1 ; j <= i ; j ++ )
			F[i][j] = F[i-1][j-1] * A[i] + F[i-1][j] * (1.0 - A[i]) ;
	}
	return F[K][K/2] ;
}

void Solve() {
	double ans = 0.0 ;
	for ( int i = 0 ; i <= K ; i ++ ) {
		int j = 0 ;
		for ( int k = 1 ; k <= i ; k ++ ) A[++j] = P[k] ;
		for ( int k = N-(K-i)+1 ; k <= N ; k ++ ) A[++j] = P[k] ;
		double ret = DP() ;
		if ( ret > ans ) ans = ret ;
	}
	cout.precision(12) ;
	cout << fixed << ans << "\n" ;
}

int main() {
	freopen("B-large.in" , "r" , stdin) ;
	freopen("B-large.out", "w" ,stdout) ;
	
	int Test ; cin >> Test ;
	for ( int i = 1 ; i <= Test ; i ++ ) {
		cin >> N >> K ;
		for ( int j = 1 ; j <= N ; j ++ ) cin >> P[j] ;
		sort(P+1 , P+N+1) ;
		cout << "Case #" << i << ": " ;
		Solve() ;
	}
}