#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#define FOR(i,a,b) for(i=a; i<=b; i++)
#define FOR2(i,n) FOR(i,0,n-1)
#define TFOR(i,a,b) for(i=a; i>=b; i--)
#define f first
#define s second
#define all(x) x.begin(),x.end() 
#define MAXN 50
using namespace std;
typedef pair < long long , long long > pii;
long long read(){ long long res(0),sign(1); char c;
	while(1){ c = getchar(); if('0' <= c && c <= '9') { res = c - '0'; break; } else if(c == '-') { sign = -1; break; } }
	while(1){ c = getchar(); if('0' <= c && c <= '9') res = res*10 + c - '0'; else break; }
	return res * sign;
}
long long N = 16;
long long K;


bool primeCheck( long long n ) {

	if( !(n&1) ) return false;

	for( long long i = 3; i * i <= n; i += 2 )
		if( !(n%i) )
			return false;
	return true;
}

long long firstDivisor( long long n ) {

	if( !(n&1) ) return 2;

	for( long long i = 3; i * i <= n; i += 2 )
		if( !(n%i) )
			return i;

	printf("This is fucked up!!!");
	exit(0);
}

long long convertToInt( vector < long long > A , long long base) {

	long long s(0),t(1);
	for( long long i = 0; i < N; i++ ) {
		s += t * A[i];
		t *= base;
	}

	return s;
}
int main()
{
	vector < long long > A;
	vector < pair < vector < long long > , vector < long long > > > V;

	for( int t = (1 << 15) + 1; t < ( 1 << 16 ); t += 2 ) {

		A.clear();
		A.resize(N);

		int tmp = t;

		for( long long i = 0; i < N; i++ , tmp >>= 1 )
			A[i] = tmp&1;

		long long k;
		for( k = 2; k <= 10; k++ )
			if( primeCheck( convertToInt(A,k) ) )
				break;

		if( k == 11 ) {

			vector < long long > B;

			for( long long k = 2; k <= 10; k++ )
				B.push_back( firstDivisor( convertToInt(A , k) ) );

			V.push_back( make_pair( A , B ) );

			if( ++K == 50 ) break;

		}

	}

	printf("Case #1:\n");

	for( auto it = V.begin(); it != V.end(); ++it ) {

		reverse( all(it->f) );

		for( auto it2 = it->f.begin(); it2 != it->f.end(); ++it2 )
			printf("%lld" , *it2 );

		for( auto it2 = it->s.begin(); it2 != it->s.end(); ++it2 )
			printf(" %lld" , *it2 );

		printf("\n");

	}


	return 0;
}
