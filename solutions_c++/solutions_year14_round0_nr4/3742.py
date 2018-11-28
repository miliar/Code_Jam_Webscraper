#include<iostream>
#include<stdlib.h>
using namespace std;
int main()
{
//	freopen("C:\\Users\\Tarun\\Desktop\\ip.txt","r",stdin);
//	freopen("C:\\Users\\Tarun\\Desktop\\op.txt","w",stdout);
	int i,j,k,n,t;
	double a[1005],b[1005];
	cin>>t;
	for(k=1;k<=t;k++)
	{
		int c[1005]={0},d[1005]={0},np=0;
		cout<<"Case #"<<k<<": ";
		cin>>n;
		for(i=0;i<n;i++)
			cin>>a[i];
		for(i=0;i<n;i++)
			cin>>b[i];
		sort(a,a+n);
		sort(b,b+n);
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
			{
				if(c[j]!=1 && a[j]>b[i])
				{
					c[j]=1;
					np++;
					break;
				}
			}
		}
		cout<<np<<" ";
		np=0;
		for(i=n-1;i>=0;i--)
		{
			for(j=0;j<n;j++)
			{
				if( d[j]!=1 && b[j]>a[i] )
				{
					d[j]=1;
					break;
				}
			}
			if(j==n)
			{
				for(j=0;j<n;j++)
				{
					if(d[j]!=1)
					{
						d[j]=1;
						break;
					}
				}
				np++;
			}
		}
		cout<<np<<endl;
	}
	return 0;
}