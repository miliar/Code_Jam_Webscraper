#include<stdio.h>

int main()
{
	int t,i;
	long long n,k,c,l,x,d,t1;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%lli",&n);
		if(n==0)
			printf("Case #%d: INSOMNIA\n",i);
		else
		{
			k=0;c=0;
			while(k!=1023)
			{
				c++;
				t1=n*c;
				l=t1;
				while(l!=0)
				{
					d=l%10;
					x=1<<d;
					k=k|x;
					if(k==1023)
						break;
					l/=10;
				}
			}
			printf("Case #%d: %lli\n",i,t1);
		}
	}
	return 0;
}
