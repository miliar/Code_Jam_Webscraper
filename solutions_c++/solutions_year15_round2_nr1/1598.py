#include <bits/stdc++.h>

#define REP(i,n) for(i=0;i<n;i++)
#define FOR(i,a,b) for(i=a;i<=b;i++)
#define DEC(i,a,b) for(i=a;i>=b;i--)
#define SKIP(i,a,b,k) for(i=a;i<=b;i+=k)
#define DEBUG printf("ok\n")
#define NL printf("\n")

#define MIN(a,b) (a<b?a:b)
#define MAX(a,b) (a>b?a:b)
#define SQR(x) (x)*(x)
#define MOD(a,b) ((a)%(b)+b)%(b)

#define N 1000000
#define inf 2000000000

typedef long long ll;
typedef double db;

using namespace std;

int dp[N+10];

void solve(int T)
{
	int n;
	scanf("%d",&n);
	printf("Case #%d: %d\n",T,dp[n]);
}

int main()
{
	freopen("A-small-attempt0.in","r",stdin); freopen("1.out","w",stdout);
	int T;
	int i,num,r;
	FOR(i,1,N){
		num=i; r=0;
		while(num>0){
			r=10*r+num%10;
			num/=10;
		}
		if(r>=i||i%10==0) dp[i]=1+dp[i-1];
		else dp[i]=MIN(dp[i-1],dp[r])+1;
	}
	scanf("%d",&T);
	REP(i,T) solve(i+1);
	return 0;
}