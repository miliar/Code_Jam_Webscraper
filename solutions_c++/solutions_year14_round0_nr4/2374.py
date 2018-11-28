#include<iostream>
#include<algorithm>
#include<stdio.h>
using namespace std;
double a[1010],b[1010];
int main()
{
	freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
	int t,n;
	cin>>t;
	for(int in=1;in<=t;in++)
	{
		cin>>n;
		int a1=0,a2=0,a3=0;
		for(int i=0;i<n;i++)
		{
			cin>>b[i];
		}
		for(int i=0;i<n;i++)
		{
			cin>>a[i];
		}
		sort(a,a+n);
		sort(b,b+n);
		bool di[1010]={0};
		for(int i=0;i<n;i++)
		{
			double k=a[n-1-i],c=0;
			for(int j=0;j<n;j++)
			{
				if(!di[j] && b[j]>k)c++;
			}
			//cout<<c<<a2<<endl;
			if(c>(a2))
			{
				a2++;
			}
			else
			{
				for(int j=0;j<n;j++)if(!di[j]){di[j]=1;break;}
			}
		}
		bool d[1010]={0};
		for(int i=0;i<n;i++)
		{
			double k=b[n-i-1];
			bool ch=0;
			for(int j=0;j<n;j++)
			{
				if(d[j]==0 && a[j]>k)
				{
					ch=1;
					d[j]=1;
					a1++;
					break;
				}
			}
			if(!ch)for(int j=0;j<n;j++)if(!d[j]){d[j]=1;break;}
		}
		cout<<"Case #"<<in<<": "<<max(a3,a2)<<" "<<n-a1<<endl;

	}
}