#include<iostream>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<map>
#include<vector>
#include<cstdio>
#include<climits>
#include<cmath>
#include<cstring>
#define mod 1000000009
using namespace std;

int main()
{
	int t,n,i,k,j,temp,temp2;
	cin>>t;
	for(k=1;k<=t;k++)
	{
		cin>>n;
		temp=0;
		temp2=0;
		double a[n],b[n];
		for(i=0;i<n;i++)
			cin>>a[i];
		for(i=0;i<n;i++)
			cin>>b[i];	
		sort(a,a+n);
		sort(b,b+n);
		for(i=0,j=0;i<n && j<n;)
		{
			if(a[i]>b[j])
			{
				i++;
				j++;
				temp++;
			}
			else
			{
				i++;
			}
		}
		for(i=n-1;i>=0;i--)
		{
			int flag=0;
			for(j=0;j<n;j++)
			{
				if(b[j]>a[i])
				{
					b[j]=-b[j];
					flag=1;
					break;
				}
			}
			if(flag==0)
			{
				temp2++;
				for(j=0;j<n;j++)
				{
					if(b[j]>0)
					{
						b[j]=-b[j];
						break;
					}
				}
			}
		}
		cout<<"Case #"<<k<<": "<<temp<<" "<<temp2<<endl;
		//printf("%.7f\n",ans);
	}
	return 0;
}