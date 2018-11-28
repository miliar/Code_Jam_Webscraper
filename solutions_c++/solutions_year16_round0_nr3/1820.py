#include<stdio.h>

int main(void)
{
	int i,k;
	int arr[50];
	int t;
	int n,j;
	unsigned long long p,q;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d %d %d",&t,&n,&j);
	for(i=1;i<=n;i++)
		arr[i]=0;
	arr[1]=arr[n]=1;
	printf("Case #1:\n");
	for(;j>=1;)
	{
		for(i=2;i<=n;i++)
		{
			arr[i+1]+=arr[i]/2;
			arr[i]%=2;
		}
		p=1;
		q=0;
		for(i=1;i<=n;i++)
		{
			q+=p*arr[i];
			p*=-1;
		}
		if(q==0)
		{
			for(i=n;i>=1;i--)
			{
				printf("%d",arr[i]);
			}
			printf(" ");
			for(i=3;i<=11;i++)
				printf("%d ",i);
			printf("\n");
			j--;
		}
		arr[2]++;
	}
}