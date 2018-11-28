#define _CRT_SECURE_NO_DEPRECATE
//#define _CRT_RAND_S

//#include <windows.h>
//#include <tchar.h>
//#include <atlbase.h>
//#include <winerror.h>

#include <stdint.h>
#include <climits>
#include <ctime>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <map>
#include <set>
#include <list>
#include <queue>
#include <deque>
#include <string>
#include <bitset>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<ll, int> pli;
typedef pair<ll, ll> pll;

int64_t isq(int32_t x) { return int64_t(x)*x; }
int64_t isq(int64_t x) { return int64_t(x)*x; }
int32_t isqrt(int64_t x) { if (x <= 0) return 0; int32_t q = int32_t(floor(sqrt(double(x)))); while (isq(q) > x) q--; while (isq(q+1) <= x) q++; return q; }
int32_t isqrtc(int64_t x) { if (x <= 0) return 0; int32_t q = int32_t(ceil(sqrt(double(x)))); while (isq(q) < x) q++; while (q > 0 && isq(q-1) >= x) q--; return q; }

#define M 1000002013

#define SZ 1000
int va[SZ];
int vb[SZ];
int vp[SZ];

ll addmulmod(ll x, ll y, ll z, ll m) {
	return (x + y * z) % m;
}

ll mulmod(ll x, ll y, ll m) {
	return (x * y) % m;
}

int cost(int n, int k) {
	return int(mulmod(k, 2 * n - k + 1, M) / 2);
}

struct node {
	int pos;
	int cnt;
	node *prev;
	node *next;
};

node vn[2*SZ];

int main() {
	//freopen("in.txt", "r", stdin);
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int T; scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		int n, m; scanf("%d %d", &n, &m);
		ll r = 0;
		map<int, int> mx;
		for (int i = 0; i < m; i++) {
			scanf("%d %d %d", va+i, vb+i, vp+i);
			mx[va[i]] = mx[vb[i]] = -1;
			r = addmulmod(r, vp[i], cost(n, vb[i] - va[i]), M);
		}
		int c = 0;
		for (auto it = mx.begin(); it != mx.end(); it++) {
			it->second = c++;
			vn[it->second].pos = it->first;
		}
		for (int i = 0; i < m; i++) {
			vn[mx[va[i]]].cnt += vp[i];
			vn[mx[vb[i]]].cnt -= vp[i];
		}
		int n_sz = (int) mx.size();
		int i0; for (i0 = 0; i0 < n_sz && vn[i0].cnt == 0; i0++);
		node *head = 0;
		if (i0 < n_sz) {
			head = &vn[i0];
			head->prev = 0;
			head->next = 0;
		}
		for (int i = i0, j = 0; i < n_sz; i = j) {
			vn[i].next = 0;
			for (j = i + 1; j < n_sz && vn[j].cnt == 0; j++);
			if (j >= n_sz) break;
			vn[i].next = &vn[j];
			vn[j].prev = &vn[i];
		}
		set<int> s;
		for (node *t = head; t && t->next; t = t->next) {
			if (t->cnt > 0 && t->next->cnt < 0) s.insert(int(t - vn));
		}
		while (!s.empty()) {
			node *t = vn + *s.begin(); s.erase(s.begin());
			node *tn = t->next;
			int cnt = min(t->cnt, -tn->cnt);
			r = addmulmod(r, -cnt, cost(n, tn->pos - t->pos), M);
			t->cnt -= cnt;
			tn->cnt += cnt;
			node *tp = t->prev;
			node *tnn = tn->next;
			if (t->cnt == 0 && tn->cnt == 0) {
				if (tp && tnn && tp->cnt > 0 && tnn->cnt < 0) s.insert(int(tp - vn));
				if (tp) tp->next = tnn;
				if (tnn) tnn->prev = tp;
			}
			else if (t->cnt == 0) {
				if (tp && tp->cnt > 0) s.insert(int(tp - vn));
				if (tp) tp->next = tn;
				if (tn) tn->prev = tp;
			}
			else if (tn->cnt == 0) {
				if (tnn && tnn->cnt < 0) s.insert(int(t - vn));
				if (t) t->next = tnn;
				if (tnn) tnn->prev = t;
			}
		}
		printf("Case #%d: %d\n", t, r);
	}
	return 0;
}
