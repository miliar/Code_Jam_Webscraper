/*
 * cj2013a.cpp
 *
 *  Created on: Apr 13, 2013
 *      Author: ahmedfarag
 */

#include <algorithm>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iterator>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <bitset>
#include <cstring>
#include <climits>
#include <deque>
#include <utility>
#include <complex>
#include <numeric>
#include <functional>
#include <stack>
#include <iomanip>
#include <ctime>
#include <valarray>
//#include "vc.h"
//#ifdef _MSC_VER
//	#include <hash_set>
//	#include <hash_map>
//	using namespace stdext;
//#else
//	#if __GNUC__ > 2
//		#include <ext/hash_set>
//		#include <ext/hash_map>
//		using namespace __gnu_cxx;
//	#else
//		#include <hash_set>
//		#include <hash_map>
//	#endif
//#endif

using namespace std;

typedef stringstream ss;
typedef pair<int, int> pii;
typedef long long ll;

#define ALL(x) (x).begin(),(x).end()
#define RALL(x) (x).rbegin(),(x).rend()
#define SZ(x) (int)(x).size()
#define MEMSET(x,val) memset((x),(val),sizeof(x))
#define mp(x,y) make_pair(x,y)

#define OO 1e9
const double PI = acos(-1);
const double EPS = 1e-11;

#define MX 102
int dx[] = { 0, 0, 1, -1 };
int dy[] = { 1, -1, 0, 0 };
int h[MX][MX][MX], v[MX][MX][MX], pat[MX][MX];
int main() {

#ifndef ONLINE_JUDGE
	freopen("B-large.in", "r", stdin);
	freopen("b.out", "w", stdout);
#endif
	int t, n, m;
	scanf("%d", &t);

	for (int tt = 1; tt <= t; ++tt) {
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				scanf("%d", pat[i]+j);
			}
		}

		bool ok = true;
		for (int i = 1; i < MX && ok; ++i) {
			for (int j = 0; j < n; ++j) {
				for (int k = 0; k < m; ++k) {
					h[i][j][k] =( k ? h[i][j][k - 1] : 0) + (pat[j][k] <= i);
					v[i][j][k] = (j ? v[i][j - 1][k] : 0) + (pat[j][k] <= i);
				}
			}
			for (int j = 0; j < n; ++j) {
				for (int k = 0; k < m; ++k) {
					if (pat[j][k] == i)
						if (h[i][j][m - 1] != m && v[i][n - 1][k] != n)
							ok = false;
				}
			}

		}

		printf("Case #%d: %s",tt, ok?"YES\n":"NO\n");
	}
	return 0;
}
