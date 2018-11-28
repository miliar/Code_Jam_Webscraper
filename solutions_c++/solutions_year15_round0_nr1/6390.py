/*This program is made on Vibhore's Machine.*/
#include<iostream>
#include<stdio.h>
#include<fstream>
#include<cstdio>
using namespace std;
int main()
{
  freopen("5.in", "r", stdin);
  freopen("5", "w", stdout);
	
	int t,n,i,j,k,sum,ans,c;
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		sum=0;
		ans=0;
		c=0;
		scanf("%d",&n);
		char carr[n+1];
		int arr[n+1];
		scanf("%s",&carr);
//cout<<"carr:"<<carr<<endl;
		for(j=0;j<n+1;j++)
		{arr[j]=(int)carr[j]-48; /*cout<<arr[j]<<"   ";*/}
//cout<<"carr:"<<arr<<endl;
		for(j=0;j<n;j++)
		{
			sum=sum+arr[j];
			c=j+1-sum;
			if(c<0)
			c=0;
			ans=ans+c;
			sum=sum+c;
//cout<<"sum:"<<sum<<"&ans:"<<ans<<endl;
		}
		cout<<"Case #"<<(i+1)<<": "<<ans<<endl;
	}
	return 0;
}

