#include<stdio.h>
int main()
{
	int t,j,n,k,m,x;
	scanf("%d",&t);
	for(j=1;j<=t;j++)
	{
		int a[17]={0};
		scanf("%d",&n);
		int i=0;
		while(i<16)
		{
			scanf("%d",&k);
			i++;
			if(i>(n-1)*4 && i<=n*4)
			{
				a[k]++;
			}
		}
		scanf("%d",&m);
		int count=0;
		i=0;
		bool flag=0;
		while(i<16)
		{
			scanf("%d",&k);
			i++;
			if(i>(m-1)*4 && i<=m*4)
			{
				if(a[k]>0)
				{
				count++;
				if(flag==0)
				{
				x=k;
				flag=1;
				}
				}
			}
		}
		if(count==1)
		printf("Case #%d: %d\n",j,x);
		else if(count>1)
		printf("Case #%d: Bad magician!\n",j);
		else if(count==0)
		printf("Case #%d: Volunteer cheated!\n",j);
	}
	return 0;
}
