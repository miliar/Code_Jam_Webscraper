#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <unordered_map>
#include <unordered_set>

using namespace std;

int r,c;
char ma[110][110];
int rnum[110];
int cnum[110];
const int dx[] = {-1, 0, 1, 0};
const int dy[] = {0, 1, 0, -1};

int check(int i, int j)
{
	int dir = -1;
	if(ma[i][j] == '^')
		dir = 0;
	else if(ma[i][j] == '>')
		dir = 1;
	else if(ma[i][j] == 'v')
		dir = 2;
	else
		dir = 3;
	int cx = i + dx[dir];
	int cy = j + dy[dir];
	while(cx >= 0 && cx <r && cy >= 0 && cy < c && ma[cx][cy] == '.')
		cx += dx[dir], cy += dy[dir];

	//printf("%d %d: \n", i, j);
	//printf("%d %d\n", cx, cy);
	if(cx >= 0 && cx <r && cy >= 0 && cy < c)
		return 0;
	else
		return 1;
}

int main()
{
	int T;
	int ca = 0;
	//freopen("in.txt", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &T);
	while(T--)
	{
		scanf("%d%d", &r, &c);
		for (int i = 0; i < r; ++i)
		{
			scanf("%s", ma[i]);
		}


		memset(rnum, 0, sizeof(rnum));
		memset(cnum, 0, sizeof(cnum));
		for (int i = 0; i < r; ++i)
		{
			for (int j = 0; j < c; ++j) if(ma[i][j] != '.')
			{
				rnum[i]++;
				cnum[j]++;
			}
		}
		int flag = 1;
		for (int i = 0; i < r; ++i)
		{
			for (int j = 0; j < c; ++j) if(ma[i][j] != '.')
			{
				if(rnum[i] == 1 && cnum[j] == 1)
				{
					flag = 0;
					break;
				}
			}
		}

		printf("Case #%d: ", ++ca);
		if(!flag)
			printf("IMPOSSIBLE\n");
		else
		{
			int res = 0;
			for (int i = 0; i < r; ++i)
			{
				for (int j = 0; j < c; ++j) if(ma[i][j] != '.')
				{
					res += check(i, j);
				}
			}
			printf("%d\n", res);
		}
		
	}
	return 0;
}