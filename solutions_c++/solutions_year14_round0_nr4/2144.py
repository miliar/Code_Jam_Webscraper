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
#include <unordered_map>

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

int fy(vector<double> a, vector<double> b) {
	set<double> _a(a.begin(), a.end());
	int ans = 0;
	FOR(i, sz(b)) {
		auto it = _a.lower_bound(b[i]);
		if (it == _a.end()) {
			_a.erase(_a.begin());
		} else {
			ans++;
			_a.erase(it);
		}
	}
	return ans;
}

int fz(vector<double> a, vector<double> b) {
	int ans = 0;
	set<double> _b(b.begin(), b.end());
	for(int i = sz(a) - 1; i >= 0; i--){
		auto it = _b.lower_bound(a[i]);
		if (it == _b.end()) {
			ans++;
			_b.erase(_b.begin());
		} else {
			_b.erase(it);
		}
	}
	return ans;
}

int main(){
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int n; cin >> n;
		vector<double> a(n), b(n);
		FOR(i, n) cin >> a[i];
		FOR(i, n) cin >> b[i];
		sort(a.begin(), a.end());
		sort(b.begin(), b.end());

		int y = fy(a, b);
		int z = fz(a, b);

		printf("Case #%d: %d %d\n", t, y, z);
	}

	return 0;
}
