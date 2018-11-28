#include<iostream>
#include<bits/stdc++.h>
using namespace std;
//int digit()
int main()
{
	long long int t,l,k,m,n,j,s,c,i,b[10];
	cin>>t;
	for(l=1;l<=t;l++)
	{
		c=0;
		for(i=0;i<10;i++)
		{
			b[i]=0;
		}
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<l<<": "<<"INSOMNIA"<<endl;
		}
		else
		{
			for(i=1;;i++)
			{
				s=n*i;
				c=0;
				//cout<<"s="<<s<<endl;
				k=n*i;
				while(s>0)
				{
					m=s%10;
					b[m]++;
					s=s/10;
				}
				for(j=0;j<10;j++)
				{
					if(b[j]>=1)
					{
						c++;
						//cout<<"c="<<c<<endl;
					}
				}
				if(c==10)
				{
					cout<<"Case #"<<l<<": "<<k<<endl;
					break;
				}
			}	
		}
		
	}
}
