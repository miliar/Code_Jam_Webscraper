#include<stdio.h>
main()
{
	freopen("A-large.in","r",stdin);
	freopen("output_file.out","w",stdout);
	long long int t,n,num,ans,ca=0;
	long long int arr[10];
	int i=0,count=0,j,flag=0;
	scanf("%lld",&t);
	while(t--)
	{
		ca++;
		count=0;
		flag=0;
		for(i=0;i<10;i++)
		{
			arr[i]=0;
		}
		scanf("%lld",&num);
		n=num;
		if(n==0)
		{
			printf("Case #%d: INSOMNIA\n",ca);
		}
		else
		{
			for(i=1;flag==0;i++)
			{
				n=num*i;
				ans=n;
				while(n)
				{
		    		j=n%10;
		    		arr[j]++;
		    		if(arr[j]==1)
		    		{
		    			count++;
		    			if(count==10)
		    			{
		    				flag=1;
		    			}
		    		}
		    		n /= 10;
				}
			}
			printf("Case #%d: %lld\n",ca,ans);
		}
	}
	return 0;
}
