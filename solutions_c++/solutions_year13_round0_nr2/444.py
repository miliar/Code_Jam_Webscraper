#include<iostream>
#include<stdio.h>
#include<fstream>
#include<vector>
using namespace std;
int main()
{
	int i,j,t,k,n,a,b,m,flg;
	//fstream cin;
	int arr[100][100];
	int m1[100];
	int m2[100];
	//cin.open("C:\\Users\\Sushrut\\Desktop\\Google Code Jam\\2013\\Qualify\\B\\Small Input.txt",ios::in);
	//freopen("C:\\Users\\Sushrut\\Desktop\\Google Code Jam\\2013\\Qualify\\B\\Small Output.txt","w",stdout);
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
			m1[i]=a;
		}
		for(j=0;j<m;j++)
		{
			a=0;
			for(i=0;i<n;i++)
				if(arr[i][j]>a)
					a=arr[i][j];
			m2[j]=a;
		}
		flg=0;
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				a=arr[i][j];
				if(a<m1[i]&&a<m2[j])
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