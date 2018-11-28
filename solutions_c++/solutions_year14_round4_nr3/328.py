// written by Amirmohsen Ahanchi //
#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <queue>
#include <cstring>
#include <cmath>

#define pb push_back
#define mp make_pair
#define f1 first
#define f2 second
#define X first
#define Y second
#define Size(n) ((int)(n).size())
#define Foreach(i, x) for (__typeof(x.begin()) i = x.begin(); i != x.end(); i++)
#define all(x) x.begin(),x.end()
#define rep(i, n) for (int i = 0; i < n; i++)
#define dbg(x) "#" << #x << ": " << x 
#define spc << " " <<

using namespace std;

//#define cin fin
//#define cout fout

typedef long long LL;
typedef pair <int, int> PII; 

const int maxN = 100 * 1000 + 10;
const int maxM = 500 * 1000 + 5;
const LL INF = (1ll << 55) + 5;

//LL f[maxN][maxN];
int to[maxM], prv[maxM], head[maxN];
int c[maxM], f[maxM];
int lvl[maxN], pnt[maxN];
int ecnt = 0;

int n;

#define min(x,y) (x<y?x:y)

int que[maxN];

inline bool bfs(int s, int t)
{
	rep(i, n) lvl[i] = -1;
	int sz = 0;
	que[sz++] = s;
	lvl[s] = 0;
	for (int q = 0; q < sz && lvl[t] == -1; q++)
	{
		int v = que[q];
		for (int i = head[v]; i != -1; i = prv[i])
		{
			int u = to[i];
			if (lvl[u] == -1 && c[i] > f[i])
			{
				lvl[u] = lvl[v]+1;
				que[sz++] = u;
				if (u == t) break;
			}
		}
	}
	return lvl[t] != -1;
}


LL dfs(int x, const int &t, LL mx = INF)
{
	if (x == t) return mx;
	LL res = 0;
	LL tmp;
	for (int &i = pnt[x]; i != -1; i = prv[i])
	{
		int u = to[i];
		if (lvl[u] == lvl[x]+1 && c[i] > f[i] && (tmp = dfs(u, t, min(mx, c[i]-f[i]))) )
		{
			f[i] += tmp;
			f[i^1] -= tmp;
			res += tmp;
			mx -= tmp;
			if (!mx) break;
		}
	}
	return res;
}

void edge(int u, int v, int w)
{
	to[ecnt] = v, c[ecnt] = w, prv[ecnt] = head[u], head[u] = ecnt++;
	to[ecnt] = u, c[ecnt] = 0, prv[ecnt] = head[v], head[v] = ecnt++;
}


const int maxH = 500 + 5;
int a[maxH][maxH];
int dx[] = {0, 1, 0, -1};
int dy[] = {1, 0, -1, 0};

int H, W, B;
int get(int x, int y) { return y*W+x;}

void clr(int N, int M)
{
	ecnt = 0;
//	for (int i = 0; i <= N; i++)	
//		head[i] = -1;
	memset(head, -1, sizeof head);
//	for (int i = 0; i <= M; i++)
//		f[i] = 0;
	memset(f, 0, sizeof f);
}


int main()
{
	// n == number of nodes
	ios_base::sync_with_stdio(false);
	int T; cin >> T;
	for (int tt = 0; tt < T; tt++)
	{
		cin >> W >> H >> B;
		rep(i, W) rep(j, H) a[i][j] = 0;
		clr(2*H*W+100, H*W*6+10);
		for (int i = 0; i < B; i++)
		{
			int x1, y1, x2, y2;
			cin >> x1 >> y1 >> x2 >> y2;
			for (int i = x1; i <= x2; i++)
				for (int j = y1; j <= y2; j++)
					a[i][j] = 1;
		}
		n = H*W;
		for (int i = 0; i < W; i++)
			for (int j = 0; j < H; j++)
				for (int dir = 0; dir < 2; dir++)
				{
					int v = get(i,j);
					int x = i+dx[dir], y = j+dy[dir];
					if (x >= W || y >= H || a[i][j] || a[x][y]) continue;
					int u = get(x, y);
//					cerr << u << " " << v << endl;
					edge(u+n, v, 1);
					edge(v+n, u, 1);
				}
		// voroodi v
		for (int i = 0; i < n; i++)
			edge(i, i+n, 1);
		int s = 2*n, t = 2*n+1;
		for (int i = 0; i < W; i++)
		{
			edge(s, get(i, 0), 1);
			edge(get(i, H-1)+n, t, 1);

		}
		LL ans = 0;
		n = 2*n+2;
		while (bfs(s, t))
		{
			rep(i, n) pnt[i] = head[i];
			ans += dfs(s, t);
		}
		cout << "Case #" << tt+1 << ": ";
		cout << ans << endl;

	}
	return 0;
}

