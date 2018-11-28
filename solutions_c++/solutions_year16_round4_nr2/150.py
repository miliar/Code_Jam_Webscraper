#include<stdio.h>
#include<algorithm>
#include<vector>
using namespace std;
double p[210];
double dp[210][210];
double calc(vector<double>v){
	int n=v.size();
	for(int i=0;i<=n;i++)for(int j=0;j<=n;j++)dp[i][j]=0;
	dp[0][0]=1;
	for(int i=0;i<n;i++){
		for(int j=0;j<=i;j++){
			dp[i+1][j+1]+=dp[i][j]*v[i];
			dp[i+1][j]+=dp[i][j]*(1.0-v[i]);
		}
	}
	return dp[n][n/2];
}
int main(){
	int T;scanf("%d",&T);
	for(int t=1;t<=T;t++){
		int a,b;scanf("%d%d",&a,&b);
		for(int i=0;i<a;i++){
			scanf("%lf",p+i);
		}
		std::sort(p,p+a);
		double ret=0;
		for(int i=0;i<=a-b;i++){
			vector<double>v;
			for(int j=0;j<b;j++)v.push_back(p[i+j]);
			ret=max(ret,calc(v));
		}
		for(int i=1;i<b;i++){
			vector<double>v;
			for(int j=0;j<i;j++)v.push_back(p[j]);
			for(int j=0;j<b-i;j++)v.push_back(p[a-1-j]);
			ret=max(ret,calc(v));
		}
		printf("Case #%d: %.12f\n",t,ret);
	}
}