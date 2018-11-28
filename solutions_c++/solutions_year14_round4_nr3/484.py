#include <cstdio>
#include <algorithm>
#define mp make_pair
#define pb push_back
#define fir first
#define sec second
using namespace std;
typedef long long ll;

template<typename T> inline void R(T &x) {
	char ch = getchar(); x = 0;
	for (; ch<'0'; ch=getchar());
	for (; ch>='0'; ch=getchar()) x = x*10+ch-'0';
}
const int N = 10000005, M = 10000005, inf = (1 << 30) - 1;
namespace G {
	struct edge{int s, e, c; edge *nxt; } es[M], *fr[N];
	struct node{int h; edge *se, *ce;} ns[N];
	int n, S, T, nes, l[N], Gap[N], aug[N];
	bool v[N];
	inline void clear() { // If multiple test case
		for (int i=0; i<=n; ++i)
			ns[i].se = ns[i].ce = NULL, ns[i].h = 0,
			v[i] = false, Gap[i] = 0;
		Gap[n+1] = 0;
	}
	inline void init(int _n, int _s, int _t) {
		n = _n, S = _s, T = _t;
		nes = 1;
	}
	inline void NE(int s, int e, int c) {
		edge *x;
		x = &es[++nes]; x->s = s, x->e = e, x->c = c, x->nxt = ns[s].se, ns[s].se = x;
		x = &es[++nes]; x->s = e, x->e = s, x->c = 0, x->nxt = ns[e].se, ns[e].se = x;
		//printf("%d\n", nes);
	}
	inline void bfs() {
		int ls = 1, le = 1;
		node *x;
		l[1] = T; v[T] = true; 
		for (; ls<=le; ++ls) {
			x = &ns[l[ls]];
			for (edge *w=x->se; w; w=w->nxt)
				if (!v[w->e])
					l[++le] = w->e,
					v[w->e] = true,
					ns[w->e].h = x->h + 1;
		}
		for (int i=1; i<=n; ++i)
			++Gap[ns[i].h];
	}
	inline int sap() {
		bfs();
		int x = S, flow, to, ans = 0; bool found; edge *mf;
		for (int i=1; i<=n; ++i)
			ns[i].ce = ns[i].se;
		fr[S] = NULL, aug[S] = inf;
		while (ns[S].h <= n) {
			if (x == T) {
				ans += flow = aug[T];
				for (edge *w=fr[T]; w; w=fr[w->s])
					w->c -= flow,
					(es+((w-es)^1))->c += flow;
				x = S;
			}
			found = false;
			for (edge *w=ns[x].ce; w; w=w->nxt) {
				to = w->e;
				if (w->c && ns[to].h + 1 == ns[x].h) {
					aug[to] = min(aug[x], w->c),
					fr[to] = w, ns[x].ce = w;
					x = to; found = true; break;
				}
			}
			if (!found) {
				int min = n; mf = NULL;
				for (edge *w=ns[x].se; w; w=w->nxt)
					if (w->c && ns[w->e].h < min)
						min = ns[w->e].h,
						mf = w;
				if (!--Gap[ns[x].h]) break;
				++Gap[ns[x].h = min + 1];
				ns[x].ce = mf;
				if (x != S) x = fr[x]->s;
			}
		}
		return ans;
	}
}
int n, m, r, cnt, l[2005];
bool can[1005][2005];
struct rec {
	int x1, y1, x2, y2;
	inline void read() {
		R(x1); R(y1); R(x2); R(y2);
		++y2;
		l[cnt++] = y1, l[cnt++] = y2;
	}
	inline void draw() {
		for (int i=x1; i<=x2; ++i)
			for (int j=y1; j<y2; ++j)
				can[i][j] = 0;
	}
} a[1005];
inline int pos(int x, int y, int dir) {
	return ((x*m+y)<<1)+dir+1;
}
inline void NE(int x1, int y1, int x2, int y2, int c) {
	if (!can[x1][y1]) return;
	if (!can[x2][y2]) return;
	if (x1 >= n || x2 >= n) return;
	if (y1 >= m || y2 >= m) return;
	G::NE(pos(x1, y1, 1), pos(x2, y2, 0), c);
	G::NE(pos(x2, y2, 1), pos(x1, y1, 0), c);
}
bool print = 0;
void run() {
	G::clear();
	R(n); R(m); R(r);
	if (print) printf("%d %d %d\n", n, m, r);
	cnt = 0;
	l[cnt++] = 0;
	l[cnt++] = m;
	for (int i=1; i<=r; ++i) a[i].read();
	//bf
	for (int i=0; i<=m; ++i) l[i] = i;
	cnt = m+1;
	//end bf
	sort(l, l+cnt);
	cnt = unique(l, l+cnt) - l;
	m = lower_bound(l, l+cnt, m) - l;
	for (int i=1; i<=r; ++i) {
		a[i].y1 = lower_bound(l, l+cnt, a[i].y1) - l;
		a[i].y2 = lower_bound(l, l+cnt, a[i].y2) - l;
	}
	for (int i=0; i<n; ++i)
		for (int j=0; j<m; ++j)
			can[i][j] = 1;
	int tot = n*m*2, S = tot+1, T = S + 1;
	G::init(T, S, T);
	for (int i=1; i<=r; ++i)
		a[i].draw();
	for (int i=0; i<n; ++i)
		for (int j=0; j<m; ++j)
			if (can[i][j]) {
				G::NE(pos(i, j, 0), pos(i, j ,1), l[j+1]-l[j]);
				NE(i, j, i, j+1, 1);
				NE(i, j, i+1, j, l[j+1]-l[j]);
			}
	for (int i=0; i<n; ++i)
		G::NE(S, pos(i, 0, 0), 1),
		G::NE(pos(i, m-1, 1), T, 1);
	printf("%d\n", G::sap());
}
int main() {
	int T; R(T);
	for (int i=1; i<=T; ++i) {
		//print = (i == 57);
		printf("Case #%d: ", i);
		run();
	}
	return 0;
}
