#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

#define EPS 1e-7

int t, ti = 0;
double c, f, x, p;
double ans;

const int dcmp( const double x ) { if( x < -EPS ) return -1; return x > EPS; }

int main( void )
{
	int i;

	scanf( "%d", &t );

	while( t-- ) {
		scanf( "%lf%lf%lf", &c, &f, &x );
		ans = 0;
		p = 2.0;

		while( dcmp( (x/p) - (c/p+x/(p+f)) ) > 0 ) {
			ans += c/p;
			p += f;
		}
		ans += x/p;

		printf( "Case #%d: %.7lf\n", ++ti, ans );
	}


	return 0;
}
