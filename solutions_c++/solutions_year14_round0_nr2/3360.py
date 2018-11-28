#include <iostream>
using namespace std;

double solve( double speed_now , double speed_inc , double sum , double cost ) {
	if ( sum + 1e-7 <= cost )
		return sum / speed_now ;
	// printf( "%lf %lf %lf %lf %lf " , speed_now , speed_inc , sum , cost , cost / speed_now ) ;
	if ( sum / speed_now < sum / ( speed_now + speed_inc ) + cost / speed_now ) {
		// printf( "Doing\n" ) ;
		return sum / speed_now ;
	} else {
		// printf( "Buy\n" ) ;
		return cost / speed_now + solve( speed_now + speed_inc , speed_inc , sum , cost ) ;
	}
}

int main() {
	freopen( "B-large.in" , "r" , stdin ) ;
	freopen( "B-large.out" , "w" , stdout ) ;

	int test_case ;
	scanf( "%d" , &test_case ) ;
	for ( int t = 1 ; t <= test_case ; t ++ ) {
		double c , f , x ;
		scanf( "%lf %lf %lf" , &c , &f , &x ) ;
		printf( "Case #%d: %.7lf\n" , t , solve( 2.00 , f , x , c ) ) ;
	}
}