#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std ;

typedef long long LL ;

LL N , P ;

LL Solve1() {
	for ( LL i = (1<<N) ; i >= 1 ; i -- ) {
		LL Ans = 0 ; 
		LL Up = (i-1) ;
		for ( LL j = 1 ; j <= N ; j ++ ) {
			if ( Up == 0 ) Ans *= 2 ;
			else {
				Ans = Ans * 2 + 1 ;
				Up = (Up-1) / 2 ;
			}
		}
		if ( Ans+1 <= P ) return i-1 ;
	}
}

LL Solve2() {
	for ( LL i = (1<<N) ; i >= 1 ; i -- ) {
		LL Ans = 0 ;
		LL Up = (1<<N)-i ;
		for ( LL j = 1 ; j <= N ; j ++ ) {
			if ( Up == 0 ) Ans = Ans * 2 + 1 ;
			else {
				Ans = Ans * 2 ;
				Up = (Up-1) / 2 ;
			}
		}
		if ( Ans+1 <= P ) return i-1 ;
	}
}

int main() {
	freopen("B.in","r",stdin) ;
	freopen("B.out","w",stdout) ;
	
	LL Test ; cin >> Test ;
	for ( LL i = 1 ; i <= Test ; i ++ ) {
		cin >> N >> P ;
		cout << "Case #" << i << ": " << Solve1() << " " << Solve2() << "\n" ;
	}
}




