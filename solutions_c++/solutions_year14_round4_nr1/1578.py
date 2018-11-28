#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cfloat>
#include <ctime>
#include <cassert>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <numeric>
#include <list>
#include <iomanip>
#include <fstream>
#include <iterator>

using namespace std;
const int MOD = 1000000007; // check!!!
const int INF = 100000000; //1e8

typedef long long ll;
typedef pair<int, int> Pii;
typedef pair<ll, ll> Pll;

#define FOR(i,n) for(int i = 0; i < (n); i++)
#define sz(c) ((int)(c).size())
#define ten(x) ((int)1e##x)
#define tenll(x) ((ll)1e##x)


int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int n, x; cin >> n >> x;
		multiset<int> v;
		FOR(i, n) {
			int s; cin >> s;
			v.insert(s);
		}

		int ans = 0;
		while (sz(v)) {
			auto it= v.end();
			it--;
			int val = *it;
			v.erase(it);
			if (sz(v) == 0) {
				ans++;
				break;
			}
			auto it2 = v.upper_bound(x - val);
			if(it2 != v.begin()) it2--;
			if (*it2 + val <= x) {
				v.erase(it2);
			}
			ans++;
		}

		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
