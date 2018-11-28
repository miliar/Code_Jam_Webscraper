#include<iostream>
#include<cmath>
using namespace std;

bool ispalin(int a)
{
	int b=0,c=a;
	while(a>0)
	{
		b=b*10+a%10;
		a=a/10;
	}
	if(c==b)
	{
		return 1;
	}
	return 0;	
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		int a,b,c,d,count=0;
		bool f=0;
		scanf("%d%d",&a,&b);
		c=ceil(sqrt(a));
		d=floor(sqrt(b));
		for(int j=c;j<=d;j++)
		{
			f=ispalin(j);
			if(f==1)
			{
				f=ispalin(j*j);
				if(f==1)
					count+=1;
			}
		}
		printf("Case #%d: %d\n",i,count);
	}
	return 0;
}
