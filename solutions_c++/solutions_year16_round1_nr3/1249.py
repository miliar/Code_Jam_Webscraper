#include <algorithm>
#include <cstdio>
#include <cstring>
#define FOR(i,a,b) for(i=a; i<=b; i++)
#define FOR2(i,n) FOR(i,0,n-1)
#define TFOR(i,a,b) for(i=a; i>=b; i--)
#define f first
#define s second
#define all(x) x.begin(),x.end() 
#define MAXN 10005
using namespace std;
typedef pair < int , int > pii;
int read(){ int res(0),sign(1); char c;
	while(1){ c = getchar(); if('0' <= c && c <= '9') { res = c - '0'; break; } else if(c == '-') { sign = -1; break; } }
	while(1){ c = getchar(); if('0' <= c && c <= '9') res = res*10 + c - '0'; else break; }
	return res * sign;
}
int N;
int A[MAXN] , D[MAXN] , H[MAXN];

bool _try(int x,int n) {

	if( x == n + 1 ) {
		
		int i;
		D[0] = D[n];
		D[n+1] = D[1];


		FOR(i,1,n)
			if( D[i-1] != A[ D[i] ] && D[i+1] != A[ D[i] ] )
				return false;

		return true;

	}
	int i;
	FOR(i,1,N)
		if( !H[i] ) {

			H[i] = true;
			D[x] = i;
			if( _try(x+1,n) )
				return true;
			H[i] = false;

		}

	return false;


}

int solve() {

	int i;
	N = read();
	FOR(i,1,N) A[i] = read();

	TFOR(i,N,1) {
		memset( H , 0 , sizeof H );
		if( _try(1,i) )
			return i;
	}

	return 0;
}
int main()
{
	freopen( "input.txt" , "r" , stdin );
	freopen( "output.txt" , "w" , stdout );

	int T = read() , i;

	FOR(i,1,T)
		printf("Case #%d: %d\n" , i , solve() );

	return 0;
}
