#include<stdio.h>
#include<algorithm>
using namespace std;
int mod=1000000007;
long long modpow(long long a,long long b){
	long long ret=1;
	while(b){
		if(b%2)ret=ret*a%mod;
		a=a*a%mod;
		b/=2;
	}
	return ret;
}
int gcd(int a,int b){
	while(a){
		b%=a;
		int c=a;a=b;b=c;
	}
	return b;
}
long long dp[15][15][15][15];
int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		int a,b;
		scanf("%d%d",&a,&b);
		printf("Case #%d: ",t);
		for(int i=0;i<10;i++)for(int j=0;j<10;j++)for(int k=0;k<10;k++)
			for(int l=0;l<10;l++)dp[i][j][k][l]=0;
		dp[2][0][0][0]=1;
		dp[3][0][0][0]=1;
		dp[4][1][0][0]=1;
		dp[4][0][1][0]=1;
		dp[5][0][0][1]=1;
		for(int i=2;i<a;i++){
			for(int j=0;j<a;j++){
				for(int k=0;k<a;k++)for(int l=0;l<a;l++){
					if(!dp[i][j][k][l])continue;
					dp[i+3][j][k][l]=(dp[i+3][j][k][l]+dp[i][j][k][l])%mod;
					dp[i+4][j+1][k][l]=(dp[i+4][j+1][k][l]+dp[i][j][k][l])%mod;
					dp[i+4][j][k+1][l]=(dp[i+4][j][k+1][l]+dp[i][j][k][l])%mod;
					dp[i+5][j][k][l+1]=(dp[i+5][j][k][l+1]+dp[i][j][k][l])%mod;
				}
			}
		}
		
		long long ret=(dp[a][0][0][0]+dp[a+2][0][0][0])%mod;
		if(b%3==0){
			for(int i=1;i<a;i++)ret=(ret+(dp[a][i][0][0]+dp[a+2][i][0][0])%mod*modpow(3,i-1))%mod;
			if(b%6==0){
				for(int i=1;i<a;i++)for(int j=0;j<a;j++){
					ret=(ret+(dp[a][j][i][0]+dp[a+2][j][i][0])%mod*modpow(6,i-1)%mod*modpow(3,j))%mod;
				}
			}
		}
		if(b%4==0){
			for(int i=1;i<a;i++)ret=(ret+(dp[a][0][0][i]+dp[a+2][0][0][i])%mod*modpow(5,i-1))%mod;
		}
		printf("%lld\n",ret);
	}
}