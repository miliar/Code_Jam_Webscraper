#include<stdio.h>
#include<math.h>
int main()
{
	int t,a,b,count=0;
	scanf("%d %d %d",&t,&a,&b);
	int c[9];
	int d[32];
	d[0]=d[a-1]=1;
	for(int i=1;i<a-1;i++)
	d[i]=0;
	printf("Case #1:\n");
	while(count<b)
	{
		int i;
		for(i=2;i<=10;i++)
		{
			long long int sum=0;
			for(int j=0;j<a;j++)
			{
				sum+=pow(i,j)*d[j];
			}
			int j;
			for(j=2;j<=sqrt(sum);j++)
			{
				if(sum%j==0)
				{	
					c[i-2]=j;
					break;
				}
			}
			if(j>sqrt(sum))
			break;			
		}
		if(i==11)
		{
		count++;
		for(i=a-1;i>=0;i--)
		printf("%d",d[i]);
		for(i=0;i<=8;i++)
		printf(" %d",c[i]);
		printf("\n");
		}
		i=a-2;	
		while(1)
		{
			if(d[i]==0)
			{
				d[i]=1;
				
				break;
			}
			else
			d[i]=0;
			i--;			
		}					
	}
	return 0;
}
