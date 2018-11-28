#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <algorithm>
#include <map>
#include <iostream>
#include <sstream>
#include <queue>
#include <cstring>
#include <ctime>
#include <cfloat>

using namespace std;

#define SZ 105
#define INF 10000001

int n, m;
int maze[SZ][SZ];

int main()
{
	//freopen("B-small-attempt0.in", "rt", stdin);
	//freopen("B-small.out", "wt", stdout);

	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);

	int inp, kase, i, j, k;
	scanf("%d", &inp);
	for(kase = 1; kase <= inp; kase++)
	{
		scanf("%d %d", &n, &m);
		for(i = 0; i < n; i++)
		{
			for(j = 0; j < m; j++)
			{
				scanf("%d", &maze[i][j]);
			}
		}
		int mn = INF;
		int mnx, mny;
		bool gflag = false;
		while(true)
		{
			mn = INF;
			for(i = 0; i < n; i++)
			{
				for(j = 0 ; j < m ; j++)
				{
					if(maze[i][j] != -1 && maze[i][j] < mn)
					{
						mn = maze[i][j];
						mnx = i;
						mny = j;
					}
				}
			}
			if(mn == INF)
			{
				gflag = true;
				break;
			}
			bool lflag = true;
			int cnt = 0;
			for(j = 0; j < m; j++)
			{
				if(maze[mnx][j] > mn)
				{
					lflag = false;
					break;
				}
			}
			if(lflag)
			{
				cnt++;
				for(j = 0; j < m; j++)
				{
					maze[mnx][j] = -1;
				}
			}
			lflag = true;
			for(i = 0; i < n; i++)
			{
				if(maze[i][mny] > mn)
				{
					lflag = false;
					break;
				}
			}
			if(lflag)
			{
				cnt++;
				for(i = 0; i < n; i++)
				{
					maze[i][mny] = -1;
				}
			}
			if(cnt == 0)
			{
				break;
			}
		}
		printf("Case #%d: ", kase);
		if(gflag)
			printf("YES\n");
		else
			printf("NO\n");
	}

	return 0;
}
