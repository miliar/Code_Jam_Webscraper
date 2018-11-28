#include<iostream>
#include<stdlib.h>
using namespace std;
int main()
{
	int T;
	cin>>T;
	for(int k=1;k<=T;k++)
	{
		char c, s[1002];
		int n, a[1002], b[1002],ct=0;
		cin>>n;
		cin>>s;
		for(int i=0; i<=n;i++)
		{
			a[i]=(int)s[i]-48;
		}
		for(int i=0;i<=n;i++)
		{
			if(i==0) b[i]=a[i];
			else b[i]=b[i-1]+a[i];
			if(b[i]<=i)
			{
				ct+=i+1-b[i];
				b[i]+=i+1-b[i];
			}
		}
		cout<<"Case #"<<k<<": "<<ct<<endl;
	}
}
