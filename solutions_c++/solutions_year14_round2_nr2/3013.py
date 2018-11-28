#include<stdio.h>

int main()
{
	int N,j,k,i,count=1;
	long long int A,B,K,counter=0;
	scanf("%d",&N);
	
	while(N)
	{
		counter=0;
		scanf("%lld",&A);
		scanf("%lld",&B);
		scanf("%lld",&K);
		
		for(j=0;j<A;j++)
		{
			for(k=0;k<B;k++)
			{
				for(i=0;i<K;i++)
				{
					if((j&k)==i)
					{
						counter++;
						break;
					}
				}
			}
		}
		printf("CASE #%d: %lld\n",count,counter);
		N--;
		count++;
	}
	
	return 0;
}
