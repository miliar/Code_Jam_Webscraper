#include<stdio.h>
int a[5][5],b[5][5];
int main()
{
	freopen("A-small-attempt3.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
	int i,t,n,j,k,p,q,h,ca=1;
	scanf("%d",&t);
	while(t--)
	{
		h=0;
		scanf("%d",&p);
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				scanf("%d",&a[i][j]);
			scanf("%d",&q);
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				scanf("%d",&b[i][j]);
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				if(a[p][i]==b[q][j])
				{
				k=a[p][i];h++;
				}
			}
		}
		printf("Case #%d: ",ca++);
		if(h==0)
			printf("Volunteer cheated!\n");
		else if(h>1)
			printf("Bad magician!\n");
		else
			printf("%d\n",k);
	}
	return 0;
}