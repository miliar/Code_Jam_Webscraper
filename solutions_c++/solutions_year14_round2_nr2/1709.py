#include <algorithm>
#include <cstdio>
#include <cstring>
#define FOR(i,a,b) for(i=a; i<=b; i++)
#define FOR2(i,n) FOR(i,0,n-1)
#define TFOR(i,a,b) for(i=a; i>=b; i--)
#define f first
#define s second
#define all(x) x.begin(),x.end()
#define MAXN 
using namespace std;
void solve()
{
	int a,b,i,j,k,res(0);
	scanf("%d %d %d" , &a , &b , &k );
	for(i = 0; i < a; i++)
		for(j = 0; j < b; j++)
			res += ( (i&j) < k );

	printf("%d\n" , res );
}
int main()
{
	freopen("inp","r",stdin);
	freopen("out.txt","w",stdout);
	int T,i;
	scanf("%d" , &T );
	FOR(i,1,T)
	{
		printf("Case #%d: " , i );
		solve();
	}
	return 0;
}
