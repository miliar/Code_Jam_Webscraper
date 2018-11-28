#include<stdio.h>
int main()
{
	long long t,n,a[1010],i,s=0,c=0,d=0,j,k=0;
	FILE *ip,*op;
	ip=fopen("C:\\Users\\rimpa\\Desktop\\input.in","r");
	op=fopen("C:\\Users\\rimpa\\Desktop\\output.txt","a");
	fscanf(ip,"%lld",&t);
	for(i=1;i<=t;i++)
	{
		fscanf(ip,"%lld",&n);
		for(j=0;j<n;j++)
		{
			fscanf(ip,"%lld",&a[j]);
			if(j>=1)
			{
				d=a[j-1]-a[j];
				if(d>0)
					s=s+d;
			}
			if(c<d)
				c=d;
		}
		fgetc(ip);
		for(j=0;j<n-1;j++)
		{
			if(a[j]>=c)
				k=k+c;
			else
				k=k+a[j];
			//printf("%lld %lld\n",j,k);	
		}
		fprintf(op,"Case #%lld: %lld %lld\n",i,s,k);
		s=0;
		c=0;
		k=0;
		d=0;
	}
	return 0;
}
