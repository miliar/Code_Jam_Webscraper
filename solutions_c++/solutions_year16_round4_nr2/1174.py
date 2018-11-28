#include<stdio.h>
#include<algorithm>
#include<iostream>
double ans[300];
double dp[300][600],max;
double a[300];
int k;
void DO(){
	int i,j;
	dp[0][300] = 1;
	for(i=0;i<k;i++){
		for(j=0;j<600;j++)dp[i+1][j]=0;
		for(j=0;j<600;j++){
			if(dp[i][j]){
				dp[i+1][j+1] += dp[i][j]*ans[i];
				dp[i+1][j-1] += dp[i][j]*(1-ans[i]);
			}
		}
	}
	if(dp[k][300]>max) max = dp[k][300];
}
void getall(int x,int n,int k){
	if(k==0){
		DO();
		return;
	}
	else if(n==x) return;
	ans[k-1] = a[x];
	getall(x+1,n,k-1);
	getall(x+1,n,k);
}
int main(){
	int T,t,n,l,j,x,i,kk;

	scanf("%d",&T);
	for(t=1;t<=T;t++){
		scanf("%d%d",&n,&k);
		for(i=0;i<n;i++)scanf("%lf",&a[i]);
		//std::sort(a,a+n);
		max = 0;
		getall(0,n,k);
		printf("Case #%d: %.6lf\n",t,max);
	}
}
