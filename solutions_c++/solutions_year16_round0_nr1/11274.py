#include<stdio.h>

int i,j,t,n,m,p,a[10],b;
main()
{
	FILE *d;
	d=fopen("CountingSheep","w");
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		scanf("%d",&n);
		if(n==0)
		{
			fprintf(d,"Case #%d: INSOMNIA\n",i+1);
			continue;
		}
		for(j=0;j<10;j++)
			a[j]=0;
		b=0;m=0;
		while(1)
		{
			m+=n;
			p=m;
			while(p>0)
			{
				if(a[p%10]==0)
				{
					b++;
					a[p%10]=1;
				}
				p/=10;
			}
			if(b==10)
				break;
		}
		fprintf(d,"Case #%d: %d\n",i+1,m);
	}
	fclose(d);
}
