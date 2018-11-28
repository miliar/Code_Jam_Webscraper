#include <cstdio>
#include <iostream>

using namespace std;

const double eps = 0.0000001;

double c, f, x;

void read() {
	scanf ( "%lf %lf %lf", &c, &f, &x );
}

void solve ( int test ) {
	double cur = 2.0, best = 2000000000.0, ans = 0.0;

	while ( 1 ) {
		double tmp = c / cur;
		double to_end = x / cur;
		if ( ans + to_end < best ) best = ans + to_end;
		else break;

		ans += tmp;
		cur += f;
	}

	printf ( "Case #%d: %.7lf\n", test, best );

}

int main() {
	int tests;

	scanf ( "%d", &tests );

	for ( int i = 1; i <= tests; ++ i ) {
		read();
		solve( i );
	}

	return 0;

}