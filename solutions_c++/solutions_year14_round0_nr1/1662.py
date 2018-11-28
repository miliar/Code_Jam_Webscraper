#include<cstdio>
#include<cstdlib>
using namespace std;

int main()
{
	int t,T,a1,a2,r1[10],r2[10],count,i,j,x,ans;
	scanf("%d",&T);
	for (t=1;t<=T;t++)
	{
		scanf("%d",&a1);
		count=0;
		for (i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				if (i==a1)
				{
					scanf("%d",&r1[j]);
				}
				else
					scanf("%d",&x);
			}
		}
		
		scanf("%d",&a2);
		for (i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				if (i==a2)
				{
					scanf("%d",&r2[j]);
				}
				else
					scanf("%d",&x);
			}
		}
		
		for (i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				if (r1[i]==r2[j])
				{
					count++;
					ans = r1[i];
				}
			}
		}
		if (count==0)
		{
			printf("Case #%d: Volunteer cheated!\n",t);
		}
		else if (count==1)
		{
			printf("Case #%d: %d\n",t,ans);
		}
		else
			printf("Case #%d: Bad magician!\n",t);
	}
	return 0;
}