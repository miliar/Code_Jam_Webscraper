#include<stdio.h>
long long int exp(long long int a,long long int b)
{
	long long int tem=1;
	while(b)
	{
		if(b%2)
		tem=tem*a;
		b=b/2;
		a=a*a;
	}
	return tem;
}
int main()
{
	int t;
	scanf("%d",&t);
	int at;
	for(at=1;at<=t;at++)
	{
	long long int m;
	long long int j;
	long long int i;
	long long int p;
	long long int q;
	long long int add;
	long long int cnt =0;
	scanf("%lld %lld",&m,&p);
	printf("Case #%d:\n",at);
	long long int tem=m;
	m=2<<m-2;
	m--;
	long long int store[11];
	for(i=0;i<m;i++)
	{
		int a[16]={0};
		a[0]=1;
		a[tem-1]=1;
		j=0;
		while(i>>j)
		{
			if(i>>j&1)
			a[j+1]=1;
			j++;
		}
		add=0;
		j=2;
		while(j<=10)
		{
			add=0;
			long long int q=0;
			while(q<tem)
			{
				if(a[q])
				add=add+exp(j,q);
				q++;
			}
			q=2;
			while(q*q<=add)
			{
				if(add%q==0)
				{
					store[j]=q;
					break;
				}
				q++;
			}
			if(q*q>add)
			break;
			j++;
		}
		if(j==11)
		{
			printf("%lld ",add);
			for(q=2;q<=10;q++)
			printf("%lld ",store[q]);
			printf("\n");
			cnt++;
		}
		if(cnt==p)
		break;
		}
	}
	return 0;
}
