#include<stdio.h>
int main()
{
	int t,i,j,x,y,n,l,a[1000],max;
	FILE *fp1,*fp2;

	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		x=0;
		y=0;
		scanf("%d",&n);
		for(j=0;j<n;j++)
		{
			scanf("%d",&a[j]);
		}
		for(l=0;l<n-1;l++)
		{
			if(a[l]-a[l+1]>0)
			{
				x=x+a[l]-a[l+1];
			}
		}
	 
		max=a[0]-a[1];
		for(l=0;l<n-1;l++)
		{
			if(a[l]-a[l+1]>max)
			{
				max=a[l]-a[l+1];
			}
		}
	 
		for(l=0;l<n-1;l++)
		{
			if(a[l]>max)
			{
				y=y+max;
			}
			else
			{
				y=y+a[l];
			}
		}
		printf("case #%d: %d %d\n",i+1,x,y);
		
	}
}
