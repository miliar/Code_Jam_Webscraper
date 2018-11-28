#include<iostream>
#include<fstream>
#include<stdio.h>
#include<string.h>

using namespace std;

int s[10]={0,0,0,0,0,0,0,0,0,0};
int count=0;


void digits(int x)
{
	int d=0;
	while(x>0)
	{
		d=x%10;
		x=x/10;
		if(s[d]==0)
		{
			count++;
			s[d]=1;
		}
	}
}

int main()
{
	int t=0,n=0,i=0,n1=0;
	scanf("%d",&t);

	for(int k=0;k<t;k++)
	{
		for(int y=0;y<10;y++)
			s[y]=0;
		scanf("%d",&n);
		std::cout<<"Case #"<<(k+1)<<": ";
		count=0;
		if(n==0)
			std::cout<<"INSOMNIA\n";
		else
		{
			i=1;
			n1=0;
			while(count!=10)
			{
				n1=n1+n;
				digits(n1);
			}
			std::cout<<n1<<"\n";
		}
	}
	return 0;
}
