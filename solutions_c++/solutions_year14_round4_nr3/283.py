

#include <deque>
#include <queue>
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
#include <set>
#include <cstdlib>
#include <hash_map>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <map>
#include <cstdlib>
#include <cassert>
#include <ctime>

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;

#define rep(i,s,e) for(int i=s;i<e;i++)
#define sz(X) ((int)(X.size()))
#define tr(it,x) for(typeof(x.begin()) it=x.begin();it!=x.end();++it)
#define all(x) x.begin(),x.end()
#define clr(x,c) memset(x,c,sizeof(x))
//---------------------------------------------------------------

#define inf 1000000000

//最大流 dinic  http://acm.hdu.edu.cn/showproblem.php?pid=3046已AC
template <typename FLOW_TYPE = int, int MAXN = 20010, int MAXE = 60000> struct Netflow{
	int L[MAXN], Q[MAXN]; //L=level  Q=queue
	struct Edge{ int v, x;  FLOW_TYPE c; }E[MAXE]; //c:剩余可增广的流量capacity
	int X[MAXN], e; //邻接表
	void init() { 
		e=0; memset(X,-1,sizeof(X));  
	}
	void add_edge(int u, int v, FLOW_TYPE f, FLOW_TYPE invf){ //u->v=f   v->u=invf
		//printf("%d --> %d %d\n", u, v, f);
		E[e].v=v; E[e].c=f;   E[e].x=X[u]; X[u]=e++;
		E[e].v=u; E[e].c=invf;E[e].x=X[v]; X[v]=e++;
	}
	bool _bfs(int S, int T){ //从S开始广搜, 并标记level(只取流量大于0的边)
		int head = 0, tail = 0;
		memset(L, -1, sizeof(L));
		L[S] = 0; Q[tail++] = S;
		while (head < tail){
			int u = Q[head++];
			for (int x = X[u]; x >= 0; x = E[x].x)
				if (E[x].c>0 && L[E[x].v]==-1)
					L[(Q[tail++] = E[x].v)] = L[u] + 1;
		}
		return L[T] != -1;
	}
	FLOW_TYPE _find(int u, FLOW_TYPE in, int T) { //in:能流入u节点的最大流量. 返回u节点能流出的最大流量
		if (u == T) return in;
		FLOW_TYPE tmp, w = 0; //w表示已经从u流出的总流量
		for (int x = X[u]; x >= 0 && w < in; x = E[x].x) {
			if (E[x].c>0 && L[E[x].v]==L[u]+1) {
				if (tmp = _find(E[x].v, min(E[x].c,in-w), T)) {
					E[  x].c -= tmp;
					E[x^1].c += tmp; //这里表示必须
					w += tmp;        //多路增广优势巨大
				}
			}
		}
		if(w < in) L[u] = -1;//关键的一句话
		return w;
	}
	FLOW_TYPE dinic(int S, int T){ //在当前的残余网络求S到T的最大流
		FLOW_TYPE f, res = 0;
		while (_bfs(S, T)) while (f = _find(S, inf, T)) res += f;
		return res;
	}
}; //********模板结束***********
Netflow<int, 4100000, 40000000> flow;
// 使用方法:
// flow.init();
// flow.add_edge(0, 1, 1, 0);
// flow.add_edge(1, 2, 2, 0);
// cout<<flow.dinic(0, 2)<<endl;

struct Rect{
	int x0, y0, x1, y1;
	Rect(int _x0=0, int _y0=0, int _x1=0, int _y1=0):
		x0(_x0), y0(_y0),x1(_x1),y1(_y1) {};
};

int mat[4000][1010];
int id1[4000][1010], id2[4000][1010];

int dir[4][2] = {0,1, 1,0, 0,-1, -1,0};

int main() {
	freopen("F:/TDDOWNLOAD/C-small-attempt1.in", "r", stdin);
	freopen("F:/TDDOWNLOAD/C-small-attempt1.out", "w", stdout);

	int Te;
	cin>>Te;
	for(int te=1;te<=Te;te++) {
		int W, H, B;
		cin>>W>>H>>B;
		vector<int> h;
		set<int> st;
		st.insert(0);
		st.insert(H);

		rep(i, 0, H) st.insert(i);

		vector<Rect> recs; 
		rep(i, 0, B) {
			int x0, y0, x1, y1;
			cin>>x0>>y0>>x1>>y1;
// 			x0 = rand()%W;
// 			y0 = rand()%H;
// 			x1 = rand()%W;
// 			y1 = rand()%H;
// 			if(x0>x1) swap(x0, x1);
// 			if(y0>y1) swap(y0, y1);

			recs.push_back(Rect(x0, y0, x1, y1));
			st.insert(y0);
			st.insert(y1+1);
		}
		h = vector<int>(all(st));
		map<int, int> mp;
		rep(i, 0, sz(h)) {
			mp[h[i]] = i;
		}

		clr(mat, 0);
		rep(r, 0, sz(recs)) {
			int yid0 = mp[recs[r].y0];
			int yid1 = mp[recs[r].y1+1];
			rep(i, yid0, yid1) rep(j, recs[r].x0, recs[r].x1+1) {
				mat[i][j] = 1;
			}
		}
		flow.init();
		int src = 0, cnt = 1;
		clr(id1, -1);
		clr(id2, -1);
		for(int i=0;i<sz(h);i++) if(h[i]!=H) {
			for(int j=0;j<W;j++) if(mat[i][j]==0) {
				id1[i][j] = cnt++;
				id2[i][j] = cnt++;
			}
		}
		int sink = cnt++;
		for(int i=0;i<sz(h);i++) if(h[i]!=H) {
			for(int j=0;j<W;j++) if(mat[i][j]==0) {
				if(h[i]==0) {
					flow.add_edge(src, id1[i][j], 1, 0);
				}
				if(h[i+1]==H) {
					flow.add_edge(id2[i][j], sink, 1, 0);
				}
				flow.add_edge(id1[i][j], id2[i][j], h[i+1]-h[i], 0);
				
				rep(in, 0, 4) {
					int ti = i + dir[in][0];
					int tj = j + dir[in][1];
					if(ti<0 || ti>=sz(h)-1 || tj<0 || tj>=W || mat[ti][tj]) 
						continue;
					if(in==0 || in==2) {
						flow.add_edge(id2[i][j], id1[ti][tj], h[i+1]-h[i], 0);
					} else {
						flow.add_edge(id2[i][j], id1[ti][tj], 1, 0);
					}
				}
			}
		}

		printf("Case #%d: ", te);
		cout<<flow.dinic(src, sink)<<endl;
	}
}








