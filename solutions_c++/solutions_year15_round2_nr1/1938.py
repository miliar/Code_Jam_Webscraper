#include <bits/stdc++.h>
using namespace std;
#define INF 1000000000

int dp[1000005];

int reverse(int n){
	int ret = 0;
	while(n>0){
		ret*=10;
		ret+=n%10;
		n/=10;
	}
	return ret;
}

int main(){
	int rev;

	for(int i=0; i<=1000000; i++)
		dp[i]=INF;
	
	dp[1]=1;

	for(int i=2; i<=1000000; i++){
		rev = reverse(i);
		if(rev < i && i%10 !=0)
			dp[i] = min(dp[i-1],dp[rev])+1;
		else
			dp[i] = dp[i-1]+1;
	}

	int zz,temp;
	cin>>zz;
	for(int tc = 1; tc<=zz; tc++){
		cin>>temp;
		printf("Case #%d: %d\n",tc,dp[temp]);
	}
}