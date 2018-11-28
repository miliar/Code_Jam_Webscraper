#include<cstdio>

using namespace std;

int main()
{
	freopen("A-small.in","r",stdin);
	freopen("A-smallout.out","w",stdout);
	int a[4][4],b[4][4],ans1,ans2;
	int T,cases,i,j,lone,r1[4],r2[4];
	scanf("%d",&T);
	for(cases=1;cases<=T;cases++)
	{
		int z=0;
		scanf("%d",&ans1);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				scanf("%d",&a[i][j]);
				if(i==(ans1-1))
				{
					r1[z++]=a[i][j];
				}
			}
		}
		scanf("%d",&ans2);
		z=0;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				scanf("%d",&b[i][j]);
				if(i==(ans2-1))
				{
					r2[z++]=b[i][j];
				}
			}
		}
		int count = 0;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(r1[i]==r2[j])
				{
					count++;
					lone = r1[i];
				}
			}
		}
		printf("Case #%d: ",cases);
		if(count==1)
		{
			printf("%d\n",lone);
		}
		if(count>1)
		{
			printf("Bad magician!\n");
		}
		if(count==0)
		{
			printf("Volunteer cheated!\n");
		}
		
	}
	
	return 0;
	
}
