#include<stdio.h>
#include<algorithm>
using namespace std;
int dp[120][1200][2];
int h[120];
int g[120];
int main(){
	int T;
	scanf("%d",&T);
	for(int t=0;t<T;t++){
		int p,q,a;
		scanf("%d%d%d",&p,&q,&a);
		for(int i=0;i<a;i++){
			scanf("%d%d",h+i,g+i);
		}
		for(int i=0;i<=a+1;i++)
			for(int j=0;j<1200;j++)
				dp[i][j][0]=dp[i][j][1]=-999999999;
		dp[0][0][0]=0;
		for(int i=0;i<a;i++){
			for(int j=0;j<1200;j++){
				if(dp[i][j][0]>=0){
					// hosii!!
			//		printf("%d %d %d: %d\n",i,j,0,dp[i][j][0]);
					int t1=(h[i]+p-1)/p;
					int v=0;
					int count=0;
					while(v<h[i]){
						int u=(h[i]-v+p-1)/p;
						t1=min(t1,u-count-1);
						v+=q;
						count++;
					}
					if(t1<999&&j>=t1&&j-t1<1200){
						dp[i+1][j-t1][1]=max(dp[i+1][j-t1][1],dp[i][j][0]+g[i]);
					}
					// iranai..
					int t2=(h[i]+q-1)/q;
					if(j+t2<1200)dp[i+1][j+t2][0]=max(dp[i+1][j+t2][0],dp[i][j][0]);
				}
				if(dp[i][j][1]>=0){
				//	printf("%d %d %d: %d\n",i,j,1,dp[i][j][1]);
					int t1=(h[i]+p-1)/p;
					int v=q;
					int count=0;
					while(v<h[i]){
						int u=(h[i]-v+p-1)/p;
						t1=min(t1,u-count-1);
						v+=q;
						count++;
					}
					if(t1<999&&j>=t1&&j-t1<1200){
						dp[i+1][j-t1][1]=max(dp[i+1][j-t1][1],dp[i][j][1]+g[i]);
					}
					int t2=(h[i]+q-1)/q-1;
					if(j+t2<1200)dp[i+1][j+t2][0]=max(dp[i+1][j+t2][0],dp[i][j][1]);
				}
			}
		}
		int ret=0;
		for(int i=0;i<1200;i++)ret=max(ret,max(dp[a][i][0],dp[a][i][1]));
		printf("Case #%d: %d\n",t+1,ret);
	}
}