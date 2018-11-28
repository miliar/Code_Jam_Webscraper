#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
typedef long long LL;

LL a[20];
char s[20];
int n, j;

LL isP( LL x ) {
	for( LL i = 2; i * i <= x; ++i ) if( x % i == 0 ) return i;
	return -1;
}

LL convert( LL x, int b ) {
	LL ret = 1;
	for( int i = n - 3; i >= 0; --i ) {
		ret = ret * b + ( ( x & ( 1 << i ) ) ? 1 : 0 );
	}
	ret = ret * b + 1;
	return ret;
}

void print( LL x ) {	
	int len = 0;
	while( x ) {
		s[len++] = x % 2 + '0';
		x /= 2;
	}
	for( int i = len; i < n - 2; ++i ) s[i] = '0';
	reverse( s, s + n - 2 );
	printf( "1%s1", s );
	return ;
}

int main() {
	freopen( "C.out", "w+", stdout );
	int t, cnt;
	scanf( "%d", &t );
	for( int ncas = 1; ncas <= t; ++ncas ) {
		cnt = 0;
		printf( "Case #%d:\n", ncas );
		scanf( "%d%d", &n, &j );
		for( int s = 1; s < ( 1 << ( n - 2 ) ); ++s ) {
			bool flag = true;
			for( int i = 2; i <= 10; ++i ) {
				LL tmp = convert( s, i );
				if( ( a[i] = isP( tmp ) ) == -1 ) { flag = false; break; }
			}
			if( flag ) {
				print( s );
				for( int i = 2; i <= 10; ++i ) printf( " %lld", a[i] );
				puts( "" );
				++cnt;
			}
			if( cnt >= j ) break;
		}
	}
	return 0;
}
