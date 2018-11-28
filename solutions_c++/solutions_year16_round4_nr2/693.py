#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cstdlib>

using namespace std;
#define rep(i,a,b) for (int i=(a);i<=(b);i++)
#define repd(i,a,b) for (int i=(a);i>=(b);i--)

typedef long long ll;
typedef unsigned long long ull;

const int inf=~0u>>1;
const int maxn=220;
double dp[maxn][maxn];
int n,k;
double p[maxn];
double pp[maxn];
double ans;

void dfs(int now,int num) {
	if (num==k) {
		rep(i,0,n) rep(j,0,n) dp[i][j]=0;
		dp[0][0]=1;
		rep(i,1,k) rep(j,0,i) {
			if (j==0) dp[i][j]=dp[i-1][j]*(1-pp[i]);
			else dp[i][j]=dp[i-1][j-1]*pp[i]+dp[i-1][j]*(1-pp[i]);
		}
		if (ans<dp[k][k/2])
			ans=dp[k][k/2];
		return;
	}
	if (now>n) return;
	dfs(now+1,num);
	pp[num+1]=p[now];
	dfs(now+1,num+1);
}

double work() {
	rep(i,0,n) rep(j,0,n) dp[i][j]=0;
	dp[0][0]=1;
	rep(i,1,k) rep(j,0,i) {
		if (j==0) dp[i][j]=dp[i-1][j]*(1-pp[i]);
		else dp[i][j]=dp[i-1][j-1]*pp[i]+dp[i-1][j]*(1-pp[i]);
	}
	return dp[k][k/2];
}

int main() {
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int T;scanf("%d\n",&T);
	rep(t,1,T) {
		printf("Case #%d: ",t);
		scanf("%d%d\n",&n,&k);
		rep(i,1,n) {
			scanf("%lf",&p[i]);
		}
		sort(p+1,p+n+1);
		ans=0;
		rep(len,0,k) {
			int tt=0;
			memset(pp,0,sizeof pp);
			rep(i,1,len) pp[++tt]=p[i];
			rep(i,1,k-len) pp[++tt]=p[n-i+1];
			ans=max(ans,work());
		}
		printf("%.8f\n",ans);
	}
	return 0;
}
