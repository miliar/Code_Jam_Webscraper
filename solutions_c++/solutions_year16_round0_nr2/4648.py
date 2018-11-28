#include <iostream>
#include <cstring>
using namespace std;
int main(void)
{
	int t;
	cin>>t;
	for(int j=1;j<=t;j++)
	{
		char s[1010];
		int dp[1010]={0};
		cin>>s;
		int l=strlen(s);
		for(int i=l-1;i>=0;i--)
		{
			if(s[i]=='-'&&dp[i+1]%2==0)
				dp[i]=dp[i+1]+1;
			else if(s[i]=='+'&&dp[i+1]%2!=0)
				dp[i]=dp[i+1]+1;
			else dp[i]=dp[i+1];
		}
		cout<<"Case #"<<j<<": "<<dp[0]<<endl;
	}
}