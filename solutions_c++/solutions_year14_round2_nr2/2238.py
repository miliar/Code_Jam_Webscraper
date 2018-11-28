#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
	int t,i=0,a,b,w,p,k,sum;
	cin>>t;
	while(++i<=t)
	{
		cin>>a>>b>>k;
		p=-1;
		sum=0;
		while(++p<a)
		{
			w=-1;
			while(++w<b)
			{
				if((w&p)<k)
				sum=sum+1;
			}
		}
		printf("Case #%d: %d\n",i,sum);
	}
	return 0;
}
