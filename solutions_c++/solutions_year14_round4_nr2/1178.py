#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cassert>
#include <memory.h>
#include <ctype.h>
  
#include <iostream>
  
#include <string>
#include <complex>
#include <numeric>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <sstream>
  
using namespace std;
  
template<typename TYPE> inline TYPE sqr(const TYPE& a) { return (a) * (a); }
  
#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define pb push_back
#define mp make_pair
#define all(v) (v).begin(), (v).end()
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
  
typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;
  
const int INF = 1000 * 1000 * 1000;
const ld EPS = 1e-9;
const ld PI = 2 * acos(0.0);
const int N = 1010;

int a[N];
int b[N];
int c[N];
int d[N];
int di[N];

bool comp1(int x, int y) {
	return b[x] < b[y];
}

bool comp2(int x, int y) {
	return d[x] > d[y];
}

int solve(int n, int id) {
	int mend = 1 << id;
	int res = INF;
	forn (mask, mend) {
		//printf("= move: ");
		int bt = 0;
		int dt = 0;
		int cnt = 0;
		for (int i = id - 1; i >= 0; --i)
			if (mask & (1 << i)) {
				c[bt] = bt;
				b[bt] = a[i];
				++bt;
			} else {
				//printf("%d ", a[i]);
				d[dt] = a[i];
				di[dt] = dt;
				++dt;
				cnt += 1 + bt;
			}
		//printf("\n rest +%d\n", cnt);
		reverse(b, b + bt);
		reverse(d, d + dt);
		sort(c, c + bt, comp1);
		int temp = 0;
		forn (i, bt) {
			forn (j, i)
				if (c[j] > c[i])
					++temp;
		}
		//printf("sort left: +%d\n", temp);
		cnt += temp;
		for (int i = id + 1; i < n; ++i) {
			d[dt] = a[i];
			di[dt] = dt;
			++dt;
		}
		/*printf("right: ");
		forn (i, dt)
			printf("%d ", d[i]);
		printf("\n");
		*/
		sort(di, di + dt, comp2);
		temp = 0;
		forn (i, dt)  {
			forn (j, i)
				if (di[j] > di[i])
					++temp;
		}
		//printf("sort right: +%d\n", temp);
		cnt += temp;
		//printf("= val %d\n", cnt);
		res = min(res, cnt);
	}
	return res;
}

int pe[N];
int nans;
void naive(int n) {
	forn (i, n)
		pe[i] = i;
	int res = INF;
	do {
		bool up = true;
		bool ok = true;
		
		forn (i, n - 1) {
			if (a[pe[i]] < a[pe[i + 1]]) {
				if (!up) {
					ok = false;
					break;
				}
			} else {
				if (up) {
					up = false;
				}
			}
		}
		if (ok) {
			int cnt = 0;
			forn (i, n)
				forn (j, i)
					if (pe[j] > pe[i])
						++cnt;
			if (0 && res > cnt) {
				printf("better: ");
				forn (i, n)
					printf("%d ", a[pe[i]]);
				printf(" => %d\n   ", cnt);
				forn (i, n)
					printf("%d ", pe[i]);
				printf("\n");
				res = cnt;
			}
			res = min(res, cnt);
		}
	} while (next_permutation(pe, pe + n));
	printf("naive: %d\n", res);
	nans = res;
}

int main() {
	int tests;
	scanf("%d", &tests);
	for1 (it, tests) {
		int n;
		scanf("%d", &n);
		int id = 0;
		forn (i, n) {
			scanf("%d", &a[i]);
			if (id != i && a[i] > a[id])
				id = i;
		}
		//naive(n);
		int ans = solve(n, id);
		reverse(a, a + n);
		//puts("reverse");
		id = n - 1 - id;
		ans = min(ans, solve(n, id));
		//assert(ans == nans);
		printf("Case #%d: %d\n", it, ans);
	}
    return 0;
}
