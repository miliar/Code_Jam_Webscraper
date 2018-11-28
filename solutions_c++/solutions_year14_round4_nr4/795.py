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

struct BIT{
	int n;
	int dat[1030];

	BIT(){
		n = 1024;
		rep(i, 1030) dat[i] = 0;
	}

	void add(int x){
		for (int i = x; i <= n; i += i&-i) dat[i] += 1;
	}

	int sum(int x){
		int s = 0;
		for (int i = x; i > 0; i -= i&-i) s += dat[i];
		return s;
	}
};


int swap_cnt(vector<int> &v, int l, int r, bool asc){
	if (r <= l) return 0;

	BIT bit;
	
	int sum = 0;
	for (int i = l; i < r; ++i){
		if(asc) sum += bit.sum(bit.n) - bit.sum(v[i]);
		else sum += bit.sum(v[i]);
		bit.add(v[i]);
	}

	return sum;
}

int a[10];
int n, m, ans, anscnt;
vector<string> v;

int check(){
	set<string> s[4];

	rep(i, m){
		s[a[i]].insert("");
		rep(j, v[i].size()){
			s[a[i]].insert(v[i].substr(0, j+1));
		}
	}

	int res = 0;
	rep(i, n) res += s[i].size();
	return res;
}

void dfs(int num){
	if (num == m){
		int ret = check();
		if (ret == ans) ++anscnt;
		if (ret > ans){
			ans = ret;
			anscnt = 1;
		}
		return;
	}

	rep(i, n){
		a[num] = i;
		dfs(num + 1);
	}
}

int main(){
	int T;
	cin >> T;
	FOR(t, 1, T + 1){
		printf("Case #%d: ", t);

		ans = 0, anscnt = 0;
		cin >> m >> n;
		v.clear();
		v.resize(m);
		rep(i, m) cin >> v[i];

		dfs(0);

		cout << ans << ' ' << anscnt << '\n';
	}


	return 0;
}