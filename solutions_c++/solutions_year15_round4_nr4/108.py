#include "assert.h"
#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <time.h>
#include <vector>

#if LOCAL
	#define DO_NOT_SEND
#endif

typedef long long LL;

int IntMaxVal = (int) 1e20;
int IntMinVal = (int) -1e20;
LL LongMaxVal = (LL) 1e20;
LL LongMinVal = (LL) -1e20;

#define FOR(i, a, b) for(int i = a; i < b ; ++i)
#define FORD(i, a, b) for(int i = a; i >= b; --i)

template<typename T> inline void minimize(T &a, T b) { a = std::min(a, b); }
template<typename T> inline void maximize(T &a, T b) { a = std::max(a, b); }

#define all(v) v.begin(),v.end()

using namespace std;

#define endl '\n'
template<typename T> struct argument_type;
template<typename T, typename U> struct argument_type<T(U)> { typedef U type; };
#define next(t, i) argument_type<void(t)>::type i; cin >> i;

template <typename T1, typename T2> istream& operator >>(istream& is, pair<T1, T2>& s) { is >> s.first >> s.second; return is; }
template <typename T> ostream& operator << (ostream& os, const vector<T> &v) { for (int i = 0 ; i < v.size() ; i++) os << v[i] << ' '; os << endl; return os; }
template <typename T1, typename T2> ostream& operator <<(ostream& s, const pair<T1, T2>& t) { s << t.first << ' ' << t.second; return s; }
template <typename T> vector<T> readVector(int n) { vector<T> res(n); for (int i = 0 ; i < n ; i++) cin >> res[i]; return res; }

const int mod = 1000 * 1000 * 1000 + 7;

struct mod_num {
	int x;
	
	mod_num() : x(0) { }
	mod_num(int x) : x(x) { }
	
	mod_num operator +(const mod_num &b) { int res = x + b.x; if (res >= mod) res -= mod; return res; }
	mod_num operator +=(const mod_num &b) { x += b.x; if (x >= mod) x -= mod; return *this; }
	
	mod_num operator -=(const mod_num &b) { if (b.x > 0) *this += mod - b.x; return *this; }
	
	mod_num operator *(const mod_num &b) { return (int) (x * (LL) b.x % mod); }
	mod_num operator *=(const mod_num &b) { x = x * (LL) b.x % mod; return *this; }
		
	mod_num pow(int n) {
		if (n == 0) return 1;
		auto res = pow(n / 2);
		res *= res;
		if (n & 1) res *= *this;
		return res;
	}
};

mod_num operator +(int a, const mod_num &b) { return mod_num(a) + b; }
mod_num operator *(int a, const mod_num &b) { return mod_num(a) * b; }
istream& operator >> (istream& is, mod_num &x) { return is >> x.x; }
ostream& operator << (ostream& os, const mod_num &x) { return os << x.x; }

vector<int> period = { 1 , 1 , 3 , 6 , 4 , 1 };

vector<vector<int>> can_follow = {
	{ 1 , 2 , 3 , 4 , 5 },
	{ 2 , 3 , 4 , 5 },
	{ 1 },
	{ 1 },
	{ 1 },
	{ 1 },
};

vector<int> heights = { 0, 2 , 2 , 2 , 3 , 1 };

mod_num cur_ans = 0;
vector<int> cur_stack;
int cur_h = 0;

int gcd(int a, int b) {
	if (b == 0) return a;
	return gcd(b, a % b);
}

void build(int h, int cols) {
	if (cur_h == h) {
		int cur_period = 1;
		mod_num options = 1;
		for (auto x : cur_stack) {
			if (cur_period > 1) options *= gcd(period[x], cur_period);
			cur_period = cur_period * period[x] / gcd(cur_period, period[x]);			
		}
		
		if (cols % cur_period == 0) cur_ans += options;
		// for (auto x : cur_stack) cout << x << ' '; cout << options << endl;
		return;
	} else {
		for (auto follower : can_follow[cur_stack.back()]) if (heights[follower] + cur_h <= h) if (cols % period[follower] == 0) {
			cur_h += heights[follower];
			cur_stack.push_back(follower);
			build(h, cols);
			cur_stack.pop_back();
			cur_h -= heights[follower];
		}
	}
}

mod_num solve() {
	next(int, r);
	next(int, c);
	
	cur_ans = 0;
	cur_h = 0;
	cur_stack = { 0 };
	build(r, c);
	
	return cur_ans;
}

int main() {
	srand (time(NULL));
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	
	next(int, t);
	FOR (i, 0, t) {
		cout << "Case #" << i + 1 << ": " << solve() << endl;
	}
}