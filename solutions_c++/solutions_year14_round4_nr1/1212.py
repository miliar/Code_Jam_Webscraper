#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#define FOR(i,a,b) for(i=a; i<=b; i++)
#define FOR2(i,n) FOR(i,0,n-1)
#define TFOR(i,a,b) for(i=a; i>=b; i--)
#define f first
#define s second
#define all(x) x.begin(),x.end()
#define MAXN 10005
using namespace std;
typedef pair < int , int > pii;
int A[MAXN] , B[MAXN];
int N,X;
void solve()
{
	int N,i;
	scanf("%d %d" , &N , &X );
	FOR(i,1,N)
		scanf("%d" , A+i );

	sort( A+1,A+N+1 );

	int k = N , res(0);
	FOR(i,1,N)
	{
		if(i == k) { res++; break; }
		while( k > i && A[k] + A[i] > X ) res++,k--;
		res++;
		k--;
		if( k <= i ) break;
	}

	printf("%d\n" , res );

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
