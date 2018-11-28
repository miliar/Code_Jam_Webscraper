#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int map[105][105];
int n,m;
int row[105];
int col[105];

void init()
{
	memset(row,-1,sizeof(row));
	memset(col,-1,sizeof(col));
}

int main()
{
	int T;
	scanf("%d",&T);
	for (int caseno = 1;caseno<=T;++caseno)
	{
		scanf("%d%d",&n,&m);
		for (int i=0;i<n;++i)
			for (int j=0;j<m;++j)
				scanf("%d",&map[i][j]);
		init();
		for (int i=0;i<n;++i)
			for (int j=0;j<m;++j)
			{
				if (map[i][j] > row[i]) row[i] = map[i][j];
				if (map[i][j] > col[j]) col[j] = map[i][j];
			}

		bool isOk = true;
		for (int i=0;i<n && isOk;++i)
			for (int j=0;j<m && isOk;++j)
			{
				if (map[i][j] != row[i] && map[i][j] != col[j])
				{
					isOk = false;
				}
			}
			printf("Case #%d: ",caseno);
		if (isOk)
		{
			printf("YES\n");
		}
		else
		{
			printf("NO\n");
		}
	}
	return 0;
}