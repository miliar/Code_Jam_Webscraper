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
const int N = 10100;

int a[N];

int main() {
	int tests;
	scanf("%d", &tests);
	for1 (it, tests) {
		int n, x;
		scanf("%d%d", &n, &x);
		forn (i, n)
			scanf("%d", &a[i]);
		sort(a, a + n);
		int lf = 0, rg = n - 1;
		int c = 0;
		while (lf <= rg) {
			if (a[lf] + a[rg] <= x) {
				++c;
				++lf;
				--rg;
			} else {
				++c;
				--rg;
			}
		}
		printf("Case #%d: %d\n", it, c);
	}
    return 0;
}
