#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int t,j=0,i,c,d=0,k=1,a[20],l=0,q=1;
	long s[200];
	cin>>t;
	for(i=0;i<t;i++)
	{
		cin>>s[i];
	}
	while(l<t)
	{
		long b=s[l];
		j=0;
		k=0;
		while(b>0)
		{
			q=0;
			d=0;
			c=b%10;
			b=b/10;
			for(i=0;i<j;i++)
			{
				if(a[i]==c)
				{
					d=1;
				}
			}
			if(d==0)
			{
				a[j]=c;
				j++;
			}
			if(j==10)
			{
				b=0;
			}
			else if(b==0 && j!=10)
			{
				k++;
				b=s[l]*k;
			}
			if(k>=100)
			{
				b=0;
				q=1;
			}
		}
		if(q!=1)
		{
			cout<<"Case #"<<l+1<<": "<<k*s[l]<<"\n";
		}	
		else
		{
			cout<<"Case #"<<l+1<<": "<<"INSOMNIA\n";
		}
		l++;
		
	}
	return 0;
}
