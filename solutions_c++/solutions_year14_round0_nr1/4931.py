#include<stdio.h>
int main()
{
	int t,l;
	scanf("%d",&t);
	for(l=0;l<t;l++)
	{
		int i,j,k=-1,n,m;
		int a[4][4],b[4][4];
		scanf("%d",&n);
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		scanf("%d",&a[i]);
		scanf("%d",&m);
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		scanf("%d",&b[i]);
		n--;m--;
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		if(a[n][i]==b[m][j])
		{
			if(k==-1)
			{
				k=a[n][i];
			}
			else
			{
				k=20;break;
			}
		}
		if(k==-1)
		printf("Case #%d: Volunteer cheated!\n",l);
		else if(k==20)
		printf("Case #%d: Bad magician!\n",l);
		else
		printf("Case #%d: %d\n",l,k);
		
		
	}
	return 0;
}
