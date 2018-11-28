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
#include <iterator>
#include <bitset>
#include <random>
#include <assert.h>
#include <unordered_map>
#include <array>

#ifdef _MSC_VER
#include <agents.h>
#endif

#define FOR(i, a, b) for(int i = (a); i < (int)(b); ++i)
#define rep(i, n) FOR(i, 0, n)
#define ALL(v) v.begin(), v.end()
#define REV(v) v.rbegin(), v.rend()
#define MEMSET(v, s) memset(v, s, sizeof(v))
#define X first
#define Y second
#define MP make_pair
#define umap unordered_map

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int, int> P;
typedef unsigned int uint;

int main(){
	int T;
	cin >> T;
	FOR(t, 1, T + 1){
		printf("Case #%d: ", t);

		int n, X;
		cin >> n >> X;
		set<P> s;
		rep(i, n){
			int x;
			cin >> x;
			s.insert(MP(-x, i));
		}

		int ans = 0;
		while (!s.empty()){
			++ans;
			auto it = s.begin();
			int x = it->first;
			s.erase(it);
			auto it2 = s.lower_bound(MP(- X - x, 0));
			if (it2 != s.end()) s.erase(it2);
		}
		cout << ans << '\n';
	}


	return 0;
}