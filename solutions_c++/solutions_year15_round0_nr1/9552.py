#include <cstdio>
#include <iostream>

using namespace std;

const int MAXN = 1024;

int n;
char s[MAXN];

void read() {
	scanf ( "%d", &n );

	scanf ( "%s", s );

}

void solve ( int test ) {
	int i, cur = s[0] - '0', ans = 0;

	for ( i = 1; i <= n; ++ i ) {
		if ( i <= cur ) cur += s[i] - '0';
		else {
			ans += i - cur;
			cur = i + ( s[i] - '0' );
		}
	}

	printf ( "Case #%d: %d\n", test, ans );

}

int main() {
	freopen ( "A-large.in" , "r", stdin );
    freopen ( "a.out", "w", stdout );

	int test;

	scanf ( "%d", &test );

	for ( int i = 1; i <= test; ++ i ) {
		read();
		solve(i);
	}

	return 0;

}