#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
#define MAX INT_MAX
#define MIN INT_MIN
using namespace std;

int main()
{
//	freopen("in.txt","r",stdin);
//	freopen("out.txt","w",stdout);
	int test;
	cin>>test;
	for(int t=1;t<=test;t++)
	{
		char str[20005];
		cin>>str;
		int l=strlen(str);
		
		int arr[10]={0};
		int dp[200]={0};
		for(int i=0;i<l;i++)
		{
			int temp=str[i]+32;
			dp[temp]++;
		}
		
	/*	for(int i=97;i<=122;i++)
		cout<<dp[i]<<" ";*/
		arr[0]=dp['z'];
		dp['z']-=arr[0];
		dp['e']-=arr[0];
		dp['r']-=arr[0];
		dp['o']-=arr[0];
		
		arr[2]=dp['w'];
		dp['t']-=arr[2];
		dp['w']-=arr[2];
		dp['o']-=arr[2];
		
		arr[4]=dp['u'];
		dp['f']-=arr[4];
		dp['o']-=arr[4];
		dp['u']-=arr[4];
		dp['r']-=arr[4];
		
		arr[6]=dp['x'];
		dp['s']-=arr[6];
		dp['i']-=arr[6];
		dp['x']-=arr[6];
		
		arr[8]=dp['g'];
		dp['e']-=arr[8];
		dp['i']-=arr[8];
		dp['g']-=arr[8];
		dp['h']-=arr[8];
		dp['t']-=arr[8];
		
		arr[5]=dp['f'];
		dp['f']-=arr[5];
		dp['i']-=arr[5];
		dp['v']-=arr[5];
		dp['e']-=arr[5];
		
		arr[7]=dp['v'];
		dp['s']-=arr[7];
		dp['e']-=arr[7];
		dp['v']-=arr[7];
		dp['e']-=arr[7];
		dp['n']-=arr[7];
		
		arr[3]=dp['r'];
		dp['t']-=arr[3];
		dp['h']-=arr[3];
		dp['r']-=arr[3];
		dp['e']-=arr[3];
		dp['e']-=arr[3];
		
		arr[1]=dp['o'];
		dp['o']-=arr[1];
		dp['n']-=arr[1];
		dp['e']-=arr[1];
		
		arr[9]=dp['e'];
		dp['n']-=2*arr[9];
		dp['i']-=arr[9];
		dp['e']-=arr[9];
		
		cout<<"Case #"<<t<<": ";
		for(int i=0;i<10;i++)
		{
			for(int j=0;j<arr[i];j++)
			cout<<i;
		}
		cout<<endl;
	}
	
	return 0;
}
