#include <bits/stdc++.h>
using namespace std;
int dp[105],t;
string s;
int main(){
    cin>>t;
    for(int k=1;k<=t;k++){
    	cin>>s;
    	int sz=s.size();
    	if(s[0]=='-')dp[1]=1;
    	else dp[1]=0;
    	for(int i=2;i<=sz;i++){
             if(s[i-1]=='+')dp[i]=dp[i-1];
             if(s[i-1]=='-'&&s[i-2]=='-')dp[i]=dp[i-1];
             if(s[i-1]=='-'&&s[i-2]=='+')dp[i]=dp[i-1]+2;
    	}
    	cout<<"Case #"<<k<<": "<<dp[sz]<<'\n';
    }

	return 0;
}