#include<bits/stdc++.h>
using namespace std;
int a[10];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("aad.out","w",stdout);
	int t;
	cin>>t;
	int m=t;
	while(t--)
	{
		long long n;
		cin>>n;
		long long num;
		for(int i=0;i<10;i++)
		a[i]=0;
		int count=0;
		if(n==0)
		cout<<"Case #"<<m-t<<": INSOMNIA\n";
		else
		{
			long long j=1;
			while(count!=10)
			{	count=0;
				num=n*j;
				j++;
				long long u=num;
			//	a[u%10]++;
				while(u>0)
				{		
					a[u%10]++;
					u/=10;
				}
				for(int i=0;i<10;i++)
				{//	cout<<a[i]<<"\t";
					if(a[i]>0)
					count++;
				}
				//cout<<count<<"\n";
			}
			cout<<"Case #"<<m-t<<": "<<num<<"\n";
		}
	}
}
