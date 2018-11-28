#include<stdio.h>
#include<math.h>
long long int power(int a,int b)
{
	//printf("here\n");
	if(b==1)
	return a;
	if(b==0)
	return 1;
	else
	return a*power(a,b-1);
}
int main()
{
	int t,a,b,c;
	long long int count;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		printf("Case #%d:",i+1);
		scanf("%d %d %d",&a,&b,&c);
		for(int j=1;j<=c;j++)
		{
			count=1;
			for(int k=b-1;k>=0;k--)
			{
				count+=(j-1)*power(a,k);	
			}
			printf(" %lld",count);
		}
		printf("\n");
	}
	return 0;
}
