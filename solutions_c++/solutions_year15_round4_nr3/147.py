#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <limits>
#include <ctime>
#include <cassert>
#include <map>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <stack>
#include <queue>
#include <numeric>
#include <iterator>
#include <bitset>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> Pii;
typedef pair<ll, ll> Pll;

#define FOR(i,n) for(int i = 0; i < (n); i++)
#define sz(c) ((int)(c).size())
#define ten(x) ((int)1e##x)

#pragma comment(linker,"/STACK:36777216")

template<class T> void chmax(T& l, const T r){ l = max(l, r); }
template<class T> void chmin(T& l, const T r){ l = min(l, r); }

template<class T>
void splitstr(const string &s, vector<T> &out)
{
	istringstream in(s);
	out.clear();
	copy(istream_iterator<T>(in), istream_iterator<T>(), back_inserter(out));
}

int solve() {
	int n; cin >> n;
	vector<vector<string>> vs;
	string s; getline(cin,s);
	FOR(i, n){
		getline(cin,s);
		vector<string> tmp;
		splitstr(s, tmp);
		vs.push_back(tmp);
	}

	vector<vector<int>> is;
	map<string, int> mp;
	FOR(i, n){
		is.emplace_back();
		for (auto& s : vs[i]) {
			if (mp.count(s) == 0) {
				int size = sz(mp);
				mp[s] = size;
			}
			is.back().push_back(mp[s]);
		}
	}

	int ans = sz(mp);
	FOR(i, 1 << n){
		if (i % 4 != 2) continue;
		static bool left[3000];
		static bool right[3000];
		memset(left, 0, sz(mp));
		memset(right, 0, sz(mp));
		FOR(j, n) {
			bool* ch = (i & (1 << j)) ? left : right;
			for (auto id : is[j]) {
				ch[id] = true;
			}
		}
		int cnt = 0;
		FOR(i, 3000){
			if (left[i] && right[i]) cnt++;
		}
		ans = min(ans, cnt);
	}
	return ans;

}
int main(){
	int t; cin >> t;
	FOR(i, t){
		printf("Case #%d: ", i + 1);
		int ans = solve();
		printf("%d\n", ans);
	}

	return 0;
}
