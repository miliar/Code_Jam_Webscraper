#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std ;

void tCase() {
	double a, b, c, t=1.0*0, crg=2.0 ;
	double res ;
	int K ;

	scanf("%lf%lf%lf", &a, &b, &c ) ;
	res = c/2.0 ;
	K = ceil(c) ;

	for( int i=0; i<K; i++ ) {
		t += a/crg ;
		crg += b ;
		res = min( res, t + c/crg ) ;
	}

	printf("%.9lf\n", res ) ;
}

int main() {
	int T ;

	scanf("%d", &T ) ;
	for( int i=0; i<T; i++ ) {
		printf("Case #%d: ", i+1) ;
		tCase() ;
	}

	return 0 ;
}
