/*
coded by @just_code21
© to Prakhar Srivastava
*/
#include<bits/stdc++.h>
#define ll long long int
#define M 1000000007
using namespace std;

int main()
{
	ifstream fcin("B-large.in");
	ofstream fcout("output.txt");
	int t;
	fcin>>t;
	for(int j=1;j<=t;j++)
	{
		string s;
		fcin>>s;
		int size=s.size();
		int dp[size+2]={0};
		for(int i=size-1;i>=0;i--)
		{
			if(s[i]=='-' && dp[i+1]%2==0)
				dp[i]=dp[i+1]+1;
			else if(s[i]=='+' && dp[i+1]%2!=0)
				dp[i]=dp[i+1]+1;
			else 
				dp[i]=dp[i+1];
		}
		fcout<<"Case #"<<j<<": "<<dp[0]<<"\n";
	}
	return 0;
}
/*

*/


