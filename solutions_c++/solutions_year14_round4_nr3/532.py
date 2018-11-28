#include <iostream>
#include <cstring>
#include <set>
#include <map>
#include <algorithm>
#include <string>
#include <queue>
#include <vector>
using namespace std;
#define ll long long
#define VI vector<int>
#define inf 1000000000
#define L(s) ((int)(s).size())
#define x first 
#define y second
#define pii pair<int, int>
#define mp make_pair
#define pb push_back
#define all(s) (s).begin(), (s).end()
const int E= 500 * 100 * 4 * 4 + 1000;
const int V= 500 * 100 * 2 + 10;
int e[E],nxt[E],cap[E];
int st[V],cur[V],h[V];
int ST,FN,n,m,ecnt;
inline void add_edge(int p,int q,int f1,int f2)
{
	e[ecnt]=q;cap[ecnt]=f1;nxt[ecnt]=st[p];st[p]=ecnt++;
	e[ecnt]=p;cap[ecnt]=f2;nxt[ecnt]=st[q];st[q]=ecnt++;
}
queue<int> q;
inline bool bfs()
{
	q.push(FN);
	for(int i = 0; i < n; ++i) 
		h[i]=-1;
	h[FN]=n;
	while(!q.empty())
	{
		int cur=q.front();
		q.pop();
		for(int pos=st[cur];pos!=-1;pos=nxt[pos])
			if (cap[pos^1]&&h[e[pos]]==-1)
			{
				h[e[pos]]=h[cur]-1;
				q.push(e[pos]);
			}
	}
	return h[ST]!=-1;
}
ll flow=0;
int add;
inline bool dfs(int v,int f)
{
	if (v==FN)
	{
		add=f;flow+=f;return true;
	}
	for(int &pos=cur[v];pos!=-1;pos=nxt[pos])
		if (h[e[pos]]==h[v]+1&&cap[pos]&&dfs(e[pos],min(f,cap[pos])))
		{
			cap[pos]-=add;
			cap[pos^1]+=add;
			return true;
		}
		return false;
}
int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};
int block[555][555], w, ht, b, t;
inline bool ok(int i, int j) {
	return i >= 0 && i < w && j >= 0 && j < ht;
}
int main() {
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for(int tc = 1; tc <= t; ++tc) {
		cerr << tc << endl;
		if (tc == 6) {
			tc = tc;
		}
		memset(block, 0, sizeof(block));
		scanf("%d%d%d", &w, &ht, &b);
		for(int i = 0; i < b; ++i) {
			int sx, sy, fx, fy;
			cin >> sx >> sy >> fx >> fy;
			for(int x = sx; x <= fx; ++x)
				for(int y = sy; y <= fy; ++y) 
					block[x][y] = 1;
		}
		ecnt = 0;
		ST = w * ht * 2;
		FN = ST + 1;
		n = FN + 1;
		memset(st, -1, sizeof(st));
		memset(cur, 0, sizeof(cur));
		memset(h, 0, sizeof(h));

		for(int x = 0; x < w; ++x) {
			add_edge(ST, x * ht + 0, 1, 0);
			add_edge(w * ht + x * ht + ht - 1, FN, 1, 0);
		}

		for(int x = 0; x < w; ++x) {
			for(int y = 0; y < ht; ++y) {
				if (!block[x][y]) {
					add_edge(x * ht + y, w * ht + x * ht + y, 1, 0);
				}
				for(int s = 0; s < 4; ++s) {
					int nx = x + dx[s];
					int ny = y + dy[s];
					if (!ok(nx, ny)) continue;
					add_edge(w * ht + x * ht + y, nx * ht + ny, 1, 0);
				}
			}
		}

		flow = 0;
		while(bfs())
		{
		//	cerr << "bfs " << endl;
			for(int i =  0; i < n; ++i)
				cur[i]=st[i];
			do
			{
				add=0;
			}
			while(dfs(ST,inf));
		}

		printf("Case #%d: %d\n", tc, flow);
	}
}
	