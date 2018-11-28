#include<stdio.h>
#define INF 1000000000
int tab[2000];
int dp[2000][2000];
int main(){
	int t;
	for(int i = 1 ; i <= 1100 ; i++ ){
		for(int j = i+1 ; j <= 1100 ; j++ ){
			dp[i][j] = INF ;
			for(int k = 1 ; k < j ; k++ ){
				if( dp[i][k]+dp[i][j-k]+1 < dp[i][j] )
					dp[i][j] = dp[i][k]+dp[i][j-k]+1;
			}
		}
	}
	scanf("%d",&t);
	for(int e = 0 ; e < t ; e++ ){
		int n;
		scanf("%d",&n);
		for(int i = 0 ; i < n ; i++ ){
			scanf("%d",&tab[i]);
		}
		int ans = INF ;
		for(int rem = 1 ; rem <=1000 ; rem++ ){
			int sum = 0;
			for(int i = 0 ; i < n ; i++ ){
				sum += dp[rem][tab[i]];
			}
			if( sum+rem < ans ) ans = sum+rem;
		}
		printf("Case #%d: %d\n",e+1,ans);
	}
}
