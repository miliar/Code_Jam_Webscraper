#include "cstdio"
#include "iostream"
#include "algorithm"
#include "cmath"
#include "cstring"
#include "cstdlib"
#include "climits"
#include "cassert"
#include "bitset"
#include "complex"
#include "queue"
#include "vector"
#include "queue"
#include "set"
#include "map"
#define runtime() ((long double)clock() / CLOCKS_PER_SEC)
#define rep(i, n) for(int i=0; i<n; i++)
#define repp(i, a, b) for(int i=a; i<a+b; i++)
using namespace std;
#define SZ(x) ((int)(x).size())
#define PB push_back
#define MK make_pair
#define X first
#define Y second
#define ll long long
#define ull unsigned long long
#define ITR iterator
#define LB lower_bound
#define UB upper_bound
#define PII pair<int, int>
#define CLR(a) memset(a, 0, sizeof(a))
int getint(){
    int s = 0, o = 1;
    char c;
    for(c = getchar(); c<'0'||c>'9';c = getchar()) if(c=='-') o = -1;
    for(;c>='0'&&c<='9'; c = getchar()) s *=10, s+=c-'0';
    return s*o;
}
  
const int maxn = 100010, maxe = (100010 + maxn) * 2;
int e[maxe], hd[maxn], nt[maxe], c[maxe], d[maxn], tot, cur[maxn];
int S, T, vis[maxn];
int aug(int u, int lim){
	if(u==T) return lim;
	int now = lim;
	for(int p = cur[u]; p; p = nt[p], cur[u] = p) if(c[p]>0 && d[u] == d[e[p]] + 1){
		int &v = e[p];
		int push = aug(v, min(now, c[p]));
		c[p] -= push;
		c[p^1] += push;
		now -= push;
		if(!now) break;
	}
	if(lim==now) d[u] = -1;//DINIC 有木有 10倍的效率啊 
	return lim - now;
}
bool label(){
	static int q[maxn];
	static int V = 0;
	q[0] = T;
	static int l, r;
	l = 0, r = 1;
	vis[T] = ++V; 
	while(l<r && vis[S]!=V){
		int u = q[l++];
		for(int p = hd[u]; p; p = nt[p]) if(c[p^1]>0){
			int v = e[p];
			if(vis[v]<V) d[v] = d[u] + 1, vis[v] = V, q[r++] = v;
		}
	}
	rep(i, r) cur[q[i]] = hd[q[i]];
	return vis[S]==V;
}
void add(int u, int v, int cc){
	e[++tot] = v, c[tot] = cc, nt[tot] = hd[u], hd[u] = tot;
	e[++tot] = u, c[tot] = 0, nt[tot] = hd[v], hd[v] = tot;
}

int need[maxn];
int main(int argc, char const *argv[])
{
	// freopen("transport.in", "r", stdin);
    // freopen("transport.out", "w", stdout); 
	int A,B,m,sum = 0, sum2 = 0;
	A = getint(), B = getint(), m = getint();
	S = A+B+1, T = S+1;
	repp(i,1,A+B) need[i] = getint();
	repp(i,1,A) sum += need[i];
	repp(i,1,B) sum2 += need[i+A];
	tot = 1;
	rep(mm,m){
		int x,y;
		#define norm(x) (x<0? -x: A+x)
		x = getint(), y = getint();
		x = norm(x), y = norm(y);
		add(x, y, sum);
	}
	repp(i,1,A) add(S, i, need[i]); 
	repp(i,1,B) add(i+A, T, need[i+A]);
	int flow = 0;
	while(label()) flow += aug(S, sum);
	if(flow==sum && flow==sum2){
		printf("YES\n");
		repp(i,1,m) printf("%d ", c[i<<1|1]);
	}else{
		printf("NO\n");
	}
	return 0;
}