#include<bits/stdc++.h>
using namespace std;
int main()
{
	ios_base::sync_with_stdio(false);
	int t,smax,ans,sum;
	cin>>t;
	string s;
	for(int j=1; j<=t; j++)
	{
		cin>>smax;
		cin>>s;
		ans=0;
		sum=s[0]-'0';
		for(int i=1; i<=smax; i++)
		{
			if(sum<i)
			{
				ans=ans+i-sum;
				sum=i;
			}
			sum=sum+s[i]-'0';
		}
		cout<<"Case #"<<j<<": "<<ans<<endl;
	}
	return 0;
}
	
