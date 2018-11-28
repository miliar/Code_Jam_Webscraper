#include <cstdio>
#include <algorithm>
using namespace std;

int t;
int main()
{
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		int a[4][4],b[4][4],row1,row2,pos=0;
		scanf("%d",&row1);
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				scanf("%d",&a[j][k]);
		scanf("%d",&row2);
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				scanf("%d",&b[j][k]);
		row1--; row2--;	
		
		// checking whether volunteer has cheated or not
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				if(a[row1][j] == b[row2][k])
				{
					pos = 3;
					break;
				}
			}	
			if(pos == 3) break;
		}
		if(pos != 3)
		{
			printf("Case #%d: Volunteer cheated!\n",i+1);
			continue;
		}

		// Checking for bad magician
		int cnt = 0,ans; 
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				if(a[row1][j] == b[row2][k])
				{
					cnt++;
					if(cnt == 1) ans = a[row1][j];
				}
			}
		}
		if(cnt > 1)
			printf("Case #%d: Bad magician!\n",i+1);
		else
			printf("Case #%d: %d\n",i+1,ans);
	}	
	return 0;
}