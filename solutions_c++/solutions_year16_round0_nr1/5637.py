#include<stdio.h>

int main()
{
	long long int a[10],i,j,k,c,t,N,temp,n,flag;
	
	FILE *fp = fopen("a.in","r");
	FILE *fp2 = fopen("ab.out","w");
	
	fscanf(fp,"%lld",&t);
	
	for(c=1;c<=t;c++)
	{
		for(i=0;i<10;i++)
		a[i]=0;
	
		fscanf(fp,"%lld",&n);
	
		if(n==0)
	{
    	fprintf(fp2,"Case #%lld: INSOMNIA\n",c);
    	continue;
	}
	
	N=n;
	while(1)
	{
		temp=N;
		while(temp>0)
		{
			k=temp%10;
			a[k]=1;
			temp=temp/10;
		}
		
		flag=1;
		for(j=0;j<10;j++)
		{
		if(a[j]==0)
		{
		flag=0;
		break;
		}
		}
		
		if(flag==1)
		{
		   fprintf(fp2,"Case #%lld: %lld\n",c,N);
			break;
		}
		else
		{
			N=N+n;
		}
	}
}
	return 0;	
		
}
