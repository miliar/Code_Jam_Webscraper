#include <cstdio>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <vector>

using namespace std;

char S[2010];
string res;

void f( int to ) {
	int p = 0;
	int cnt = 1;
	for( int i = 1; i <= to; ++i ) {
		if( S[i] > S[p] ) {
			p = i;
			cnt = 1;
		}
		else if( S[i] == S[p] ) ++cnt;
	}
	if( p != 0 ) {
		f( p-1 );
	}
	for( int i = p+1; i <= to; ++i ) {
		if( S[i] != S[p] ) res += S[i];
	}
	res = string(cnt,S[p]) + res;
}

int main() {
	int T;
	scanf( "%d", &T );

	for( int t = 0; t < T; ++t ) {
		printf( "Case #%d: ", t+1 );
		scanf( "%s", S );
		int n = strlen( S );
		assert( 1 <= n && n <= 1000 );
		for( int i = 0; i < n; ++i ) {
			assert( 'A' <= S[i] && S[i] <= 'Z' );
		}
		res.clear();
		f( n-1 );
		printf( "%s\n", res.c_str() );
	}
	return 0;	
}
