#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,j,c,ans1,n,i;
	cin>>t;
	int ans;
	char s[1000];
	for(j=1;j<=t;j++)
	{
		ans1=0;
		ans=0;
		cin>>n;
		cin>>s;
		//ans=(ans+s[0]%400-48);
		for(i=1;i<=n;i++)
		{
			ans=ans+s[i-1]%400-48;
			c=i-ans;
			if(c > 0 && (s[i]%400-48)>0)
			{
				ans1=ans1+c;
			
			ans=ans+c;
			}
		}
	//	cout<<ans;
		//ans1=n-ans;
		//if(ans1<=0)
		//{
		//	cout<<"Case #"<<j<<":"<<" "<<0<<'\n';
		//}
		//else
		//{
				cout<<"Case #"<<j<<":"<<" "<<ans1<<'\n';
		//}
	}
	return 0;
}
