#include <algorithm>
#include <cstdio>
#include <cstring>
#define FOR(i,a,b) for(i=a; i<=b; i++)
#define FOR2(i,n) FOR(i,0,n-1)
#define TFOR(i,a,b) for(i=a; i>=b; i--)
#define f first
#define s second
#define pb push_back
#define all(x) x.begin(),x.end() 
#define MAXN 100005
using namespace std;
typedef pair < int , int > pii;
int read(){ int res(0),sign(1); char c;
	while(1){ c = getchar(); if('0' <= c && c <= '9') { res = c - '0'; break; } else if(c == '-') { sign = -1; break; } }
	while(1){ c = getchar(); if('0' <= c && c <= '9') res = res*10 + c - '0'; else break; }
	return res * sign;
}
int A[MAXN];
void solve()
{
	int N = read() , i,maxi(0),s1(0),s2(0);
	FOR(i,1,N)
	{
		A[i] = read();
		if( A[i] < A[i-1] )
		{
			s1 += A[i-1] - A[i];
			maxi = max( maxi , A[i-1] - A[i] );
		}
	}

	FOR(i,1,N-1)
			s2 += min( A[i] , maxi );



	printf("%d %d\n" , s1 , s2 );


}
int main()
{
	int T = read() , i;
	FOR(i,1,T)
	{
		printf("Case #%d: " , i );
		solve();
	}
	return 0;
}
