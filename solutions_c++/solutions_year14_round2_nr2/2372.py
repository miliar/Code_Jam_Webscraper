#include<stdio.h>

int main()
{
	int t,tt;
	long int count,a,b,k,i,j;

	scanf("%d",&tt);

	for(t=1;t<=tt;t++)
	{
		scanf("%d%d%d",&a,&b,&k);
		count=0;

		for(i=0;i<a;i++)
		{
			for(j=0;j<b;j++)
			{
				if((i&j)<k)
					count++;
			}
		}

		printf("Case #%d: %ld\n",t,count);
	}

	return 0;
}
