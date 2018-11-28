#include<stdio.h>
int main()
{
	int t;
	scanf("%d",&t);
	long long int q;
	for(q=1;q<=t;q++)
	{
		long long int m[10]={0};
		long long int i=1;
		long long int j;
		long long int p;
		scanf("%lld",&p);
		if(!p)
		printf("Case #%lld: INSOMNIA\n",q);
		else
		{
			while(1)
			{
				long long int tem=i*p;
				while(tem)
				{
					m[tem%10]++;
					tem=tem/10;
				}
				for(j=0;j<=9;j++)
				if(!m[j])
				break;
				if(j==10)
				{
					long long int ad=i*p;
					printf("Case #%lld: %lld\n",q,ad);
					break;
				}
				i++;
			}
		}
	}
	return 0;
}
