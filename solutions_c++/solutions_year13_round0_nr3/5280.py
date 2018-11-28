#include<stdio.h>
int main()
{
	int t,a,b,count,K=1,i;
	int c[]={0,1,4,9,121,484,10201};
	scanf("%d",&t);
	while(t--)
	{
		count=0;
		scanf("%d %d",&a,&b);
		for(i=0;i<=6;i++)
		{
			if(c[i]>=a&&c[i]<=b)
				count++;
		}
		printf("Case #%d: %d\n",K,count);
		K++;
	}
	return 0;
}
