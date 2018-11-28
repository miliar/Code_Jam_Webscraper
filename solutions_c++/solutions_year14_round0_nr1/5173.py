#include<stdio.h>
int main()
{
	long long int f,x,y,i,j,a[103][103],hash[500],ctr,k=1;
	scanf("%lld",&f);
	while(f--)
	{
		for(i=0;i<100;i++)
		hash[i]=0;
		scanf("%lld",&x);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				scanf("%lld",&a[i][j]);
			}
		}
		for(i=0;i<4;i++)
		hash[a[x-1][i]]++;
		scanf("%lld",&x);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				scanf("%lld",&a[i][j]);
			}
		}
		for(i=0;i<4;i++)
		hash[a[x-1][i]]++;
		ctr=0;
		for(i=0;i<100;i++)
		{
			if(hash[i]==2)
			{
				ctr++;
				y=i;
			}
		}
		printf("Case #%lld: ",k++);
		if(ctr==1)
		printf("%lld\n",y);
		else if(ctr==0)
		printf("Volunteer cheated!\n");
		else
		printf("Bad magician!\n");
	}
	return 0;
}
