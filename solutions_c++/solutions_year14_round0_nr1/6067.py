#include <cstdio>
#include <algorithm>
#include <iostream>
#include <cmath>
using namespace std ;

void tCase() {
	int a, b, x=0, y=0 ;

	scanf("%d", &a ) ;
	for( int i=0; i<4; i++ ) {
		for( int j=0; j<4; j++ ) {
			int tmp ;
			scanf("%d", &tmp ) ;
			if( i+1==a )
				x += (1<<(tmp-1)) ;
		}
	}
	scanf("%d", &b ) ;
	for( int i=0; i<4; i++ ) {
		for( int j=0; j<4; j++ ) {
			int tmp ;
			scanf("%d", &tmp ) ;
			if( i+1==b )
				y += (1<<(tmp-1)) ;
		}
	}

	x &= y ;
	if( x==0 ) {
		printf("Volunteer cheated!\n" ) ;
		return ;
	}
	for( int i=0; i<16; i++ ) {
		if( (1<<i) & x ) {
			if( x-(1<<i) )
				printf("Bad magician!\n" ) ;
			else
				printf("%d\n", i+1 ) ;
			return ;
		}
	}
}

int main() {
	int T ;

	scanf("%d", &T ) ;
	for( int i=0; i<T; i++ ) {
		printf("Case #%d: ", i+1 ) ;
		tCase()  ;
	}

	return 0 ;
}
