/*
 * A.cpp
 *
 *  Created on: Apr 12, 2014
 *      Author: Marwan
 */

#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> VI;
typedef vector<VI> VVI;

const int oo = (int) 1e9;
const ll ool = (ll) 1e17;
const double eps = 1e-7;
const double PI = acos(-1.0);

#define MP(x,y)		make_pair((x),(y))
#define SZ(x) 		((int)(x.size()))
#define min(x,y) 	(((x)<(y))?(x):(y))
#define max(x,y) 	(((x)>(y))?(x):(y))

int main() {
#ifndef ONLINE_JUDGE
	freopen("in.in", "rt", stdin);
	freopen("out.txt", "wt", stdout);
#endif	
	int t;
	cin >> t;
	for (int tt = 0; tt < t; tt++) {
		cout << "Case #" << tt + 1 << ": ";
		double c, f, x;
		cin >> c >> f >> x;
		double r = 2, res = 0;
		while (1) {
			double rem1 = x / r;
			double rem2 = c / r + x / (r + f);
			if (rem1 < rem2) {
				res += rem1;
				break;
			}
			res += c / r;
			r += f;
		}
		printf("%.7lf\n", res);
	}
	return 0;
}

