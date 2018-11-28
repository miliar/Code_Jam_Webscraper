#include<stdio.h>
#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<memory.h>
#include<map>
#include<set>
#include<queue>
#include<list>
#include<sstream>
#define mp make_pair
#define pb push_back      
#define F first
#define S second
#define SS stringstream
#define sqr(x) ((x)*(x))
#define m0(x) memset(x,0,sizeof(x))
#define m1(x) memset(x,63,sizeof(x))
#define CC(x) cout << (x) << endl
#define pw(x) (1ll<<(x))
#define M 1000000007
#define N 111111
using namespace std;
typedef pair<int,int> pt;

int n, m;
char fi[111][111];
int fr[222], to[222], did[222];

struct edge{
	int t, x, y;
	edge() {}
	edge(int tt, int xx, int yy) : t(tt), x(xx), y(yy) {}
};

edge pr[2][111][111];

vector<edge> path(edge a, edge b) {
	edge em = edge(-1, -1, -1);

	for (int i = 0; i < n + 1; i++) for (int j = 0; j < m; j++) pr[0][i][j] = em;
	for (int i = 0; i < n; i++) for (int j = 0; j < m + 1; j++) pr[1][i][j] = em;



	vector<edge> q;
	int q2 = 0;

	pr[a.t][a.x][a.y] = edge(-2, -2, -2);
	q.pb(a);
	while (q2 < q.size()) {
		edge w = q[q2++];

		if (w.t == 0) {
			if (w.x < n) {
				if (fi[w.x][w.y] != '\\') {
					edge to = edge(1, w.x, w.y);
					if (pr[to.t][to.x][to.y].t == -1) {
						pr[to.t][to.x][to.y] = w;
						q.pb(to); 
					}
				}
				if (fi[w.x][w.y] != '/') {
					edge to = edge(1, w.x, w.y + 1);
					if (pr[to.t][to.x][to.y].t == -1) {
						pr[to.t][to.x][to.y] = w;
						q.pb(to); 
					}
				}
			}
			if (w.x > 0) {
				if (fi[w.x - 1][w.y] != '\\') {
					edge to = edge(1, w.x - 1, w.y + 1);
					if (pr[to.t][to.x][to.y].t == -1) {
						pr[to.t][to.x][to.y] = w;
						q.pb(to); 
					}
				}
				if (fi[w.x - 1][w.y] != '/') {
					edge to = edge(1, w.x - 1, w.y);
					if (pr[to.t][to.x][to.y].t == -1) {
						pr[to.t][to.x][to.y] = w;
						q.pb(to); 
					}
				}
			}
		} else {
			if (w.y < m) {
				if (fi[w.x][w.y] != '\\') {
					edge to = edge(0, w.x, w.y);
					if (pr[to.t][to.x][to.y].t == -1) {
						pr[to.t][to.x][to.y] = w;
						q.pb(to); 
					}
				}
				if (fi[w.x][w.y] != '/') {
					edge to = edge(0, w.x + 1, w.y);
					if (pr[to.t][to.x][to.y].t == -1) {
						pr[to.t][to.x][to.y] = w;
						q.pb(to); 
					}
				}
			}
			if (w.y > 0) {
				if (fi[w.x][w.y - 1] != '\\') {
					edge to = edge(0, w.x + 1, w.y - 1);
					if (pr[to.t][to.x][to.y].t == -1) {
						pr[to.t][to.x][to.y] = w;
						q.pb(to); 
					}
				}
				if (fi[w.x][w.y- 1] != '/') {
					edge to = edge(0, w.x, w.y - 1);
					if (pr[to.t][to.x][to.y].t == -1) {
						pr[to.t][to.x][to.y] = w;
						q.pb(to); 
					}
				}
			}
		}
	}
	vector<edge> ret;
	int ff = pr[b.t][b.x][b.y].t;
	if (ff == -1) {
//		cerr << a.t << " " << a.x << " " << a.y << endl;
//		cerr << b.t << " " << b.x << " " << b.y << endl;
		return ret;
	}		
//	cerr << "! " << pr[b.t][b.x][b.y].t << endl;
	while (pr[b.t][b.x][b.y].t != -2) {
		ret.pb(b);
		edge f = edge(pr[b.t][b.x][b.y].t, pr[b.t][b.x][b.y].x, pr[b.t][b.x][b.y].y);
		b = f;
	}
	ret.pb(a);
	reverse(ret.begin(), ret.end());
	return ret;
}

int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		cin >> n >> m;
		vector<edge> e;
		for (int i = 0; i < m; i++) e.pb(edge(0, 0, i));
		for (int i = 0; i < n; i++) e.pb(edge(1, i, m));
		for (int i = m - 1; i >= 0; i--) e.pb(edge(0, n, i));
		for (int i = n - 1; i >= 0; i--) e.pb(edge(1, i, 0));


		vector<pair<int, int> > fr(e.size() / 2);
		for (int i = 0; i < e.size() / 2; i++) {
			cin >> fr[i].F >> fr[i].S;
			fr[i].F--;
			fr[i].S--;
		}			
		int good = 0;
		cout << "Case #" << tt << ": " << endl;
		for (int it = 0; it < pw(n * m); it++) {
			for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) 
				if (it & pw(i * m + j)) fi[i][j] = '/'; else fi[i][j] = '\\';

			int imp = 0;
			for (int it = 0; it < e.size() / 2; it++) if (!imp) {
				vector<edge> q = path(e[fr[it].F], e[fr[it].S]);
				if (q.size() == 0) {
					imp = 1;
					break;
				}
				continue;
				for (int i = 0; i + 1 < q.size(); i++) {
					int xx = q[i].x;
					int yy = q[i].y;
					if (q[i].t == 0) {
						if (q[i + 1].x == xx - 1) {
							if (q[i + 1].y == yy) fi[xx - 1][yy] = '\\'; else fi[xx - 1][yy] = '/';
						} else {
							if (q[i + 1].y == yy) fi[xx][yy] = '/'; else fi[xx][yy] = '\\';
						}
					} else {
						if (q[i + 1].y == yy - 1) {
							if (q[i + 1].x == xx) fi[xx][yy - 1] = '\\'; else fi[xx][yy - 1] = '/';
						} else {
							if (q[i + 1].x == xx) fi[xx][yy] = '/'; else fi[xx][yy] = '\\';
						}
					}
				}
			}
			if (!imp) {
				good = 1;
				for (int i = 0; i < n; i++) {
					for (int j = 0; j < m; j++) {
						if (fi[i][j] == '.') fi[i][j] = '/';
						putchar(fi[i][j]);
					}				
					puts("");
				}
				break;
			}

		}
		
		if (!good) cout << "IMPOSSIBLE\n";

	}
	return 0;
}