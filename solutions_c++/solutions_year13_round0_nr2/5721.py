#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int i,j,t,k,n,a,b,m,flg;
	int arr[100][100];
	int ar[100];
	int br[100];
	cin>>t;
	for(k=1;k<=t;k++)
	{
		cin>>n>>m;
		for(i=0;i<n;i++)
		{
			a=0;
			for(j=0;j<m;j++)
			{
				cin>>arr[i][j];
				if(arr[i][j]>a)
					a=arr[i][j];
			}
			ar[i]=a;
		}
		for(j=0;j<m;j++)
		{
			a=0;
			for(i=0;i<n;i++)
				if(arr[i][j]>a)
					a=arr[i][j];
			br[j]=a;
		}
		flg=0;
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				a=arr[i][j];
				if(a<ar[i]&&a<br[j])
				{
					flg=1;
					break;
				}
			}
			if(flg==1)
				break;
		}
		if(flg==0)
			cout<<"Case #"<<k<<": YES\n";
		else
			cout<<"Case #"<<k<<": NO\n";
	}
	return 0;
}