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

using namespace std;

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

template<typename T> inline void swap(pair<T, T> &p) { swap(p.first , p.second ); }

#define all(v) v.begin(),v.end()

#define endl '\n'
template<typename T> struct argument_type;
template<typename T, typename U> struct argument_type<T(U)> { typedef U type; };
#define next(t, i) argument_type<void(t)>::type i; cin >> i;

template <typename T1, typename T2> istream& operator >>(istream& is, pair<T1, T2>& s) { is >> s.first >> s.second; return is; }
template <typename T> ostream& operator << (ostream& os, const vector<T> &v) { for (int i = 0 ; i < v.size() ; i++) { if (i) os << ' '; os << v[i]; } os << endl; return os; }
template <typename T1, typename T2> ostream& operator << (ostream& os, const vector<pair<T1, T2>> &v) { for (int i = 0 ; i < v.size() ; i++) { os << v[i] << endl; } return os; }
template <typename T1, typename T2> ostream& operator <<(ostream& s, const pair<T1, T2>& t) { s << t.first << ' ' << t.second; return s; }
template <typename T> vector<T> readVector(int n) { vector<T> res(n); for (int i = 0 ; i < n ; i++) cin >> res[i]; return res; }

struct tree {
	int r, p, s;
	string str;

	tree(int r, int p, int s, string str) : r(r), p(p), s(s), str(str) { }

	bool has(int r2, int p2, int s2)  {
		return r == r2 && p == p2 && s == s2;
	}
};

vector<vector<tree*>> winners(12 + 1, vector<tree*>(200, NULL));

string solve() {
	next(int, n);
	next(int, r);
	next(int, p);
	next(int, s);

	string res = "Z";

	FOR (i, 0, winners[n].size()) if (winners[n][i] != NULL && winners[n][i]->has(r, p, s)) {
		minimize(res, winners[n][i]->str);
	}

	if (res == "Z") return "IMPOSSIBLE";
	return res;
}

tree* merge_them(tree* t1, tree* t2) {
	string str = t1->str < t2->str ? t1->str + t2->str : t2->str + t1->str;
	return new tree(
		t1->r + t2->r, 
		t1->p + t2->p,
		t1->s + t2->s,
		str
		);
}

int main() {
	srand (time(NULL));
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	fixed(cout); cout << setprecision(10);

	winners[0]['r'] = new tree(1, 0, 0, "R");
	winners[0]['p'] = new tree(0, 1, 0, "P");
	winners[0]['s'] = new tree(0, 0, 1, "S");

	FOR (i, 1, 13) {
		winners[i]['r'] = merge_them(winners[i - 1]['r'], winners[i - 1]['s']);
		winners[i]['p'] = merge_them(winners[i - 1]['p'], winners[i - 1]['r']);
		winners[i]['s'] = merge_them(winners[i - 1]['s'], winners[i - 1]['p']);
	}
	

	next(int, t);
	FOR (i, 1, t + 1) {
		auto sol = solve();
		cout << "Case #" << i << ": ";
		cout << sol;
		cout << endl;
	}
}