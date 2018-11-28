#include <iostream>
using namespace std;

int main() {
	int t,n,ii,cnt,temp,i,j,ans;
	char s[102];
	bool flag[10];
	int dp[105][3];
	dp[0][0]=0;
	dp[0][1]=0;
	for(i=1;i<=100;i++){
		if(i%2){
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
		cin>>s;
		if(s[0]=='+')	temp=0;
		else temp=1;
		cnt=1;
		for(i=1; s[i]!='\0'; i++){
			if(s[i]==s[i-1])	continue;
			else cnt++;
		}
		ans = dp[cnt][temp];
		cout<<"Case #"<<ii<<": "<<ans<<endl;
	}
	return 0;
}