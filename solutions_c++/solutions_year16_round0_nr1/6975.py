#include<stdio.h>
int main(void)
{
	int t,i,k,l;
	long long n,j,temp,n1;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%lld",&n1);
		if (n1==0)
		printf("Case #%d: INSOMNIA\n",i);
		else
		{
		
		int a[10]={0,1,2,3,4,5,6,7,8,9};
		int c=10;
		j=1;
		
		while(c>0)
		{
		n=n1*j;
		temp=n;
		
		while(temp>0)
		{
		k=temp%10;
		 for(l=0;l<10;l++)
		 {
		 	if(k==a[l])
		 	{
		 		a[l]=11;
		 		c=c-1;
		 		if(c<=0)
		 		break;
			 }
		 }
		temp=temp/10;	
			}	
			++j;
		}
		printf("Case #%d: %lld\n",i,n);
	}
	}
	return 0;
}
