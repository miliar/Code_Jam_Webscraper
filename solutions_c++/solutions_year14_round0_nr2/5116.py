#include <algorithm>
#include <iostream>
#include <cstdio>

using namespace std;

const long double BASE = 1000;

int main ( void )
{
	int T;
	cin >> T;
	
	for ( int t = 1; t <= T; ++t ) {
		long double c, f, x, cps = 2, ans, now = 0;
		cin >> c >> f >> x;

		cps /= BASE;
		f /= BASE;
		ans = x / cps;

		for ( int i = 0; i < BASE * BASE * 10; ++i ) {
			now += c / cps;
			cps += f;
			ans = min( ans, now + x / cps );
		}

		printf( "Case #%d: %.7Lf\n", t, ans / 1000 );
	}
	return 0;
};
