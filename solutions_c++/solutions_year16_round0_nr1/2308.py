#include <cstdio>

long long calc( int N ) {
	if( N == 0 ) return 0;

	int digits = 0;
	long long n = N;
	while( true ) {
		for( long long x = n; x != 0; x /= 10 ) {
			digits |= 1<<(x%10);
		}
		if( digits == (1<<10)-1 ) return n;
		n += N;
	}
}

int main() {
	int cases;
	scanf( "%d", &cases );
	for( int c = 0; c < cases; ++c ) {
		printf( "Case #%d: ", c+1 );
		int N;
		scanf( "%d", &N );
		auto res = calc( N );
		if( res == 0 ) puts( "INSOMNIA" );
		else printf( "%lld\n", res );
	}
	return 0;
}
