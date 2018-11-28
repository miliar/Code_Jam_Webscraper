#include <stdio.h>
#include <string.h>

const long long mod=1000000007;

long long dp[105][20];
//0 initial 0
//1 row2 1 0
//2 tag3 2 3
//3 tag4 3 4
//4 tag6 2 6
//5 row3 2 0
//6 row2 1 3
//7 row2 1 4
//8 row2 1 6
//9 row2 1 12
//10tag3 2 6
//11tag3 2 12
//12tag4 3 12
//13tag6 2 12
//14row3 2 3
//15row3 2 4
//16row3 2 6
//17row3 2 12

int main()
{
	freopen("D-small-attempt1.in","r",stdin);
	freopen("pd1.out","w",stdout);
	int cas;
	int r,c;
	bool tag3,tag4,tag6;
	scanf("%d",&cas);
	for(int T=1; T<=cas; T++){
		scanf("%d %d",&r,&c);
		if(c%3==0) tag3=true; else tag3=false;
		if(c%4==0) tag4=true; else tag4=false;
		if(c%6==0) tag6=true; else tag6=false;
		memset(dp,0,sizeof(dp));
		dp[0][0]=1;
		for(int i=1; i<=r; i++){
			if(i>=1){
				dp[i][1]=(dp[i-1][0]+dp[i-1][5])%mod;
				dp[i][6]=(dp[i-1][14])%mod;
				dp[i][7]=(dp[i-1][15])%mod;
				dp[i][8]=(dp[i-1][16])%mod;
				dp[i][9]=(dp[i-1][17])%mod;
			}
			if(i>=2){
				if(tag3) dp[i][2]=(dp[i-2][0]+dp[i-2][5]+3*dp[i-2][14])%mod;
				if(tag3) dp[i][10]=(3*dp[i-2][16])%mod;
				if(tag3) dp[i][11]=(3*dp[i-2][15]+3*dp[i-2][17])%mod;
				if(tag6) dp[i][4]=(dp[i-2][0]+dp[i-2][5]+3*dp[i-2][14]+6*dp[i-2][16])%mod;
				if(tag6) dp[i][13]=(4*dp[i-2][15]+6*dp[i-2][17])%mod;
				dp[i][5]=(dp[i-2][0]+dp[i-2][1])%mod;
				dp[i][14]=(dp[i-2][2]+dp[i-2][6])%mod;
				dp[i][15]=(dp[i-2][3]+dp[i-2][7])%mod;
				dp[i][16]=(dp[i-2][4]+dp[i-2][8]+dp[i-2][10])%mod;
				dp[i][17]=(dp[i-2][9]+dp[i-2][11]+dp[i-2][12]+dp[i-2][13])%mod;
			}
			if(i>=3){
				if(tag4) dp[i][3]=(dp[i-3][0]+dp[i-3][5]+4*dp[i-3][15])%mod;
				if(tag4) dp[i][12]=(3*dp[i-3][14]+4*dp[i-3][16]+4*dp[i-3][17])%mod;
			}
		}
		long long ans=0;
		for(int i=0; i<18; i++){
			ans=(ans+dp[r][i])%mod;
		}
		printf("Case #%d: %I64d\n",T,ans);
	}
	return 0;
}
