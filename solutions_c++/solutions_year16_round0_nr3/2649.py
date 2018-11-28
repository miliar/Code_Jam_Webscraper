/*
 *
 */
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#define N (1<<23)
typedef long long i64;
using namespace std;

bool isprime[N];
int m;
i64 *p;

void sieve() {
	i64 i,j,k;
	for ( i = 3; i < N; isprime[i] = true, i += 2 );
	for ( isprime[2] = true, i = 3; i < N; i += 2 )
		if ( isprime[i] )
			for ( j = i+i; j < N; isprime[j] = false, j += i );
	for ( i = 0; i < N; ++i )
		if ( isprime[i] ) ++m;
	p = new i64[m];
	for ( k = 0, i = 0; i < N; ++i )
		if ( isprime[i] )
			p[k++] = i;
	assert( m == k );
};

bool is_prime( i64 n, i64 &d ) {
	for ( int i = 0; i < m && p[i]*p[i] <= n; ++i )
		if ( 0 == (n%p[i]) ) {
			d = p[i];
			return false ;
		}
	return true ;
};

int main() {
	int i,j,k,cn,cur,len,n,cs = 0,ts;
	unsigned long long u,v,w;
	i64 base,d[11];
	sieve();
	for ( scanf("%d",&ts); ts--; ) {
		printf("Case #%d:\n",++cs);
	scanf("%d %d",&n,&cn), cur = 0;
	for ( u = 0; u < (1ULL<<(n-2)) && cur < cn; ++u ) {
		v = 1|(u<<1)|(1ULL<<(n-1));
		bool ok = true ;
		for ( base = 2; base <= 10 && ok; ++base ) {
			for ( w = 0, i = n-1; i >= 0; --i )
				w = base*w + ((v>>i)&1);
			if ( is_prime(w,d[base]) ) ok = false;
		}
		if ( !ok ) continue ;
		for ( i = n-1; i >= 0; --i )
			putchar(((v>>i)&1)+'0');
		for ( i = 2; i <= 10; ++i )
			printf(" %lld",d[i]);
		puts(""); ++cur;
	}
	}
	return 0;
};

