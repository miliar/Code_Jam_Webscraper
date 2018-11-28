#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std ;

#define N 200 + 10

char S[N] ;
int T , Len , size ;

void Solve() {
	int i = 1 ;
	Len = strlen( S + 1 ) ;
	while ( i <= Len ) {
		size ++ ;
		while ( S[i+1] == S[i] && i < Len ) i ++ ;
		i ++ ;
	}
}

int main() {
	freopen( "B.in" , "r" , stdin ) ;
	freopen( "B.out" , "w" , stdout ) ;
	scanf( "%d" , &T ) ;
	for (int k = 1 ; k <= T ; k ++ ) {
		printf( "Case #%d: " , k ) ;
		scanf( "%s" , S + 1 ) ;
		size = 0 ;
		Solve() ;
		if ( S[Len] == '+' ) size -- ;
		printf( "%d\n" , size ) ;
	}
	return 0 ;
}
