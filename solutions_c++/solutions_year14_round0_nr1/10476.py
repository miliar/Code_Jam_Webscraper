#include<stdio.h>

int main()
{
	int t,a1,a2;
	int ar1[4][4],ar2[4][4],flag[4][4];
	scanf("%d",&t);
	for(int tc=1;tc<=t;tc++)
	{
		scanf("%d",&a1);
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				scanf("%d",&ar1[i][j]);
		scanf("%d",&a2);
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				scanf("%d",&ar2[i][j]);

		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				flag[i][j]=0;

			int count=0;	
			int y;		
			for(int j=0;j<4;j++)
			  if(ar2[a2-1][j]==ar1[a1-1][0] || ar2[a2-1][j]==ar1[a1-1][1] || ar2[a2-1][j]==ar1[a1-1][2] || ar2[a2-1][j]==ar1[a1-1][3])
				{
					count++;
					y = ar2[a2-1][j];
				}
			if(count==1)
				printf("Case #%d: %d\n",tc,y);

			if(count>1)
				printf("Case #%d: Bad magician!\n",tc);
			if(count==0)
				printf("Case #%d: Volunteer cheated!\n",tc);

		
	}

	
	return 0;
}
