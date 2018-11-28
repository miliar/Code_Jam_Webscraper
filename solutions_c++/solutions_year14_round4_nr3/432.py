#pragma comment (linker, "/STACK:268435456")
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <cmath>
#include <cctype>
#include <sstream>
#include <ctime>

using namespace std;

struct edge
{
	int b, nxt, twin, f, c;
};

int field[110][510];
int n;
edge g[1000000];
int lnk[1000000];
int d[1000000];
int q[1000000];
map<pair<int, int>, int> nodes;

void add_edge(int from, int to)
{
	g[n].b = to;
	g[n].nxt = lnk[from];
	g[n].f = 0;
	g[n].c = 1;
	g[n].twin = n + 1;
	lnk[from] = n;

	g[n + 1].b = from;
	g[n + 1].nxt = lnk[to];
	g[n + 1].f = 0;
	g[n + 1].c = 0;
	g[n + 1].twin = n;
	lnk[to] = n + 1; 
	n += 2;
}

int get_node(int x, int y)
{
	pair<int, int> p(x, y);
	if (nodes.find(p) == nodes.end())
		nodes[p] = n++;
	return nodes[p];
}

void bfs()
{
	memset(d, -1, sizeof d);
	int head = 0, tail = 1;
	q[head] = 0;
	while (head < tail)
	{
		for (int cur = lnk[q[head]]; cur != -1; cur = g[cur].nxt)
			if (g[cur].c > g[cur].f && d[g[cur].b] == -1)
			{
				d[g[cur].b] = cur;
				q[tail++] = g[cur].b;
			}
		head++;
	}
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tn;
    cin >> tn;
    for (int tc = 0; tc < tn; tc++)
    {
    	int w, h, b;
    	cin >> w >> h >> b;
    	memset(field, 0, sizeof field);
    	memset(lnk, -1, sizeof lnk);
    	for (int i = 0; i < b; i++)
    	{
    		int x0, y0, x1, y1;
    		cin >> x0 >> y0 >> x1 >> y1;
    		for (int x = x0; x <= x1; x++)
    			for (int y = y0; y <= y1; y++)
    				field[x][y] = 1;
    	}
    	nodes.clear();
    	n = 2;
    	for (int i = 0; i < w; i++)
    		for (int j = 0; j < h; j++)
    			if (!field[i][j])
	    		{
	    			add_edge(get_node(i, j), get_node(i, j + h));
	    			if (j == 0)
	    				add_edge(0, get_node(i, j));
	    			if (j == h - 1)
	    				add_edge(get_node(i, j + h), 1);
	    			if (j < h - 1 && !field[i][j + 1])
	    			{
	    				add_edge(get_node(i, j + h), get_node(i, j + 1));
	    				add_edge(get_node(i, j + 1 + h), get_node(i, j));
	    			}
	    			if (i < w - 1 && !field[i + 1][j])
	    			{
	    				add_edge(get_node(i, j + h), get_node(i + 1, j));
	    				add_edge(get_node(i + 1, j + h), get_node(i, j));
	    			}
	    		}

	    int result = 0;
	    while (1)
	    {
	    	bfs();
	    	if (d[1] == -1)
	    		break;
	    	int cur = 1;
	    	while (cur)
	    	{
	    		g[d[cur]].f++;
	    		g[g[d[cur]].twin].f--;
	    		cur = g[g[d[cur]].twin].b;
	    	}
	    	result++;
	    }
    	cout << "Case #" << tc + 1 << ": " << result << endl;
    }
    return 0;
}