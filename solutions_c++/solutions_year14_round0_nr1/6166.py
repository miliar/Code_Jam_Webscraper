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
	freopen ("out.txt", "wt", stdout);
#endif	
	int t;
	cin >> t;
	for (int tt = 0; tt < t; tt++) {
		cout << "Case #" << tt+1 << ": ";
		set<int> s[3];
		int r, a;
		for (int idx = 0; idx < 2; idx++) {
			cin >> r;
			for (int i = 0; i < 4; i++)
				for (int j = 0; j < 4; j++) {
					cin >> a;
					if (i + 1 == r)
						s[idx].insert(a);
				}
		}

		set_intersection(s[0].begin(), s[0].end(),
						 s[1].begin(), s[1].end(),
						 inserter(s[2], s[2].begin()));

		if (s[2].empty()) {
			cout << "Volunteer cheated!" << endl;
		} else if (s[2].size() == 1) {
			cout << *s[2].begin() << endl;
		} else {
			cout << "Bad magician!" << endl;
		}
	}
	return 0;
}

