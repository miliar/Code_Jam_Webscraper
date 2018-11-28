#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

const int MAXN = 1024;

int a, b, c;

void solve( int test ) {
	int i, j;

	int cnt = 0;
	for ( i = 0; i < a; ++ i ) {
		for ( j = 0; j < b; ++ j ) {
			if ( ( i & j ) < c ) cnt ++;
		}
	}

	printf ( "Case #%d: %d\n", test, cnt );

}

int main() {
	int i, tests;

	scanf ( "%d", &tests );

	for ( i = 0; i < tests; ++ i ) {
		scanf ( "%d %d %d", &a, &b, &c );
		solve ( i + 1 );
	}

	return 0;

}