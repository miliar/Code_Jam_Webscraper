#include<stdio.h>
int main()
{
	int t,n,m,i,j,k,p,s;
	scanf("%d",&t);
	for(p=1;p<=t;p++)
	{
		scanf("%d",&n);
		int a[4][4],b[4][4];
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			scanf("%d",&a[i][j]);
		}
		scanf("%d",&m);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			scanf("%d",&b[i][j]);
		}
		k=0;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(a[n-1][i]==b[m-1][j])
				{
					s=a[n-1][i];
					k++;
				}
			}
		}
		printf("Case #%d: ",p);
		if(k==0)
		printf("Volunteer cheated!\n");
		else if(k==1)
		printf("%d\n",s);
		else
		printf("Bad magician!\n");
	}
return 0;
}
