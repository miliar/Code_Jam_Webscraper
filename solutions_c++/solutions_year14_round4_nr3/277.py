#include <iostream>
#include <vector>

using namespace std;

const int MAX_V = 1024*1024;
struct edge { int to, cap, rev; };

vector<edge> G[MAX_V];
bool used[MAX_V];

void add_edge(int from, int to, int cap)
{
	//printf("%d %d %d\n", from, to, cap);

	edge e;
	e.to = to;
	e.cap = cap;
	e.rev = G[to].size();
	G[from].push_back(e);
	e.to = from;
	e.cap = 0;
	e.rev = G[from].size()-1;
	G[to].push_back(e);
}

int dfs(int v, int t, int f)
{
	if (v==t)return f;
	used[v] = true;
	for(int i=0; i<G[v].size(); i++) {
		edge &e = G[v][i];
		if (!used[e.to] && e.cap>0)
		{
			int d = dfs(e.to, t, min(f, e.cap));
			if (d>0){
				e.cap -= d;
				G[e.to][e.rev].cap += d;
				return d;
			}
		}
	}
	return 0;
}

int max_flow(int s, int t)
{
	int flow = 0;
	for(;;){
		memset(used, 0, sizeof(used));
		int f = dfs(s, t, 0x7fffffff);
		if (f==0) return flow;
		flow += f;
	}
	return -1;
}




int main()
{
	int T;
	cin>>T;

	for (int test=1; test<=T; test++)
	{
		int W, H, B;
		cin>>W>>H>>B;
		vector<int> X0(B), Y0(B), X1(B), Y1(B);
		for (int b=0; b<B; b++)
			cin>>X0[b]>>Y0[b]>>X1[b]>>Y1[b];

		vector<vector<bool> > F(H, vector<bool>(W));
		for (int b=0; b<B; b++)
			for (int y=Y0[b]; y<=Y1[b]; y++)
			for (int x=X0[b]; x<=X1[b]; x++)
				F[y][x] = true;

		//for (int y=0; y<H; y++)
		//{
		//	for (int x=0; x<W; x++)
		//		printf("%d", int(F[y][x]));
		//	printf("\n");
		//}

		for (int i=0; i<MAX_V; i++)
			G[i].clear();
		int dx[] = {1, -1, 0, 0};
		int dy[] = {0, 0, 1, -1};
		

		for (int y=0; y<H; y++)
		for (int x=0; x<W; x++)
		if (!F[y][x])
		{
			int p = y*W+x;

			add_edge(p*2, p*2+1, 1);

			for (int d=0; d<4; d++)
			{
				int tx = x + dx[d];
				int ty = y + dy[d];
				if (0<=tx && tx<W &&
					0<=ty && ty<H && !F[ty][tx])
				{
					int q = ty*W+tx;

					add_edge(p*2+1, q*2, 1);
				}
			}
		}

		for (int x=0; x<W; x++)
		{
			if (!F[0][x])
				add_edge(W*H*2, x*2, 1);
			if (!F[H-1][x])
				add_edge(((H-1)*W+x)*2+1, W*H*2+1, 1);
		}

		int ans = max_flow(W*H*2, W*H*2+1);
		printf("Case #%d: %d\n", test, ans);
		fprintf(stderr, "Case #%d: %d\n", test, ans);
	}

	return 0;
}

	












