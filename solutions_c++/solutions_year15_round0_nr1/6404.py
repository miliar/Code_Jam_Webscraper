#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t,s; cin>>t;
	for(int j=1;j<=t;j++) {
		cin>>s;
		int dp[s+1];
		char a[s+1];
		getchar();
		for(int i=0;i<=s;i++) {cin>>a[i];}
		dp[0]=0;
		int ctr=0;
		for(int i=1;i<=s;i++) {dp[i]=dp[i-1]+a[i-1]-48; if(dp[i]<i) {ctr++;dp[i]++;}}
		cout<<"Case #"<<j<<": "<<ctr<<"\n";
	}
	return 0;
}