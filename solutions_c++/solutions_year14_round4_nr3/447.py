#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <limits>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <string>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
const int INF = 1e9;

struct pt
{
	int x, y;
	pt()
	{}
	
	pt(int x, int y)
		:x(x), y(y)
	{}
};

const int Wmax = 105, Hmax = 505, bmax = 1005;
int R, C;
pt buildings[bmax][5];
int start, end;

const int max_vertices = bmax;
int num_vertices;
int adj[max_vertices][max_vertices];	// adjacency matrix
int min_dist[max_vertices];
bool visited[max_vertices];

int search()
{
    fill(min_dist,min_dist+max_vertices,INF);
    memset(visited,false,sizeof(visited));
    
    int v=start;
    min_dist[v]=0;
	 while(true)
    {
		 visited[v]=true;
		 if(v == end)
			 return min_dist[v];
	
		 for(int v_next=0;v_next<num_vertices;v_next++)
			 if(adj[v][v_next]<INF)
			 {
				 int cost_next=min_dist[v]+adj[v][v_next];
				 if(cost_next<min_dist[v_next])
					 min_dist[v_next]=cost_next;
			 }

		 int min_cost=INF;
		 for(int v_next=0;v_next<num_vertices;v_next++)
			 if(!visited[v_next] && min_dist[v_next]<min_cost)
			 {
				 v=v_next;
				 min_cost=min_dist[v_next];
			 }
	
    }
    
    return INF;
}

int dist(int x0, int y0, int x1, int y1)
{
	return max(abs(x0 - x1), abs(y0 - y1));
}

int ldist(int xv, int yv, int x, int y0, int y1)
{
	if(y0 > y1)
		swap(y0, y1);
	if(yv < y0)
		return dist(xv, yv, x, y0);
	if(yv > y1)
		return dist(xv, yv, x, y1);
	return abs(xv - x);
}

int ldist(int xv, int yv, int x0, int y0, int x1, int y1)
{
	if(x0 == x1)
		return ldist(xv, yv, x0, y0, y1);
	else if(y0 == y1)
		return ldist(yv, xv, y0, x0, x1);
	assert(false);
}

int ldist(pt v, pt l0, pt l1)
{
	return ldist(v.x, v.y, l0.x, l0.y, l1.x, l1.y);
}

int bdist(int i, int j)
{
	int d = INF;
	for(int a=0;a<4;a++)
		for(int b=0;b<4;b++)
		{
			d = min(d, ldist(buildings[i][a], buildings[j][b], buildings[j][b+1]));
			d = min(d, ldist(buildings[j][a], buildings[i][b], buildings[i][b+1]));
		}
	return d;
}

int main(int argc,char* argv[])
{
	int num_test_cases;
	scanf("%d",&num_test_cases);
	for(int test_case=1; test_case<=num_test_cases; test_case++)
	{
		int b;
		cin >> C >> R >> b;
		for(int i=0;i<b;i++)
		{
			int x0, y0, x1, y1;
			cin >> x0 >> y0 >> x1 >> y1;
			buildings[i][0] = pt(x0, y0);
			buildings[i][1] = pt(x0, y1);
			buildings[i][2] = pt(x1, y1);
			buildings[i][3] = pt(x1, y0);
			buildings[i][4] = buildings[i][0];
		}

		num_vertices = b + 2;
		start = b;
		end = b+1;
		
		for(int i=0;i<num_vertices;i++)
			for(int j=0;j<num_vertices;j++)
				adj[i][j] = INF;
		for(int i=0;i<b;i++)
			for(int j=0;j<b;j++)
				if(i == j)
					adj[i][j] = 0;
				else
				{
					adj[i][j] = bdist(i, j) - 1;
					//printf("%d %d: %d\n", i, j, adj[i][j]);
				}
		for(int i=0;i<b;i++)
		{
			adj[start][i] = adj[i][start] = buildings[i][0].x;
			adj[end][i] = adj[i][end] = C - 1 - buildings[i][2].x;
		}
		adj[start][end] = adj[end][start] = C;
		
		printf("Case #%d: %d\n", test_case, search());
	}
	return 0;
}
