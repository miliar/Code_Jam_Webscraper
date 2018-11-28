#include<stdio.h>
int main()
{
	freopen("C:\\Users\\manish\\Desktop\\input.txt","r",stdin);
 	freopen("C:\\Users\\manish\\Desktop\\output.txt","w",stdout);
	int t,i,j,k,ans,z,x,y;
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		ans=0;
		scanf("%d",&x);
		int a[4][4],b[4][4];
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				scanf("%d",&a[j][k]);
			}
		}
		scanf("%d",&y);
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				scanf("%d",&b[j][k]);
			}
		}
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				if(a[x-1][j]==b[y-1][k])
				{
					ans++;
					z=a[x-1][j];
				}
			}
		}
		if(ans==1)	printf("Case #%d: %d\n",i+1,z);
		else if(ans==0)	printf("Case #%d: Volunteer cheated!\n",i+1);
		else if(ans>1) 	printf("Case #%d: Bad magician!\n",i+1);
	}
}
