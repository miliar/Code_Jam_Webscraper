#include <stdio.h>
int main()
{
	int t,i;
	int smax;
	char a[1009];
	scanf ("%d",&t);
	int t1=t;
	while (t--)
	{
		scanf ("%d",&smax);
		scanf ("%s",&a);
		int sum=0;int ans=0;
		for (i=0;i<=smax;i++)
		{
		
			if (sum-(i)<0)
			{
				ans+=i-sum;
				sum+=i-sum;
			}
				sum+=a[i]-48;
		}
	printf ("Case #%d: %d\n",t1-t,ans);
	}
	scanf ("%d",&a);
	return 0;
}