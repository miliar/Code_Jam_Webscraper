#include <cstdio>

int ntest;

int main()
{
	scanf("%d", &ntest);
	for(int test = 1;test <= ntest;++test)
	{
		int vrow[2][4];
		for(int i = 0;i < 2;++i)
		{
			int crow;
			scanf("%d", &crow);
			int row[4];
			for(int j = 0;j < 4;++j)
			{
				for(int k = 0;k < 4;++k)
					scanf("%d", &row[k]);
				if(j + 1 == crow)
				{
					for(int k = 0;k < 4;++k)
						vrow[i][k] = row[k];
				}
			}
		}
		int ans = -1;
		for(int i = 0;i < 4;++i)
		{
			bool found = 0;
			for(int j = 0;j < 4;++j)
				if(vrow[0][i] == vrow[1][j])
					found = 1;
			if(found)
			{
				if(ans == -1)
					ans = vrow[0][i];
				else if(ans > 0)
					ans = 0;
			}
		}
		printf("Case #%d: ", test);
		if(ans > 0)
			printf("%d\n", ans);
		else if(ans == 0)
			printf("Bad magician!\n");
		else
			printf("Volunteer cheated!\n");
	}
}
