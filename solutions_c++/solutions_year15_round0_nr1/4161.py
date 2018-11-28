#include<stdio.h>
int main()
{
	long long int i,n,t,count,sum;
	scanf("%lld",&t);
        long long int k=t;
	for(long long int j=0;j<t;j++)
	{
                 count=0;
		scanf("%lld",&n);
               char a[n+2];
		sum=0;
                 scanf("%s",a);
		for(i=0;i<=n;i++)
		{
		//	scanf("%c",&a[i]);
       if(a[i]!='0')
{
			if(i>sum)
			{
				count=count +(i-sum);
                                sum=sum+(i-sum);
			}
			sum=sum+a[i]-'0';
}
		}
		printf("case #%lld: %lld\n",j+1,count);
		
	}
	return 0;
}
