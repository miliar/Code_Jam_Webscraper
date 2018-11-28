#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int n, c, k;

int main() {
	freopen( "D.out", "w+", stdout );
	int t;
	scanf( "%d", &t );
	for( int ncas = 1; ncas <= t; ++ncas ) {
		printf( "Case #%d:", ncas );
		scanf( "%d%d%d", &n, &c, &k );
		for( int i = 1; i <= k; ++i ) printf( " %d", i );
		puts( "" );
	}
	return 0;
}
