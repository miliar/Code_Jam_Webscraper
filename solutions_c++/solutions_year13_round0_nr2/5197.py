#include <iostream>

using namespace std;

int mat[110][110];
int her[110], hec[110];

int main(void)
{
	int n, m, t;
//	freopen("D:\B-large.in", "r", stdin);
//	freopen("D:\B-ansL.out", "w", stdout);
	scanf("%d", &t);
	int ca = 0;
	while(t--)
	{
		scanf("%d %d", &n, &m);
		for(int i = 0; i < n; ++i)
		{
			her[i] = 0;
			for(int j = 0; j < m; ++j)
			{
				scanf("%d", &mat[i][j]);
				if(mat[i][j] > her[i])
					her[i] = mat[i][j];
			}
		}
		for(int j = 0; j < m; ++j)
		{
			hec[j] = 0;
			for(int i = 0; i < n; ++i)
			{
				if(mat[i][j] > hec[j])
					hec[j] = mat[i][j];
			}
		}
		int flag = 0;
		for(int i = 0; i < n; ++i)
		{
			for(int j = 0; j < m; ++j)
			{
				int th = her[i] > hec[j] ? hec[j] : her[i];
				if(mat[i][j] != th)
					flag = 1;
			}
		}
		printf("Case #%d: ", ++ca);
		if(flag)
			printf("NO\n");
		else
			printf("YES\n");
	}
	return 0;
}