#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#define FOR(i,a,b) for(i=a; i<=b; i++)
#define FOR2(i,n) FOR(i,0,n-1)
#define TFOR(i,a,b) for(i=a; i>=b; i--)
#define f first
#define s second
#define pb push_back
#define all(x) x.begin(),x.end()
#define MAXK 6
#define MAXN 10005
#define MAXT 262145
#define MOD 1000000007ll
#define MOD2 ( MOD * MOD )
using namespace std;
typedef pair < int , int > pii;
int read(){ int res(0),sign(1); char c;
	while(1){ c = getchar(); if('0' <= c && c <= '9') { res = c - '0'; break; } else if(c == '-') { sign = -1; break; } }
	while(1){ c = getchar(); if('0' <= c && c <= '9') res = res*10 + c - '0'; else break; }
}
char calc(int a,int b)
{
	int sign = 1;
	if( a < 0 ) sign *= -1 , a = -a;
	if( b < 0 ) sign *= -1 , b = -b;
	if( a == 1 && b == 1 ) return sign * 1;
	if( a == 1 && b == 2 ) return sign * 2;
	if( a == 1 && b == 3 ) return sign * 3;
	if( a == 1 && b == 4 ) return sign * 4;
	if( a == 2 && b == 1 ) return sign * 2;
	if( a == 2 && b == 2 ) return sign * -1;
	if( a == 2 && b == 3 ) return sign * 4;
	if( a == 2 && b == 4 ) return sign * -3;
	if( a == 3 && b == 1 ) return sign * 3;
	if( a == 3 && b == 2 ) return sign * -4;
	if( a == 3 && b == 3 ) return sign * -1;
	if( a == 3 && b == 4 ) return sign * 2;
	if( a == 4 && b == 1 ) return sign * 4;
	if( a == 4 && b == 2 ) return sign * 3;
	if( a == 4 && b == 3 ) return sign * -2;
	if( a == 4 && b == 4 ) return sign * -1;
}
char f(char c)
{
	if( c == '1' ) return 1;
	if( c == 'i' ) return 2;
	if( c == 'j' ) return 3;
	if( c == 'k' ) return 4;
}
char A[MAXN];
char D[MAXN][MAXN];
void solve()
{
	int L,N,X,i,j;
	scanf("%d %d" , &L , &X );
	scanf("%s" , A+1 );
	N = L * X;
	FOR(i,L+1,N)
		A[i] =  A[i-L];
	
	
	FOR(i,1,N)
	{
		D[i][i] = f(A[i]);
		FOR(j,i+1,N)
			D[i][j] = calc( D[i][j-1] , f( A[j] ) );
	}
	
	FOR(i,1,N)
		if( D[1][i] == 2 )
			FOR(j,i+2,N)
				if( D[j][N] == 4 && D[i+1][j-1] == 3 )
				{
					printf("YES\n");
					return;
				}
				
	printf("NO\n");
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,i;
	scanf("%d" , &T );
	FOR(i,1,T)
	{
		printf("Case #%d: " , i );
		solve();
	}
	return 0;
}
