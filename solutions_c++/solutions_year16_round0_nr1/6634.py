#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	long long int t,x,i,n,flag,sum,f,temp;
	
	cin>>t;
	for(x=1;x<=t;x++)
	{
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<x<<": "<<"INSOMNIA";
		}
		else
		{
			int ar[10];
			for(i=0;i<10;i++)
			ar[i]=0;
			flag=0;
			int s=1;
			while(flag==0)
			{
				f=s*n;
				temp=s*n;
				s++;
				while(temp!=0)
				{
					ar[temp%10]=1;
					temp=temp/10;
				}
				sum=0;
				for(i=0;i<=9;i++)
				{
					if(ar[i]==1)
					sum++;
				}
				if(sum==10)
				{
					flag=1;
				}
			}
			cout<<"Case #"<<x<<": "<<f;
		}
		cout<<endl;
	}
}