#include<iostream>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("q1l.out","w",stdout);
	int t;
	cin>>t;
	int k=0;
	while(t--)
	{
		k++;
		long long n;
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<k<<": "<<"INSOMNIA"<<endl;
			continue;
		}
		int a[10];
		for(int i=0;i<10;i++)
		{
			a[i]=0;
		}
		int k1=1;
		long long m=n,ans=n;
		int f=1;
		int j=2;
		while(k1!=0)
		{
			f=1;
			long long k2=m;
			while(k2!=0)
			{
				int r=k2%10;
				k2=k2/10;
				a[r]=1;
			}
			for(int i=0;i<10;i++)
			{
				if(a[i]==0)
				{
					f=0;
				}
			}
			if(f==0)
			{
				k1=1;
			}
			else
			{
				k1=0;
			}
			ans=m;
			m=j*n;
			j++;
		}
		cout<<"Case #"<<k<<": "<<ans<<endl;
	}
	return 0;
}
