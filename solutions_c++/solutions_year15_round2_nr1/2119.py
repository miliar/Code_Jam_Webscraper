#include <cstdio>
#define min(a,b) ((a)<(b)?(a):(b))
int r(int n){
	int s=0;
	while(n){
		s=s*10+n%10;
		n/=10;
	}
	return s;
}

int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		int n;
		scanf("%d",&n);
		int dp[n+1];
		dp[1]=1;
		for(int i=2;i<=n;i++){
			dp[i]=r(i)<i&&i%10?min(dp[i-1]+1,dp[r(i)]+1):dp[i-1]+1;
		}
		printf("Case #%d: %d\n",t,dp[n]);
	}
	return 0;
}
