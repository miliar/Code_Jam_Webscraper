#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <vector>
#include <assert.h>

using namespace std;

typedef pair<int,int> pii;

pii par[111][111][4];
char grid[111][111];

const int dx[] = {0,0,1,-1};
const int dy[] = {1,-1,0,0};

int dir(int ch)
{
	if(ch == '<') return 1;
	if(ch == '>') return 0;
	if(ch == 'v') return 2;
	if(ch == '^') return 3;
	assert(false);
	return -1;
}

const pii FAILED = pii(-2,-2);

int main(void)
{
	int T = 0;
	int TK = 0;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ",++TK);

		memset(par,0,sizeof(par));

		int R = 0;
		int C = 0;
		scanf("%d %d",&R,&C);
		for(int i = 0;i < R;i++) scanf("%s",grid[i]);
		for(int i = 0;i < R;i++)
		{
			for(int j = 0;j < C;j++)
			{
				if(grid[i][j] == '.') continue;
				for(int d = 0;d < 4;d++)
				{
					int x = i; int y = j;
					while(true)
					{
						if(x < 0 || x >= R || y < 0 || y >= C)
						{
							par[i][j][d] = FAILED; // failed
							break;
						}
						if((x != i || y != j) && grid[x][y] != '.')
						{
							par[i][j][d] = pii(x,y);
							break;
						}
						x += dx[d]; y += dy[d];
					}
				}
			}
		}

		bool fail = false;
		int ans = 0;

		for(int i = 0;i < R;i++) for(int j = 0;j < C;j++)
		{
			if(grid[i][j] == '.') continue;

			bool okay = false;
			for(int d = 0;d < 4;d++) 
			{
				if(par[i][j][d] != FAILED) okay = true;
			}
			if(!okay)
			{
				fail = true;
			}

			if(par[i][j][dir(grid[i][j])] == FAILED) ans++;
		}

		if(fail) puts("IMPOSSIBLE");
		else printf("%d\n",ans);
	}
	return 0;
}
