#include<stdio.h>
#include<stdlib.h>
main()
{
	long long test,org,i,j,n;
	scanf("%lld",&test);
	long long ans[test+1];
	long long m=0;
	while(test!=0)
	{
	scanf("%lld",&org);
	if(org==0)
	{
	ans[m++]=0;
	test=test-1;
	continue;
	}
	long long a1[10]={0,1,2,3,4,5,6,7,8,9};
	char a2[10]={'n','n','n','n','n','n','n','n','n','n',};
	long long mod,flag=1,k=1;
	while(1)
	{
		n=k*org;
		while(n!=0)
		{
		
		mod=n%10;
		for(j=0;j<10;j++)
		{
			if(a2[j]=='n')
			
			{
				flag=0;
				break;
			}
		}

		
		if(flag==0)
		{
		
		for(i=0;i<10;i++)
		{
			if(mod==a1[i])
			{
				a2[i]='m';
			}
		}
		}
		/*else
		{
			printf("%d",(k*org));//aur kuch karna hai
			exit(0);
		}*/
		n=n/10;
		flag=1;
		}
		
		for(j=0;j<10;j++)
		{
			if(a2[j]=='n')
			
			{
				flag=0;
				break;
			}
		}
		if(flag==1)
		{
			
			ans[m++]=(k*org);
	//	printf("%d	%d",(k*org),m);//aur kuch karna hai
			break;	
		}
	k=k+1;		
}
test=test-1;
}
for(n=0;n<m;n++)
{
	if(ans[n]==0)
	{
	printf("Case #%llu: INSOMNIA\n",(n+1));	
	}
	else
	{
	printf("Case #%llu: %llu\n",(n+1),ans[n]);
	}
}
}
