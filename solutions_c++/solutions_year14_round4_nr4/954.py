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
const int N = 8;

char buf[1024];
string sm[N];
int nodes[1 << N];
int b[N];
int g[5];
int wst, wcount;

void rec(int m, int n, int w) {
	if (w >= m) {
		int val = 0;
		bool ok = true;
		forn (i, n) {
			if (g[i] == 0) {
				ok = false;
				break;
			}
			val += nodes[g[i]];
		}
		if (!ok)
			return;
		if (val > wst) {
			wst = val;
			wcount = 1;
		} else if (val == wst) {
			++wcount;
		}
		return;
	}
	forn (i, n) {
		g[i] |= 1 << w;
		rec(m, n, w + 1);
		g[i] ^= 1 << w;
	}
}

int main() {
	int tests;
	scanf("%d", &tests);
	for1 (it, tests) {
		int m, n;
		scanf("%d%d\n", &m, &n);
		forn (i, m) {
			scanf("%s\n", buf);
			sm[i] = string(buf);
		}
		int mend = 1 << m;
		forn (mask, mend) {
			int c = 1;
			int bt = 0;
			forn (i, m)
				if (mask & (1 << i)) {
					int most = 0;
					forn (j, bt) {
						size_t rg = 0;
						int other = b[j];
						while (rg < sm[i].size() && rg < sm[other].size() &&
							sm[i][rg] == sm[other][rg])
							++rg;
						most = max(most, (int) rg);
					}
					c += int(sm[i].size()) - most;
					b[bt++] = i;
				}
			//printf("mask %d => %d node(s)\n", mask, c);
			nodes[mask] = c;
		}
		wst = 0;
		wcount = 0;
		rec(m, n, 0);
		printf("Case #%d: %d %d\n", it, wst, wcount);
	}
    return 0;
}
