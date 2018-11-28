#include<bits/stdc++.h>
using namespace std;
int main()
{
if(!freopen("gcj12.txt","rt",stdin))
cout<<"HELLO";
freopen("gcj23.txt","wt",stdout);
int t;
int mat1[3][8]={{6,5,1,7,2,4,3,0},{2,6,3,5,7,0,4,1},{4,0,6,1,3,7,5,2}};
int mat2[3][8]={{7,5,1,6,2,4,0,3},{2,7,3,5,6,0,1,4},{4,0,7,1,3,6,2,5}};	
	cin>>t;	
	for(int x=1;x<=t;x++)
		{
		
int dp[5*10003][10]={0};
long long int X,l;	
char a[10002];	
	
	cin>>l>>X;
	cin>>a;
	int prod=6;

	
	for(int i=0;i<l*(X%4);i++)
	{
		prod=mat2[a[i%l]-'i'][prod];
	//	cout<<prod<<endl;
	}
	if(prod==7)
	{
	
	for(int j=l*min((long long int)5,X)-1;j>=1;j--)
	{
		
		for(int i=0;i<=7;i++)
		{
			dp[j][i]=dp[j+1][mat1[a[j%l]-'i'][i]];
			if(a[j%l]-'i'==i)
			dp[j][i]=1;
			//	cout<<j<<" "<<j%l<<" "<<i<<" "<<dp[j][i]<<endl;
		}
	
	}
	int prod=6,flag=0;
	for(int i=0;i<=l*min((long long int)4,X)-1;i++)
	{
	//	cout<<prod<<endl;
		if(prod==0&&dp[i][1]==1)
		{
			flag=1;
			break;
		}
		prod=mat2[a[i%l]-'i'][prod];
	}
if(flag==1)
	cout<<"Case #"<<x<<":"<<" YES"<<endl;
else
	cout<<"Case #"<<x<<":"<<" NO"<<endl;
}
else
{
	cout<<"Case #"<<x<<":"<<" NO"<<endl;
}
}
return(0);
}
