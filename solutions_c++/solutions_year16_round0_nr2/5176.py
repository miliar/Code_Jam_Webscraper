#include<bits/stdc++.h>

using namespace std;
#define ll long long 
int main()
{ 
    freopen("B-large.in","r",stdin);
    freopen("output_2.txt","w",stdout);	 
	 ll t,n;
	 cin>>t;
	  for(int z=1;z<=t;z++)
	 { int cnt[10];
	   for(int i=0;i<10;i++)
	      cnt[i]=0;
	   
	   ll sum=0;
	   int flag=1;
	   //cin>>n;
	   string str;
	   cin>>str;
	   n=str.length();
	   int dp[2][120];
	   for(int i=0;i<2;i++)
	     {
	     	for(int j=0;j<110;j++)
	     	  dp[i][j]=0;
		 }
		 
		 if(str[0]=='+')
		   {dp[0][0]=0;
		      dp[1][0]=1;
		  }
		  else
		   {
		   	dp[0][0]=1;
		   	dp[1][0]=0;
		   }
		   
		   for(int i=1;i<n;i++)
		   {
		   	  if(str[i]=='+')
		   {   dp[0][i]=dp[0][i-1];
		       dp[1][i]=dp[0][i-1]+1;
		  }
		  else
		   {
		   	   dp[0][i]=dp[1][i-1]+1;
		   	   dp[1][i]=dp[1][i-1];
		   }
		   	  
		   }
		   
	   
	 	cout<<"Case #"<<z<<": "<<dp[0][n-1]<<endl;
	  } 
}
