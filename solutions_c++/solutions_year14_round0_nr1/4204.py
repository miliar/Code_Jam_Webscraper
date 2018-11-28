#include<stdio.h>
#include<map>
using namespace std;

int main()
{
	int t,T=1;
	scanf("%d",&t);
	while(t--)
	{
		int mat_1[4][4],mat_2[4][4],n,m,i,j,count = 0,ans;
		map<int,int> C1,C2;
		printf("Case #%d: ",T++);
		scanf("%d",&n);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				scanf("%d",&mat_1[i][j]);
				if((i+1) == n)
				{
					C1[	mat_1[i][j] ]++;		
				}
			}
		}
		scanf("%d",&m);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				scanf("%d",&mat_2[i][j]);
				if((i+1) == m)
				{
					C2[	mat_2[i][j] ]++;		
				}
			}
		}
		for(i=0; i < 4; i++)
		{			
			if(C2[mat_1[n-1][i]] > 0)
			{
				count++;
				ans = mat_1[n-1][i];
				C2[mat_1[n-1][i]]--;
			}			
		}
		if(count == 1)
			printf("%d\n",ans);
		else if(count > 1)
			printf("Bad magician!\n");
		else if(count == 0)
		printf("Volunteer cheated!\n");
	}
	return 0;
}
