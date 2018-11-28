#include<iostream>
using namespace std;
int a[10000];
int main()
{
	int t;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		cout<<"Case #"<<k<<": ";
		int smax;
		cin>>smax;
		string s;
		cin>>s;
		for(int i=0;i<=smax;i++)
		{
			a[i]=s[i]-'0';
		}
		int ans=0;
		int tn=0;
		for(int i=0;i<=smax;i++)
		{
			if(tn>=i)
				tn+=a[i];
			else if(a[i]!=0)
			{
				ans+=(i-tn);
				tn+=(a[i]+i-tn);
			}
		}
		cout<<ans<<endl;
	}
	return 0;
}
