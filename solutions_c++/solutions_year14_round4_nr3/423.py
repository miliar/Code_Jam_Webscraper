#include <assert.h>
#include <cstring>
#include <iostream>
#include <fstream>
#include <climits>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <list>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>

using namespace std;

int w, h ,b;

struct Node
{
	int x0, y0, x1, y1;
};

struct NodeCmp
{
	bool operator()(const Node &a, const Node &b)  
	{  
		return a.x0 > b.x0;
	}  
};

bool grid[100][500];

bool dfs(int x, int y, int dir)
{
	//printf("step: %d %d\n", x, y);
	if ((y == 0 && dir == -1) || (y == h-1 && dir == 1)) return true;

	if (x - 1 >= 0 && !grid[x-1][y]) 
	{
		grid[x-1][y] = true;
		if (dfs(x-1, y, dir)) return true;
	}
	if (y + dir >= 0 && y + dir < h && !grid[x][y+dir])
	{
		grid[x][y+dir] = true;
		if (dfs(x, y+dir, dir)) return true;
	}
	if (x + 1 < w && !grid[x+1][y])
	{
		grid[x+1][y] = true;
		if (dfs(x+1, y, dir)) return true;
	}
	return  false;
}

int main() {
	int cases;
	scanf("%d", &cases);
	for (int t = 1; t <= cases; t++)
	{
	    scanf("%d %d %d", &w, &h, &b);
	    
	    //std::vector<Node> blk;
	    memset(grid, false, sizeof(grid));
	    for (int i = 0; i < b; i ++)
	    {
	    	int x0, x1, y0, y1;
	    	scanf("%d %d %d %d", &x0, &y0, &x1, &y1);
	    	for (int j = x0; j <= x1; j++)
	    	{
	    		for (int k = y0; k <= y1; k++)
	    		{
	    			grid[j][k] = true;
	    		}
	    	}
	    }
	    int bottle = w+1;
	    int k;
	    for (int i = 0; i < h; i++)
	    {
	    	int tmp = w;
	    	for (int j = 0; j < w; j++)
	    	{
	    		if (grid[j][i]) tmp --;
	    	}
	    	if (tmp < bottle)
	    	{
	    		bottle = tmp;
	    		k = i;
	    	}
	    }
	    //printf("haha %d %d\n", bottle, k);

	    int res = 0;
	    for (int i = 0; i < w; i++)
	    {
	    	if (!grid[i][k] && dfs(i, k, -1) && dfs(i, k, 1))
	    	{
	    		res++;
	    	}
	    }
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}