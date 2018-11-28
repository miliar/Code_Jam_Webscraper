#include<stdio.h>
#include<string.h>
int main()
{
	int t,w;
	scanf("%d",&t);
	for(w=1;w<=t;w++)
	{
		long int i,n,counter=10,x,y,z;
		long int a[10];
		for(i=0;i<10;i++)
		{
			a[i]=11;
		}
		scanf("%ld",&n);
		if(n==0)
		{
			printf("Case #%d: INSOMNIA\n",w);
			goto abc;
		}
		for(i=0;i<1000;i++)
		{	y=n*i;
			if(counter==0)
			{	z=i-1;
				break;
			}
			while(y>0)
		{
			x=y%10;
			if(a[x]!=x)
			{
				counter=counter-1;
				a[x]=x;
			}
			y=y/10;
		}
		
		
		}
		
		
		

		printf("Case #%d: %ld\n",w,n*z);
	
	abc:;
	}
	return 0;
}
