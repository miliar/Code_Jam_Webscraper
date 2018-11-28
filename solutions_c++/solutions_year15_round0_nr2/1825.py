#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <numeric>
#include <cctype>
#include <tuple>
#include <array>
#include <climits>
#include <bitset>
#include <cassert>
#include <unordered_map>

#ifdef _MSC_VER
#include <agents.h>
#endif

#define FOR(i, a, b) for(int i = (a); i < (int)(b); ++i)
#define rep(i, n) FOR(i, 0, n)
#define ALL(v) v.begin(), v.end()
#define REV(v) v.rbegin(), v.rend()
#define MEMSET(v, s) memset(v, s, sizeof(v))
#define UNIQUE(v) (v).erase(unique(ALL(v)), (v).end())
#define MP make_pair
#define MT make_tuple

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> P;

int main(){
	cin.tie(0);
	ios::sync_with_stdio(false);
	cout.setf(ios::fixed);
	cout.precision(20);

	int t;
	cin >> t;
	for (int cn = 1; cn <= t; ++cn){
		int d;
		cin >> d;
		vector<int> p(d);
		rep(i, d) cin >> p[i];

		int ans = *max_element(ALL(p));
		for (int i = 1; i <= 1000; ++i){
			int res = 0;
			for (int j = 0; j < d; ++j){
				res += max(0, (p[j] - 1) / i);
			}
			ans = min(ans, res + i);
		}
		cout << "Case #" << cn << ": " << ans << endl;
	}

}
