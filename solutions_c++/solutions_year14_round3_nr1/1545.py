#include<stdio.h>
#include<iostream>

using namespace std;

int main()
{
	int t,ptr=0;
	scanf("%d",&t);
	while(t--)
	{
		ptr++;
		long long int p,q,a,b,cnt=0,i;
		
		char  ch;
		scanf("%lld%c%lld",&p,&ch,&q);
		a=p;
		b=q;
		
		while(b%2==0)
		{
			cnt++;
			b=b/2;
		}
		if(a%b!=0)
		printf("Case #%d: impossible\n",ptr);
		else
		{
			q=q/b;
			p=p/b;
			double d=(double)p/(double)q;
	//		printf("%lld %lld  %lf\n",p,q,d);
			long long int k=1;
			cnt=0;
			for(i=1;i<50;i++)
			{
				 k=k*2;
				 double h=1/(double)k;
			//	 printf("%lld   ",k);
				if(d >= h)
				{
					break;
				}
				else
				cnt++;
			}
			printf("Case #%lld: %lld\n",ptr,cnt+1);
		}
	}
	return 0;
}
