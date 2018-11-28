#include <vector>
#include <list>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#define int64 long long
#define Sort sort

using namespace std;

int map[200][600];
int v[200][600][8];
int q[5000000][2];
int dist[200][600];
bool visit[200][600];
int dir_x[8] = {0,0,1,-1,1,1,-1,-1};
int dir_y[8] = {1,-1,0,0,1,-1,1,-1};
int w,h,B,res;

int main()
{
	freopen("input1.in","r",stdin);
	freopen("output1.txt","w",stdout);
	
	int T;
	scanf("%d",&T);
	for (int ii=0;ii<T;++ii)
	{
		printf("Case #%d: ",ii+1);
		memset(map,-1,sizeof(map));
		scanf("%d%d%d",&w,&h,&B);
		for (int i=1;i<=w;++i)
			for (int j=1;j<=h;++j)
			{
				visit[i][j] = false;
				map[i][j] = 0;
			} 
		for (int i=0;i<B;++i)
		{
			int X1,Y1,X2,Y2;
			scanf("%d%d%d%d",&X1,&Y1,&X2,&Y2);
			++X1;++Y1;++X2;++Y2;
			for (int j=X1;j<=X2;++j)
				for (int k=Y1;k<=Y2;++k)
					map[j][k] = -1;
		}
		
		memset(v,0,sizeof(v));
		for (int i=1;i<=w;++i)
			for (int j=1;j<=h;++j)
			{
				if (!map[i][j+1] && !map[i+1][j+1]) v[i][j][0] = 1;
				if (!map[i][j] && !map[i+1][j]) v[i][j][1] = 1;
				if (!map[i+1][j] && !map[i+1][j+1]) v[i][j][2] = 1;
				if (!map[i][j] && !map[i][j+1]) v[i][j][3] = 1;
				if (!map[i+1][j+1]) v[i][j][4] = 1;
				if (!map[i+1][j]) v[i][j][5] = 1;
				if (!map[i][j+1]) v[i][j][6] = 1;
				if (!map[i][j]) v[i][j][7] = 1;
			}
		
		memset(dist,60,sizeof(dist));
		memset(visit,false,sizeof(visit));
		int l1 = 1,l2 = 0;
		for (int j=1;j<h;++j)
		{
			dist[w][j] = 0;
			++l2;
			q[l2][0] = w;
			q[l2][1] = j;
			visit[w][j] = true;
		}
		
		for (;l1<=l2;++l1)
		{
			int nx = q[l1][0];
			int ny = q[l1][1];
			visit[nx][ny] = false;
			for (int i=0;i<8;++i)
			{
				int nex = nx + dir_x[i];
				int ney = ny + dir_y[i];
				if (nex >= 0 && nex <= w && ney >0 && ney < h)
				{
					if (dist[nex][ney] > dist[nx][ny] + v[nx][ny][i])
					{
						dist[nex][ney] = dist[nx][ny] + v[nx][ny][i];
						if (!visit[nex][ney])
						{
							visit[nex][ney] = true;
							++l2;
							q[l2][0] = nex;
							q[l2][1] = ney;
						}
					}
				}
			}
		}
		
		int res = 999999999;
		for (int j=1;j<h;++j)
			res = min(res,dist[0][j]);
			
		printf("%d\n",res);
	}
		
	return 0;
}