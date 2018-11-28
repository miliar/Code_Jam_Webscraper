#include<stdio.h>
long int t,i,n,j,v[10],flag,d,d1,dig,k;
int main()
{

scanf("%ld",&t);
long int test[t];
for(i=1;i<=t;i++)
	scanf("%ld",&test[i]);
for(i=1;i<=t;i++)	
{
	n=test[i];
	j=1,flag=0,d,d1;
	printf("Case #%ld: ",i);
	if(n==0)
	{
		printf("INSOMNIA\n");
	}
	
	for(k=0;k<10;k++)
		v[k]=0;
		if(n!=0)
		{
		do
		{
			flag=0;
			d=n*(j++);
			d1=d;
			while(d1>0)
			{
				dig=d1%10;
				v[dig]=1;
				d1=d1/10;
			}
			for(k=0;k<10;k++)
				if(v[k]==0)
					flag=1;
			//if(flag==0)
			//	break;
		}while(flag==1);
		printf("%ld\n",d);
		}
}	
				
}			
