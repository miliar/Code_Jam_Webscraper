#include <stdio.h>

int a[2010];
int main(void)
{
	int t ,i;
	int n ,j ,j2;
	int p1 ,p2 ,p;
	int temp;
	int ans;
	int min;
	
	scanf("%d" ,&t);
	for (i=1 ; i<=t ; i++)
	{
		scanf("%d" ,&n);
		for (j=1 ; j<=n ; j++)
		{
			scanf("%d" ,&a[j]);
		}
		ans=0;
		p1=1;
		p2=n;
		for (j2=1 ; j2<=n ; j2++)
		{
			min=2000000000;
			for (j=p1 ; j<=p2 ; j++)
			{
				if (a[j]<min)	
				{
					min=a[j];
					p=j;
				}
			}
			if (p-p1<=p2-p)
			{
				ans+=p-p1;	
				for (j=p-1 ; j>=p1 ; j--)
				{
					temp=a[j];
					a[j]=a[j+1];
					a[j+1]=temp;
				}
				p1++;
			}
			else
			{
				ans+=p2-p;
				for (j=p+1 ; j<=p2 ; j++)
				{
					temp=a[j];
					a[j]=a[j-1];
					a[j-1]=temp;
				}	
				p2--;			
			}
		}
		printf("Case #%d: %d\n" ,i ,ans);
	}

	return 0;
}
