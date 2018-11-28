#include<bits/stdc++.h>
using namespace std;
int main()
{
	ios_base::sync_with_stdio(false);
	int t,n;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>n;
		int a[n];
		for(int j=0;j<n;j++)
		{
			cin>>a[j];
		}
		int s1=0,s2=0,m=0;
		for(int j=0;j<n-1;j++)
		{
			int d=a[j]-a[j+1];
			//cout<<"diff of "<<j<<" "<<j+1<<" is "<<d<<endl;
			s1+=max(0,d);
			m=max(m,d);
		}
		//cout<<"max "<<m<<endl;
		for(int j=0;j<n-1;j++)
		{
			s2+=min(a[j],m);
		}
		cout<<"Case #"<<i<<": "<<s1<<" "<<s2<<endl;
	}
}