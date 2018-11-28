#line 1 "D.cpp"
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <string>
#include <cassert>
#include <cmath>
#include <cstring>
#include <functional>
#include <random>
using namespace std;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef long long ll;
#define REP(i,a,n) for (int i = (a); i < (n); i++)

template<class T> T& setmin(T &a, const T &b) {return a = min(a, b);}
template<class T> T& setmax(T &a, const T &b) {return a = max(a, b);}
template<class T> T MODD(const T &a, const T &b) {T r = a%b; if (r < 0) r += b; return r;}




///////////////////////////////// BEGIN util.h /////////////////////////////////


#line 1 "util.h"
template <class T, class U>
ostream& operator<<(ostream &o, const pair<T,U> &p) {
	return o << "(" << p.first << ", " << p.second << ")";
}

template <class T>
ostream& print_list(ostream &o, const T &v) {
	o << "[";
	bool first = true;
	for (auto &t : v) {
		if (first)
			first = false;
		else
			o << ", ";
		o << t;
	}
	return o << "]";
}

template <class T>
ostream& print_map(ostream &o, const T &v) {
	o << "{";
	bool first = true;
	for (auto &t : v) {
		if (first)
			first = false;
		else
			o << ", ";
		o << t.first << " => " << t.second;
	}
	return o << "}";
}

template <class T>
ostream& operator<<(ostream &o, const vector<T> &v) {
	return print_list(o, v);
}

template <class T>
ostream& operator<<(ostream &o, const set<T> &v) {
	return print_list(o, v);
}

template <class T,size_t N>
ostream& operator<<(ostream &o, const array<T,N> &v) {
	return print_list(o, v);
}

template <class T,class U>
ostream& operator<<(ostream &o, const map<T,U> &v) {
	return print_map(o, v);
}

template <class T, size_t N>
struct TuplePrintHelper {
	static ostream& print(ostream& o, const T &t) {
		TuplePrintHelper<T,N-1>::print(o, t);
		o << ", ";
		return o << get<N-1>(t);
	}
};

template <class T>
struct TuplePrintHelper<T,1> {
	static ostream& print(ostream& o, const T &t) {
		return o << get<0>(t);
	}
};

template <class T>
struct TuplePrintHelper<T,0> {
	static ostream& print(ostream& o, const T &) {
		return o;
	}
};

template <class... Args>
ostream& operator<<(ostream &o, const tuple<Args...> &t) {
	o << "(";
	TuplePrintHelper<tuple<Args...>, sizeof...(Args)>::print(o, t);
	return o << ")";
}



///////////////////////////////// END util.h /////////////////////////////////


#line 30 "D.cpp"

int N;
char line[100];
bool f[100][100];
bool vis1[100];
bool vis2[100];

int sz1, sz2;
void visit2(int);
void visit1(int i) {
	if (vis1[i])
		return;
	vis1[i] = true;
	sz1++;
	REP(j,0,N)
		if (f[i][j])
			visit2(j);
}
void visit2(int i) {
	if (vis2[i])
		return;
	vis2[i] = true;
	sz2++;
	REP(j,0,N)
		if (f[j][i])
			visit1(j);
}

vector<pair<int,int> > ps;
map<vector<int>,int> dp;
int compdp(vector<int> v);
int searc(vector<int> &v, int s1, int s2, int i) {
	if (i == (int)v.size()) {
		if ((s1 == 0 && s2 == 0) || s1 != s2)
			return 1E9;
		return compdp(v)+s1*s2;
	}
	int a = v[i];
	int res = 1E9;
	for (v[i] = 0; v[i] <= a; v[i]++)
		setmin(res, searc(v, s1+(a-v[i])*ps[i].first, s2+(a-v[i])*ps[i].second, i+1));
	v[i] = a;
	return res;
}
int compdp(vector<int> v) {
	if (!dp.count(v)) {
		bool all0 = true;
		for (int t : v)
			if (t)
				all0 = false;
		int h;
		if (all0)
			h = 0;
		else
			h = searc(v, 0, 0, 0);
		dp[v] = h;
	}
// 	cerr << "compdp(" << v << ") = " << dp[v] << endl;
	return dp[v];
}

void docase() {
	scanf("%d ", &N);
	int M = 0;
	REP(i,0,N) {
		scanf("%s ", line);
		REP(j,0,N) {
			f[i][j] = line[j] == '1';
			M += f[i][j];
		}
	}
	fill_n(vis1, N, false);
	fill_n(vis2, N, false);
	map<pair<int,int>,int> ma;
	REP(i,0,N) {
		if (vis1[i])
			continue;
		sz1 = sz2 = 0;
		visit1(i);
		ma[make_pair(sz1,sz2)]++;
	}
	REP(i,0,N) {
		if (vis2[i])
			continue;
		sz1 = sz2 = 0;
		visit2(i);
		ma[make_pair(sz1,sz2)]++;
	}
	cerr << ma << endl;
	ps.clear();
	vector<int> ve;
	for (auto &p : ma) {
		ps.push_back(p.first);
		ve.push_back(p.second);
	}
	dp.clear();
	printf("%d\n", compdp(ve)-M);
}

int main() {
	int T;
	scanf("%d ", &T);
	for (int test = 0; test < T; test++) {
		fprintf(stderr, "Test %d/%d\n", test+1, T);
		printf("Case #%d: ", test+1);
		docase();
		fflush(stdout);
		fflush(stderr);
	}
	return 0;
}
