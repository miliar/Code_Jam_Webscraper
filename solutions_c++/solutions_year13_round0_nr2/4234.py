#include<cstdio>
#include<cstring>
#include<string>
#include<vector>
#include<list>
#include<algorithm>

using namespace std;

vector<int> loc[150];
int map[150][150];
bool viscol[150], visrow[150];

int main()
{
	freopen("Binp.txt","r",stdin);
	freopen("Bout.txt","w",stdout);
	int t, n, m, i, j, k, l, x, y, c, T;
	bool foun;
	T = 0;
	scanf("%d", &t);
	while(t--)
	{
		++T;
		scanf("%d %d", &n, &m);
		for(i=1; i<=100; ++i)
			loc[i].clear();
		for(i=0; i<n; ++i)
		{
			for(j=0; j<m; ++j)
			{
				scanf("%d", &map[i][j]);
				loc[map[i][j]].push_back(i*m + j);
			}
		}
		memset(viscol, false, sizeof(viscol));
		memset(visrow, false, sizeof(visrow));
		foun = false;
		for(k=1; k<=100; ++k)
		{
			for(l=0; l<loc[k].size(); ++l)
			{
				i = loc[k][l]/m;
				j = loc[k][l]%m;

				if(visrow[i] || viscol[j])
				{
					continue;
				}
				//printf("-%d %d %d", map[i][j], i, j);
				bool row = true, col = true;
				c = 2;
				for(x = 0; x<m; ++x)
				{
					if(!viscol[x] && map[i][x] > map[i][j])
					{
						--c;
						row = false;
						break;
					}
				}
				if(row)
				{
					visrow[i] = true;
				}

				for(x = 0; x<n; ++x)
				{
					if(!visrow[x] && map[x][j] > map[i][j])
					{
						--c;
						col = false;
						break;
					}
				}
				if(col)
				{
					viscol[j] = true;
				}
				//printf(" %d\n", c);
				if(c == 0)
				{
					printf("Case #%d: NO\n", T);
					foun = true;
					break;
				}
			}
			if(foun == true)
			{
				break;
			}
		}
		if(foun == false)
		{
			printf("Case #%d: YES\n", T);
		}
	}
	return 0;
}
