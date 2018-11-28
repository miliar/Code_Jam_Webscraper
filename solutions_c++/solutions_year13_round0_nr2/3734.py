#include<cstdio>

int main(int argc, char const *argv[])
{
	int t;
	scanf("%d",&t);
	for (int testcase = 1; testcase <= t; ++testcase)
	{
		int m,n;
		scanf("%d %d",&m,&n);
		int lawn[m][n];
		for(int i=0;i<m;i++)
		{
			for(int j=0;j<n;j++)
			{
				scanf("%d",&lawn[i][j]);
			}
		}
		bool ans = true;
		for(int i=0;i<m;i++)
		{
			for(int j=0;j<n;j++)
			{
				bool Valid1 = true;
				bool Valid2 = true;
				//Ver
				for(int k=0;k<m;k++)
				{
					if(lawn[k][j] > lawn[i][j])
					{
						Valid1 = false;
					}
				}
				//Hor
				for(int k=0;k<n;k++)
				{
					if(lawn[i][k] > lawn[i][j])
					{
						Valid2 = false;
					}
				}

				ans = ans && (Valid1 || Valid2);
			}
		}
		if(ans)printf("Case #%d: YES\n",testcase);
		else printf("Case #%d: NO\n",testcase);
	}
	return 0;
}