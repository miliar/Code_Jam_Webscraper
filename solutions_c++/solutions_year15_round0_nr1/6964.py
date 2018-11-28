#include<iostream>
using namespace std;
int main()
{
int t;
cin>>t;
for(int i=0;i<t;i++)
{
	int max_shy;cin>>max_shy;
	string shylevel;
	cin>>shylevel;
	int arr[max_shy+1];int dp[max_shy+1];
	for(int j=0;j<=max_shy;j++)
	{
		arr[j]=shylevel[j]-'0';
		dp[j]=0;	
	}
	
	
        	
	dp[0]=arr[0]; 
	int count=0;
	for(int j=1;j<=max_shy;j++)
	{
		if(dp[j-1]>=j)		
		dp[j]=dp[j-1]+arr[j];
		else
		{
		count=count+(j-dp[j-1]);
		dp[j]=dp[j-1]+arr[j]+(j-dp[j-1]);
			}
		
	}
for(int j=0;j<=max_shy;j++)cout<<dp[j]<<" ";cout<<endl;

cout<<"Case #"<<i+1<<": "<<count<<endl;

}



}
