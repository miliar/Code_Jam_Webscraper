#include <cstdio>
#include <algorithm>

#define EPS 0.0000000001

using namespace std;

int main( void )
{
	int T;
	freopen("in.txt","rt",stdin);
	freopen("out.txt","wt",stdout);
	scanf("%d", &T );
	for( int z = 1; z <= T; z++ ) {
		double C, F, X, ans = 0, rate = 2.0;
		scanf("%lf%lf%lf", &C, &F, &X );
		for( int i = 0;; i++ ) {
			double cost_farm = ( double )( C / rate ) + ( double )( X / ( double )( rate + F ) );
			double cost = ( double )( X / rate );
			if( cost_farm - cost < EPS ) {
				ans = ( double )( ans + ( double )( C / rate ) );
				rate = ( double )( rate + F );
			} else {
				ans = ( double )( ans + ( double )( X / rate ) );
				break;
			}
		}
		printf("Case #%d: %0.7lf\n", z, ans );
	}
	return 0;
}
