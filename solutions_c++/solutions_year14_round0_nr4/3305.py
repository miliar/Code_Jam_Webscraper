#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

const int MAXN = 1024;

int n;
double a[MAXN], b[MAXN];
bool u[MAXN];

void read() {
	int i;

	scanf ( "%d", &n );

	for ( i = 0; i < n; ++ i ) {
		scanf ( "%lf", &a[i] );
	}

	for ( i = 0; i < n; ++ i ) {
		scanf ( "%lf", &b[i] );
	}

}

int cmp ( double x, double y ) {
	if ( x >= y ) return 1;
	return 0;

}

void solve( int test ) {
	int i, j, k, k1;

	memset ( u, 0, sizeof u );

	sort ( a, a + n, cmp );
	sort ( b, b + n, cmp );

	int ans1 = 0, ans2 = 0;

	for ( i = n - 1; i >= 0; -- i ) {
		bool ok = 1;
		for ( j = n - 1; j >= 0; -- j ) {	
			if ( !u[j] && b[j] > a[i] ) {
				ok = 0;
				u[j] = 1;
				break;
			}
		}

		if ( ok ) ans2 ++;

	}


	for ( i = 0, j = n - 1; i < n; ++ i, -- j ) {
		int br = 0;
		for ( k = i, k1 = 0; k < n; ++ k, ++ k1 ) {
			if ( a[k1] > b[k] ) br ++;
		}
		ans1 = max ( br, ans1 );

	}

	printf ( "Case #%d: %d %d\n", test, ans1, ans2 );

}

int main() {
	int i, tests;

	scanf ( "%d", &tests );

	for ( i = 1; i <= tests; ++ i ) {
		read();
		solve( i );
	}

	return 0;

}