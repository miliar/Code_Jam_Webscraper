#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cassert>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <cmath>


using namespace std;

long long int powers[51];

bool meglio ( int n, long long int k, long long int p ) {
	// al caso ottimo, la squadra k arriva nelle prime p posizioni?
	
	if ( n == 0 ) {
		assert (k == 0);
		
		if ( p == 0 ) return false;
		if ( p >= 1 ) return true;
		
	}
	
	if ( k == powers[n]-1 ) {
		if ( p >= powers[n] ) return true;
		else return false;
	}
	
	bool risposta = meglio ( n-1, (k+1)/2, p );
	//printf("Meglio (%d,%lld,%lld): %d\n", n,k,p,risposta);
	return risposta;
}

bool peggio ( int n, long long int k, long long int p ) {
	
	if ( n == 0 ) {
		return meglio(n,k,p);
	}
	
	if ( k == 0 ) {
		if ( p == 0 ) return false;
		else return true;
	}
	
	return peggio ( n-1, (k-1)/2, max( (long long int)0 , p - powers[n-1] ) );
}

long long int ricerca ( int n, long long int p, long long int inizio, long long int fine, int quale ) {
	if ( inizio == fine ) return inizio;
	
	long long int m = (inizio+fine+1)/2;
	bool condizione;
	if ( quale == 0 ) {
		// peggio
		condizione = peggio( n, m, p );
	}
	else {
		// meglio
		condizione = meglio( n, m, p );
	}
	
	if ( condizione ) {
		return ricerca( n, p, m, fine, quale );
	}
	else return ricerca( n, p, inizio, m-1, quale );
}

void solve() {
	
	int n;
	long long int p;
	scanf("%d %lld\n",&n,&p);
	
	printf("%lld %lld\n", ricerca( n, p, 0, powers[n]-1, 0 ), ricerca( n, p, 0, powers[n]-1, 1 ));
}

int main() {
	
	powers[0] = 1;
	for (int i=1; i<=50; ++i) {
		powers[i] = powers[i-1] * 2;
	}
	
	int t;
	scanf("%d",&t);
	
	for (int i=0; i<t; ++i) {
		printf("Case #%d: ",i+1);
		solve();
	}
	
	return 0;
}
