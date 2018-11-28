#include <iostream>
using namespace std;

char arr[102];
int main() {
	int t,n,ii,cnt,temp,i,j,ans;
	int dp[109][4];
	dp[0][0]=0;
	dp[0][1]=0;
	for(i=1;i<=100;i++){
		if(i&1){
			dp[i][0] = dp[i-1][0];
			dp[i][1] = 1+dp[i-1][0];
		}
		else{
			dp[i][0] = 2+dp[i-1][0];
			dp[i][1] = dp[i-1][1];
		}
	}
	cin>>t;
	for(ii=1; ii<=t; ii++){
		cin>>arr;
		if(arr[0]=='+')	temp=0;
		else temp=1;
		cnt=1;
		for(i=1; arr[i]!='\0'; i++){
			if(arr[i]==arr[i-1])	continue;
			else cnt++;
		}
		cout<<"Case #"<<ii<<": "<<dp[cnt][temp]<<endl;
	}
	return 0;
}