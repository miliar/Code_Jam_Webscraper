#include<iostream>
#include<fstream>
#include<string.h>
using namespace std;

int main()
{
	freopen("Aa.in","r",stdin);
	freopen("output","w",stdout);
	int t,i,j,l,k;
	cin>>t;
	for(k=1;k<=t;k++)
	{
		int n,a[2501]={0},b[100][50],c[50],temp;
		cin>>n;
		for(i=0;i<2*n-1;i++)
		{
			for(j=0;j<n;j++)
			{
				cin>>b[i][j];
				a[b[i][j]]++;	
			}
		}
		l=0;
		for(i=1;i<=2500;i++)
		{
			if(a[i]>0 && a[i]%2==1)	
			{
				c[l]=i;
				l++;
			}
		}
		for(i=0;i<l-1;i++)
		{
			for(j=0;j<l-i-1;j++)
			{
				if(c[j]>c[j+1])
				{
					temp=c[j];
					c[j]=c[j+1];
					c[j+1]=temp;
				}	
			}
		}
		cout<<"Case #"<<k<<": ";
		for(i=0;i<l;i++)
		cout<<c[i]<<" ";
		cout<<"\n";
	}
	return 0;
}
