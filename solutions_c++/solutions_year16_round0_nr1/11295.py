#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
	freopen("codejam1.in","r",stdin);
freopen("codejamout1.out","w",stdout);
	int t;
	cin>>t;
	int k=1;
	while(t--)
	{
		ll n,i=0,ans;
		cin>>n;
		int a[11]={0},cnt=0;
		if(n==0)
	cout<<"Case #"<<k<<": "<<"INSOMNIA\n";
		else
		{
		ll s=n,p=n;
		while(true)
		{
			
			n=s;
			while(n>0)
			{
			
			int r=n%10;
			n/=10;
			if(a[r]==0)
			{
				cnt++;
				a[r]=1;
			}
			if(cnt==10)
			{
				ans=s;
				break;
			}
		}
		if(cnt==10)
		break;
		s=p*(i+1);
		i++;
	}
		cout<<"Case #"<<k<<": "<<s<<endl;
	}
		k++;
	}
	return 0;
}
