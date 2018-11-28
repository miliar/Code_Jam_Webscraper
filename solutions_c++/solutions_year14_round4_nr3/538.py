#include <iostream>
#include <vector>
#include <queue>
#include <set>

using namespace std;

struct Node
{
	set<int> routesTo;
};

vector<Node> nodes;

int w, h, b;
vector<vector<int>> river;

void tryConn(int x1, int y1, int x2, int y2)
{
	if(x2 < 0 || y2 < 0 || x2 >= w || y2 >= h) return;

	if(river[x1][y1] == 0 || river[x2][y2] == 0) return;

	int nodeOut = x1 + y1 * w + w * h;
	int nodeIn = x2 + y2 * w;

	nodes[nodeOut].routesTo.insert(nodeIn);
}

void maxFlow()
{
	while(true)
	{
		vector<int> visited(nodes.size(), -1);
		deque<int> que;

		visited[w * h * 2] = w * h * 2;
		que.push_back(w * h * 2);

		while(!que.empty())
		{
			int i = que.front();
			que.pop_front();

			for(int j : nodes[i].routesTo)
			{
				if(visited[j] == -1)
				{
					visited[j] = i;
					que.push_back(j);
				}
			}
		}

		if(visited[w * h * 2 + 1] == -1) break;

		int i = w * h * 2 + 1;

		while(i != w * h * 2)
		{
			int last = visited[i];

			nodes[last].routesTo.erase(i);
			nodes[i].routesTo.insert(last);

			i = last;
		}
	}

	cout << nodes[w * h * 2 + 1].routesTo.size();
}

void solve()
{
	cin >> w >> h >> b;

	nodes.clear();
	nodes.resize(w * h * 2 + 2);

	river.clear();
	river.resize(w, vector<int>(h, 1));

	for(int i = 0; i < b; i++)
	{
		int x0, y0, x1, y1;
		cin >> x0 >> y0 >> x1 >> y1;

		for(int y = y0; y <= y1; y++)
		{
			for(int x = x0; x <= x1; x++)
			{
				river[x][y] = 0;
			}
		}
	}

	for(int y = 0; y < h; y++)
	{
		for(int x = 0; x < w; x++)
		{
			int nodeIn = x + y * w;
			int nodeOut = nodeIn + w * h;

			nodes[nodeIn].routesTo.insert(nodeOut);

			tryConn(x, y, x - 1, y);
			tryConn(x, y, x + 1, y);
			tryConn(x, y, x, y - 1);
			tryConn(x, y, x, y + 1);
		}
	}

	for(int x = 0; x < w; x++)
	{
		nodes[w * h * 2].routesTo.insert(x);
		nodes[w * h + (h - 1) * w + x].routesTo.insert(w * h * 2 + 1);
	}

	maxFlow();
}

int main()
{
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}

	return 0;
}