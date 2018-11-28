#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
const int mxn = 100 + 10;
int dp[mxn][2];

int main(){
	int tcase;
	cin >> tcase;
	for(int casei=1;casei<=tcase;casei++){
		string in;
		cin >> in;
		memset(dp,0,sizeof(dp));
		if(in[0] == '-'){
			dp[0][0] = 0;
			dp[0][1] = 1;
		}else{
			dp[0][0] = 1;
			dp[0][1] = 0;
		}
		for(int i=1;i<in.length();i++){
			if(in[i] == '-'){
				dp[i][0] = min(dp[i-1][0],dp[i-1][1]+1);
				dp[i][1] = min(dp[i-1][1]+2,dp[i-1][0]+1);
			}else{
				dp[i][0] = min(dp[i-1][1]+1,dp[i-1][0]+2);
				dp[i][1] = min(dp[i-1][1],dp[i-1][0]+1);
			}
		}
		printf("Case #%d: %d\n",casei,dp[in.length()-1][1]);
	}
	return 0;
}
	

