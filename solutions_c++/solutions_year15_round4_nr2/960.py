/**
 * Tittle:	2015 Google Code Jam Round2 - PB
 * Author:	Cheng-Shih, Wong
 * Date:	2015/05/30
 */

// include files
#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

// definitions
#define FOR(i,a,b) for( int i=(a),_n=(b); i<=_n; ++i )
#define clr(x,v) memset( x, v, sizeof(x) )
#define EPS 1e-8
#define N 105

// declarations
int t;
int n;
double v, x;
double r[N], c[N];
double rc[N];

// functions
inline int dcmp( double x )
{
	if( x < -EPS ) return -1;
	return x > EPS;
}

// main function
int main( void )
{
	double maxt;
	double t1, t2;

	// input
	scanf( "%d", &t );

	FOR( ti, 1, t ) {
		scanf( "%d%lf%lf", &n, &v, &x );
		FOR( i, 1, n ) {
			scanf( "%lf%lf", &r[i], &c[i] );
			rc[i] = r[i]*c[i];
		}

		// output
		printf( "Case #%d: ", ti );

		if( n == 1 ) {
			maxt = (x*v)/rc[1];

			if( dcmp(r[1]*maxt-v)!=0 || dcmp(c[1]-x)!=0 ) puts("IMPOSSIBLE");
			else printf( "%.10lf\n", maxt );
		} else {
			if( dcmp(c[1]-x)>0 && dcmp(c[2]-x)>0 ) {
				puts("IMPOSSIBLE");
				continue;
			}
			if( dcmp(c[1]-x)<0 && dcmp(c[2]-x)<0 ) {
				puts("IMPOSSIBLE");
				continue;
			}
			if( dcmp(c[1]-c[2])==0 ) {
				if( dcmp(c[1]-x)!=0 ) puts("IMPOSSIBLE");
				else printf( "%.10lf\n", v/(r[1]+r[2]) );

				continue;
			}

			t2 = (c[1]-x)/((r[2]/v)*(c[1]-c[2]));
			t1 = (v-r[2]*t2)/r[1];

			if( dcmp(t1)<0 || dcmp(t2)<0 ) puts("IMPOSSIBLE");
			else printf( "%.10lf\n", max( t1, t2 ) );
		}
	}
	
	return 0;
}
