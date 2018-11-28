#include<bits/stdc++.h>
#define N 210
using namespace std;
double p[N];
double dp[N][N];
bool chk[N][N];
double cal(int n,int m){
	if(m<0||m>n) return 0;
	if(chk[n][m]) return dp[n][m];
	chk[n][m]=true;
	return dp[n][m]=p[n-1]*cal(n-1,m-1)+(1-p[n-1])*cal(n-1,m);
}
int main(){
	double a[N];
	int T;
	scanf("%d",&T);
	for(int cs=1;cs<=T;cs++){
		int n,k;
		double ans=0;
		scanf("%d%d",&n,&k);
		for(int i=0;i<n;i++){
			scanf("%lf",&a[i]);
		}
		sort(a,a+n);
		for(int i=0;i<=k;i++){
			for(int j=0;j<i;j++){
				p[j]=a[j];
			}
			for(int j=0;j<k-i;j++){
				p[i+j]=a[n-1-j];
			}
			memset(chk,0,sizeof(chk));
			chk[0][0]=true;
			dp[0][0]=1;
			ans=max(ans,cal(k,k/2));
		}
		printf("Case #%d: %.8f\n",cs,ans);
	}
	return 0;
}