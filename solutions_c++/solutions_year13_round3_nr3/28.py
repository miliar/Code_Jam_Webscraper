#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <bitset>
#include <queue>
#include <sstream>
using namespace std;
#define clr(a,x) memset(a, x, sizeof(a))
#define all(v) (v).begin(), (v).end()
#define iter(v) __typeof((v).begin())
#define foreach(it, v) for (iter(v) it = (v).begin(); it != (v).end(); it++)
#define pb push_back
#define mp make_pair
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for (int i = (int)(a); i <= (b); i++)
typedef long long ll;
typedef pair <int,int> PII;
ll sqr(ll x) {return x * x;}
template <class T> void checkmax(T &t, T x){if (x > t) t = x;}
template <class T> void checkmin(T &t, T x){if (x < t) t = x;}
template <class T> void _checkmax(T &t, T x){if (t == -1 || x > t) t = x;}
template <class T> void _checkmin(T &t, T x){if (t == -1 || x < t) t = x;}
ll power_mod(ll a, int b, int p) {
	ll ret = 1;
	for (; b; b >>= 1) {
		if (b & 1) ret = ret * a % p;
		a = a * a % p;
	}
	return ret;
}

const int N = 1005;
const int M = 676065;
int Tc;
int n;

struct Att {
	int l, r, v;
	Att(int l, int r, int v)
		:l(l), r(r), v(v) {}
};
struct Tri {
	int d, n, l, r, v, d_d, d_x, d_v;
	void read() {
		cin >> d >> n >> l >> r >> v >> d_d >> d_x >> d_v;
	}
}a[N];

vector < Att > event[M];

struct Node {
	int l, r, res, tag;
	Node *lc, *rc;

	void pd() {
		if (tag) {
			if (lc) lc->tag = max(lc->tag, tag);
			if (rc) rc->tag = max(rc->tag, tag);
			res = max(res, tag);
			tag = 0;
		}
	}

	void up() {
		if (!lc || !rc) return;
		res = min(max(lc->res, lc->tag), max(rc->res, rc->tag));
	}
}mem[80000000], *C, *root;

Node *newNode(int l, int r) {
	C->l = l;
	C->r = r;
	C->res = 0;
	C->tag = 0;
	C->lc = C->rc = NULL;
	return C++;
}

int getMin(Node *p, int l, int r) {
	int mid = (p->l + p->r) / 2;
	if (p->l + 1 < p->r) {
		if (!p->lc) p->lc = newNode(p->l, mid);
		if (!p->rc) p->rc = newNode(mid, p->r);
	}
	p->pd();
	if (l <= p->l && p->r <= r)
		return p->res;
	int res = 0x7FFFFFFF;
	if (l < mid) res = min(res, getMin(p->lc, l, r));
	if (r > mid) res = min(res, getMin(p->rc, l, r));
	return res;
}

void setTag(Node *p, int l, int r, int tag) {
	int mid = (p->l + p->r) / 2;
	if (p->l + 1 < p->r) {
		if (!p->lc) p->lc = newNode(p->l, mid);
		if (!p->rc) p->rc = newNode(mid, p->r);
	}
	p->pd();
	if (l <= p->l && p->r <= r) {
		p->tag = tag;
		return;
	}
	if (l < mid) setTag(p->lc, l, r, tag);
	if (r > mid) setTag(p->rc, l, r, tag);
	p->up();
}

int main() {
	freopen("C-large.in", "r", stdin);
	scanf("%d", &Tc);
	rep (ri, Tc) {
		rep (i, M) event[i].clear();
		printf("Case #%d: ", ri + 1);
		scanf("%d", &n);
		rep (i, n) {
			a[i].read();
			int d = a[i].d;
			int l = a[i].l;
			int r = a[i].r;
			r--;
			int v = a[i].v;
			rep (j, a[i].n) {
				event[d].pb(Att(l, r, v));
				d += a[i].d_d;
				l += a[i].d_x;
				r += a[i].d_x;
				v += a[i].d_v;
			}
		}
		C = &mem[0];
		root = newNode(-1000000000, 1000000000);
		int ans = 0;
		rep (i, M) {
			foreach (it, event[i]) {
				//printf("time %d;  %d %d %d\n", i, it->l, it->r, it->v);
				int res = getMin(root, it->l, it->r + 1);
				if (res < it->v) ans++;
			}
			foreach (it, event[i]) {
				setTag(root, it->l, it->r + 1, it->v);
			}
		}
		cout << ans << endl;
	}
	return 0;
}

