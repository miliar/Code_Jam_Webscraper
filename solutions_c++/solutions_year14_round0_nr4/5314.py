#include<stdio.h>
int main()
{
	int l,cost,i,j,x,y,n,items,a[10000];
	freopen("A-large-practice.in","rt",stdin);
	freopen("large.out","wt",stdout);
	scanf("%d",&n);
	for(l=0;l<n;l++)
	{
		scanf("%d",&cost);
		scanf("%d",&items);
		for(i=0;i<items;i++)
			scanf("%d",&a[i]);
		for(i=0;i<items;i++)
		{
			for(j=i+1;j<items;j++)
			{
				if((a[i]+a[j])==cost)
				{
					x=i+1;
					y=j+1;
				}
			}
		}
		printf("case #%d: %d %d\n",l+1,x,y);
	}
	return 0;
}
