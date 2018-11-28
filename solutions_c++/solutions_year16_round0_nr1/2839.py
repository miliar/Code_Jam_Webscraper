#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
typedef long long LL;
const LL INF = ( LL )1e18;

int flag[10], tflag[10], sum;
LL n;

bool check( LL tn ) {
	while( tn ) {
		int tmp = tn % 10;
		tflag[tmp] = 1;
		sum += ( tflag[tmp] ^ flag[tmp] );
		flag[tmp] = tflag[tmp];
		tn /= 10;
	}
	if( sum == 10 ) return true;
	return false;
}

int main() {
	int t;
	freopen( "A.out", "w+", stdout );
	scanf( "%d", &t );
	for( int ncas = 1; ncas <= t; ++ncas ) {
		memset( flag, 0, sizeof( flag ) );
		sum = 0;
		scanf( "%lld", &n );
		printf( "Case #%d: ", ncas );
		if( n == 0 ) { puts( "INSOMNIA" ); continue; }
		LL tn = n;
		while( tn <= INF ) {
			if( check( tn ) ) break;
			tn += n;
		}
		printf( "%lld\n", tn );
	}
	return 0;
}
