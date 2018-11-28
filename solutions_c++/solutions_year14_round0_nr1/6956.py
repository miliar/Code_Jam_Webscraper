#include <stdio.h>
int a[17],b[5][5];
int main()
{
	int test_case;
	int i,j,k,temp,n,t,p;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);

	scanf("%d",&test_case);
	for(i=1;i<=test_case;i++)
	{
		for(j=1;j<=16;j++)
			a[j]=0;
		for(temp=1;temp<=2;temp++)
		{
			scanf("%d",&n);
			for(j=1;j<=4;j++)
			{
				for(k=1;k<=4;k++)
				{
					scanf("%d",&b[j][k]);
				}
			}
			for(j=1;j<=4;j++)
				a[b[n][j]]++;
		}
		p=0;
		for(j=1;j<=16;j++)
		{
			if(a[j]==2)
			{
				p++;
				t=j;
			}
		}
		printf("Case #%d: ",i);
		if(p==0)
			printf("Volunteer cheated!\n");
		else if(p>=2)
			printf("Bad magician!\n");
		else
			printf("%d\n",t);
	}
	return 0;
}