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

#define SZ 1024
int an[SZ];
int ad[SZ];
int add[SZ];
int ap[SZ];
int adp[SZ];
int as[SZ];
int ads[SZ];
int al[SZ];

//#define SZP 1000
//int a0[SZP*2];
//int *a = a0 + SZP;
//
//int query(int b, int e) {
//	int s = a[b];
//	for (int p = b; p < e; p++)
//		s = min(s, a[p]);
//	return s;
//}
//
//void raise(int b, int e, int s) {
//	for (int p = b; p < e; p++)
//		a[p] = max(a[p], s);
//}

int sz; // bucket size
vector<int> vb; // bucket minimum
vector<int> va; // all

void update(int i) {
	if (i < 0 || i >= (int) vb.size()) return;
	int b = i * sz;
	int e = (i+1) * sz;
	int s = 1000000000;
	for (int p = b; p < e; p++)
		s = min(s, va[p]);
	vb[i] = max(vb[i], s);
}

int query(int b, int e) {
	int qb = b / sz + 1;
	int qe = e / sz;
	int s = 1000000000;
	for (int i = qb; i < qe; i++) {
		s = min(s, vb[i]);
	}
	int le = min(e, qb * sz);
	for (int p = b; p < le; p++)
		s = min(s, max(vb[qb-1], va[p]));
	int rb = max(b, qe * sz);
	for (int p = rb; p < e; p++)
		s = min(s, max(vb[qe], va[p]));
	return s;
}

void raise(int b, int e, int s) {
	int qb = b / sz + 1;
	int qe = e / sz;
	for (int i = qb; i < qe; i++) {
		vb[i] = max(vb[i], s);
	}
	int le = min(e, qb * sz);
	for (int p = b; p < le; p++)
		va[p] = max(va[p], s);
	int rb = max(b, qe * sz);
	for (int p = rb; p < e; p++)
		va[p] = max(va[p], s);
	update(qb-1);
	update(qe);
}

int main() {
	//freopen("in.txt", "r", stdin);
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int T; scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		int n; scanf("%dn", &n);
		for (int i = 0; i < n; i++) {
			scanf("%d %d %d %d %d %d %d %d", ad+i, an+i, ap+i, al+i, as+i, add+i, adp+i, ads+i);
			al[i] = al[i] - ap[i];
		}
		set<pii> events;
		set<int> xvals;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < an[i]; j++) {
				events.insert(pii(ad[i] + j * add[i], i));
				xvals.insert(ap[i] + j * adp[i]);
				xvals.insert(ap[i] + j * adp[i] + al[i]);
			}
		}
		map<int, int> xmap;
		int v = 0;
		for (auto it = xvals.begin(); it != xvals.end(); it++) {
			xmap[*it] = v++;
		}
		
		sz = isqrtc(xvals.size());
		vb.assign(xvals.size() / sz + 1, 0);
		va.assign(vb.size() * sz, 0);
		
		int r = 0;
		while (!events.empty()) {
			int d = events.begin()->first;
			for (auto it = events.begin(); it != events.end() && it->first == d; it++) {
				int i = it->second;
				r += (query(xmap[ap[i]], xmap[ap[i] + al[i]]) < as[i]);
			}
			for (auto it = events.begin(); it != events.end() && it->first == d; it++) {
				int i = it->second;
				raise(xmap[ap[i]], xmap[ap[i] + al[i]], as[i]);
				as[i] += ads[i];
				ap[i] += adp[i];
			}
			for (auto it = events.begin(); it != events.end() && it->first == d;) {
				events.erase(it++);
			}
		}
		printf("Case #%d: %d\n", t, r);
	}
	return 0;
}
