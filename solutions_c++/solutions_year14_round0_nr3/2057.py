#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <memory.h>
#include <string>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <vector>
#include <set>
#include <assert.h>

#define file_name ""

typedef long long ll;

const int N = 1e5+5;

using namespace std;

int dx[] = {-1, -1, 0, 1, 1, 1, 0, -1};
int dy[] = {0, 1, 1, 1, 0, -1, -1, -1};
bool us[15][15];
int r,c,m;
char a[15][15];

bool check(int x, int y)
{
	for(int i=0;i<8;++i)
		if (x+dx[i]>=0 && x+dx[i]<r && y+dy[i]>=0 && y+dy[i]<c && a[x+dx[i]][y+dy[i]]=='*')
			return false;
	return true;
}

int bfs(int x, int y)
{
	queue <pair <int, int> > q;
	memset(us,0,sizeof(us));
	q.push(make_pair(x,y));
	us[x][y] = 1;
	int count = 1;
	if (!check(x,y))
		return count;
	while (!q.empty())
	{
		x = q.front().first;
		y = q.front().second;
		q.pop();
		for(int i=0;i<8;++i)
			if (x+dx[i]>=0 && x+dx[i]<r && y+dy[i]>=0 && y+dy[i]<c && !us[x+dx[i]][y+dy[i]] && a[x+dx[i]][y+dy[i]]=='.')
			{
				us[x+dx[i]][y+dy[i]] = 1;
				count++;
				if (check(x+dx[i], y+dy[i]))
					q.push(make_pair(x+dx[i], y+dy[i]));
			}
	}
	return count;
}

int d;
bool rec(int x, int y, int m)
{
	if (!m)
	{
		int col = bfs(r-1, c-1);
		if (col + d - m ==r*c)
			return true;
		return false;
	}

	for(int i=x;i<r;++i)
		for(int j=(i==x ? y+1 : 0) ;j<c;++j)
		{
			a[i][j] = '*';
			if (rec(i,j,m-1))
				return true;
			a[i][j] = '.';
		}
	return false;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int countTests;
	scanf("%d",&countTests);
	for(int numTest=1;numTest<=countTests;++numTest)
	{
		scanf("%d%d%d",&r,&c,&m);
		d = m;
		for(int i=0;i<r;++i)
			for(int j=0;j<c;++j)
				a[i][j] = '.';
		bool res=0;
		if (!m || r*c-1==m)
		{
			res=1;
			for(int i=0;i<r && m;++i)
				for(int j=0;j<c && m;++j, --m)
					a[i][j]='*';
		}
		else
			res = rec(0,-1, m);

		printf("Case #%d:\n", numTest);
		if (!res)
			puts("Impossible");
		else
		{
			a[r-1][c-1] = 'c';
			for(int i=0;i<r;++i)
			{
				for(int j=0;j<c;++j)
					printf("%c",a[i][j]);
				puts("");
			}
		}
	}
	return 0;
}
