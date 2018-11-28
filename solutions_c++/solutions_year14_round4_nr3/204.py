#include <bits/stdc++.h>
using namespace std;
const int oo = 27081993;
const int dx[] = {-1, 0, 1, 0};
const int dy[] = {0, 1, 0, -1};

struct edge
{
	int x, y, cap, flow;
};

struct DinicFlow
{
	int n, S, T;
	vector < vector <int> > a;
	vector <int> cur, d;
	vector <edge> e;
	
	DinicFlow() {}
	DinicFlow(int n, int S, int T)
	{
		this -> n = n;
		this -> S = S;
		this -> T = T;
		a = vector < vector <int> >(n + 1);
		cur = vector <int>(n + 1);
		d = vector <int>(n + 1);
	}
	
	void addEdge(int x, int y, int cap)
	{
		edge e1 = {x, y, cap, 0};
		edge e2 = {y, x, 0, 0};
		a[x].push_back(e.size()); e.push_back(e1);
		a[y].push_back(e.size()); e.push_back(e2);
	}
	
	int bfs()
	{
		queue <int> q;
		for (int i = 1; i <= n; i++) d[i] = -1;
		q.push(S); d[S] = 0;
		while (!q.empty() && d[T] < 0)
		{
			int x = q.front(); q.pop();
			for (int i = 0; i < int(a[x].size()); i++)
			{
				int id = a[x][i], y = e[id].y;
				if (d[y] < 0 && e[id].flow < e[id].cap)
					q.push(y), d[y] = d[x] + 1;
			}
		}
		return d[T] >= 0;
	}
	
	int dfs(int x, int val)
	{
		if (!val) return 0;
		if (x == T) return val;
		for (; cur[x] < int(a[x].size()); cur[x]++)
		{
			int id = a[x][cur[x]], y = e[id].y;
			if (d[y] != d[x] + 1) continue;
			int pushed = dfs(y, min(val, e[id].cap - e[id].flow));
			if (pushed)
			{
				e[id].flow += pushed;
				e[id ^ 1].flow -= pushed;
				return pushed;
			}
		}
		return 0;
	}
	
	int maxFlow()
	{
		int res = 0;
		while (bfs())
		{
			for (int i = 1; i <= n; i++) cur[i] = 0;
			while (1)
			{
				int val = dfs(S, oo);
				if (!val) break;
				res += val;
			}
		}
		return res;
	}	
};

int a[555][555], id[555][555];

int main()
{
	freopen("c.in", "r", stdin); 
	freopen("c.out", "w", stdout);
	int test;
	cin >> test;
	for (int noTest = 1; noTest <= test; noTest++)
	{
		cerr << noTest << endl;
		int W, H, n, x, y, xx, yy;
		cin >> W >> H >> n;
		int freeCells = 0;
		memset(a, 0, sizeof a);
		for (int i = 0; i < n; i++)
		{
			cin >> x >> y >> xx >> yy;
			for (int ix = x; ix <= xx; ix++)
				for (int iy = y; iy <= yy; iy++)
					a[ix][iy] = 1;
		}
		
		for (int i = 0; i < W; i++)
			for (int j = 0; j < H; j++)
				if (!a[i][j])
					id[i][j] = ++freeCells;
		
		int S = freeCells + 1, T = S + 1;
		DinicFlow f(T + freeCells, S, T);
		for (int i = 0; i < W; i++)
			for (int j = 0; j < H; j++)
				if (!a[i][j])
				{
					f.addEdge(id[i][j], id[i][j] + T, 1);
					for (int k = 0; k < 4; k++)
					{
						int ii = i + dx[k], jj = j + dy[k];
						if (ii >= 0 && ii < W && jj >= 0 && jj < H && !a[ii][jj])
							f.addEdge(id[i][j] + T, id[ii][jj], oo);
					}
				}
				
		for (int i = 0; i < W; i++)
		{
			if (!a[i][0]) f.addEdge(S, id[i][0] + T, 1);
			if (!a[i][H - 1]) f.addEdge(id[i][H - 1], T, oo);
		}
		
		printf("Case #%d: %d\n", noTest, f.maxFlow());
	}
}
