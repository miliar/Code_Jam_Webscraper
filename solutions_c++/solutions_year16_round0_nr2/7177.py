#include <iostream>
#include <queue>
#include <vector>
#include <map>
#include <cmath>
#include <cstring>
#include <string>
#include <set>
#include <algorithm>
#include <stack>
#include <deque>
#define MAX 1000000000
#define eps 1e-10
using namespace std;


int gao(string s)
{
	if(s.size()==1)
	{
		if(s[0]=='-')
			return 1;
		else return 0;
	}
	
	if(s[s.size()-1]=='+')
		return gao(s.substr(0,s.size()-1));

	int cc = 0;		

	if(s[0]=='+')
	{
		cc++;
		s[0]='-';
	}
		
		
	if(s[0]=='-')
	{
		//just reverse
		cc++;	
		reverse(s.begin(),s.end());
		for(int i=0;i<s.size();i++)
		{
			if(s[i]=='+')
			s[i]='-';
			else s[i]='+';
		}
		return gao(s.substr(0,s.size()-1))+cc;			
	}
}

int dp[1000][2];

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	
	int re;
	cin>>re;
	
	for(int cases = 1;cases<=re;cases++)
	{
		string s;
		cin>>s;
		//printf("Case #%d: %d\n",cases,gao(s));
		
		if(s[0]=='+')
		{
			dp[0][0]=1;
			dp[0][1]=0;
		}
		else
		{
			dp[0][0]=0;
			dp[0][1]=1;
		}
		
		for(int i=1;i<s.size();i++)
		{
			if(s[i]=='+')
			{
				dp[i][1]=min(dp[i-1][1],dp[i-1][0]+1);
				dp[i][0]=min(dp[i-1][1]+1,dp[i-1][0]+3);
			}
			else
			{
				dp[i][0]=min(dp[i-1][0],dp[i-1][1]+1);
				dp[i][1]=min(dp[i-1][0]+1,dp[i-1][1]+3);
			}
		}
		printf("Case #%d: %d\n",cases,dp[s.size()-1][1]);
		
		
	}
	
	
}
	