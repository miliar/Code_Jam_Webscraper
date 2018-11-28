#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
const int MAXN = 100 + 10;

char s[MAXN];
int st[MAXN];
int len;

bool check() {
	for( int i = 0; i < len; ++i ) if( !st[i] ) return false;
	return true;
}

int main() {
	freopen( "B.out", "w+", stdout );
	int t, cnt, pos;
	scanf( "%d", &t );
	for( int ncas = 1; ncas <= t; ++ncas ) {
		printf( "Case #%d: ", ncas );
		scanf( "%s", s );
		cnt = 0; pos = 0;
		len = strlen( s );
		if( s[0] == '-' ) ++cnt;
		while( pos < len ) {
			while( pos < len ) {
				if( s[pos] == '+' ) break;
				++pos;
			}
			while( pos < len ) {
				if( s[pos] == '-' ) { cnt += 2; break; }
				++pos;
			}
		}
		printf( "%d\n", cnt );
	}
	return 0;
}
