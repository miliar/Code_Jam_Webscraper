#include<bits/stdc++.h>
using namespace std;
int dp[1000005];
int rev[1000005];

int reverse(int n)
{
	string s="";
	while(n>0)
	{
		int k=(n%10);
		s+=(k+'0');
		n/=10;
	}
	//cout<<s<<endl;
	int a=0;
	int k=0;
	for(int i=s.length()-1; i>=0; i--,k++)
	{
		a+=((s[i]-'0')*(pow(10,k)));
	}
	//cout<<a<<endl;
	return a;
}
/*
int fun(int n)
{
	if(n<=9)
	{
		dp[n]=n;
		return n;
	}
	
	if(n>1000000)
	{
		dp[n]=100000000;
		return (dp[n]);
	}
	
	if(dp[n]!=-1)
	return dp[n];
	
	int a=100000000;
	if(dp[n-1]==-1)
		a=fun(n-1);
		
		a=dp[n-1];
	
	int b=100000000;
	int temp=reverse(n);
	
	if(dp[temp]==-1)
		b=fun(temp);
	
	b=dp[temp];
	
	dp[n]=min(a,b);
	return dp[n];
}
*/
int main()
{
	int T,n;
	scanf("%d", &T);
	
	//for(int i=0; i<=1000000; i++)
	//rev[i]=-1;
	
	for(int i=1; i<=1000000; i++)
	{
		int temp=reverse(i);
		rev[i]=temp;
	}

	//for(int i=0; i<=30; i++)
	//cout<<rev[i]<<" ";
	//cout<<endl;	
	
	dp[1]=1;
	for(int i=2; i<=1000000; i++)
	{
		int temp=rev[i];
		if(temp>=i || (i%10==0))
		{
			dp[i]=dp[i-1]+1;
		}
		else
		{
			dp[i]=min(dp[i-1], dp[temp])+1;
		}
		//if(i<20)
		//cout<<dp[i]<<" ";
	}
	//cout<<endl;
	for(int t=1; t<=T; t++)
	{
		scanf("%d", &n);
		//int ans=fun(n);
		int ans=dp[n];
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
