#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<queue>
#include<map>
#include<set>
#include<string.h>
#include<time.h>
typedef long long lnt;
const lnt mod=1e9+7;
double a[210];
int in[210];
double ch[210],dp[210][210],max;
int n,m;
void dfs(int now,int num){
	int k,i;
	if(num==m){
		dp[0][0]=1;
		for(k=1;k<=m;k++){
			for(i=0;i<=k;i++){
				dp[k][i]=dp[k-1][i]*(1-ch[k]);
				if(i>0) dp[k][i]+=dp[k-1][i-1]*ch[k];
			}
		}
		if(dp[m][m/2]>max) max=dp[m][m/2];
		return;
	}
	if(now==n+1) return;
	ch[num+1]=a[now];
	dfs(now+1,num+1);
	dfs(now+1,num);
	return;
}
int main(){
	freopen("pB.in","r",stdin);
	freopen("pB.txt","w",stdout);
	int T,t=0,k,c,d,i,j;
	double p;
	scanf("%d",&T);
	while(T--){
		scanf("%d%d",&n,&m);
		t++;
		for(k=1;k<=n;k++) scanf("%lf",&a[k]);
		max=0;
		dfs(1,0);
		dp[0][0]=1;
		for(k=1;k<=m;k++){
			for(i=0;i<=k;i++){
				dp[k][i]=dp[k-1][i]*(1-ch[k]);
				if(i>0) dp[k][i]+=dp[k-1][i-1]*ch[k];
			}
		}
		printf("Case #%d: ",t);
		printf("%.10f\n",max);
	}
}
