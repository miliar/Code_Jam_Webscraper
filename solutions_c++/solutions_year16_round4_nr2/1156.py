#include <algorithm>
#include <cstdio>
#include <cstring>
#define FOR(i,a,b) for(i=a; i<=b; i++)
#define FOR2(i,n) FOR(i,0,n-1)
#define TFOR(i,a,b) for(i=a; i>=b; i--)
#define f first
#define s second
#define all(x) x.begin(),x.end() 
#define MAXN 205
using namespace std;
typedef pair < int , int > pii;
int read(){ int res(0),sign(1); char c;
	while(1){ c = getchar(); if('0' <= c && c <= '9') { res = c - '0'; break; } else if(c == '-') { sign = -1; break; } }
	while(1){ c = getchar(); if('0' <= c && c <= '9') res = res*10 + c - '0'; else break; }
	return res * sign;
}
int K,N;
double A[MAXN] , P[MAXN];
double DP[MAXN][2*MAXN];
double dp(int x,int t) {

	double &ret = DP[x][t];
	if( ret ) return ret;

	if( x == K + 1 ) return ret = (t == K) ? 1.0 : 0.0;


	return ret = dp(x+1,t-1) * A[x] + dp(x+1,t+1) * ( 1 - A[x] );

}

double res;
int C[MAXN];

void rec(int x) {

	if( x == K + 1 ) {
		memset( DP , 0 , sizeof DP );
		res = max( res , dp(1,K) );

		return;
	}

	int i;
	FOR(i,C[x-1]+1,N)
	{
		C[x] = i;
		A[x] = P[i];
		rec(x+1);
	}

}

void solve() {

	N = read(); K = read();
	int i;
	FOR(i,1,N)
		scanf("%lf" , P+i );

	res = 0;
	rec(1);

	printf("%.8lf\n" , res );

}
int main()
{
	int T = read() , i ;
	FOR(i,1,T) {
		printf("Case #%d: " , i );
		solve();
	}
	return 0;
}
