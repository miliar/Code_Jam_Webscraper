#include <cstdio>
#include <cstring>

double c;
double f;
double x;

bool deq( double l, double r ) {
	double dist = ( l > r ) ? ( l - r ) : ( r - l );
	return dist < 0.0000001;
}

double time( double r, int n ) {
	if ( n == 0 ) {
		return x / r;
	} else {
		double straight = ( x - c ) / r;
		double recur = time( r + f, n - 1 );
		return ( c / r ) + ( ( straight < recur ) ? straight : recur );
	}
}

int main() {

	int T;
	scanf( "%d", &T );
	for ( int t = 1; t <= T; t++ ) {
		
		scanf( "%lf %lf %lf", &c, &f, &x );
		
		double last = time( 2.0, 0 );
		double current;
		bool stop = false;
		int i = 1;
		while ( !stop ) {
			current = time( 2.0, i );
			if ( deq( current, last ) ) {
				stop = true;
			} else {
				last = current;
				i++;
			}
		}
		
		printf( "Case #%d: %.7f\n", t, current );
		
	}
	
	return 0;
}