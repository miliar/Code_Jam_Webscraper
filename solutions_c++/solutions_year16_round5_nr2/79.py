#line 1 "B.cpp"
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
	for (const auto &t : v) {
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


template <class T>
T fastpow(const T &a, ll n) {
	T r = 1, e = a;
	for (int i = 0; (1ll<<i) <= n; i++, e *= e) {
		if (n&(1ll<<i))
			r *= e;
	}
	return r;
}



///////////////////////////////// END util.h /////////////////////////////////


#line 30 "B.cpp"

int testcasenr;

mt19937 gen(43242394);
int N, M;
int par[200];
char name[200];
char word[10][200];
int rootdp[200];
vector<bool> had;

int root(int i) {
	if (rootdp[i] == -1) {
		if (par[i] == -1 || had[par[i]])
			rootdp[i] = i;
		else
			rootdp[i] = root(par[i]);
	}
	return rootdp[i];
}

string blub() {
	string res;
	had.assign(N, false);
	REP(t,0,N) {
		REP(i,0,N)
			rootdp[i] = -1;
		vector<int> v;
		REP(i,0,N)
			if (!had[i])
				v.push_back(root(i));
// 		cerr << "v = " << v << endl;
		shuffle(v.begin(), v.end(), gen);
		res += name[v[0]];
		had[v[0]] = true;
	}
	return res;
}

void docase() {
	scanf("%d ", &N);
	REP(i,0,N) {
		scanf("%d ", &par[i]);
		par[i]--;
	}
	scanf("%s ", name);
	scanf("%d ", &M);
	vector<int> freq(M, 0);
	REP(i,0,M) {
		scanf("%s ", word[i]);
	}
	const int RU = 3000;
	REP(ru,0,RU) {
		string hat = blub();
// 		cerr << hat << endl;
		REP(m,0,M) {
			int lw = strlen(word[m]);
			bool found = false;
			REP(i,0,N-lw+1) {
				bool ok = true;
				REP(j,0,lw)
					if (hat[i+j] != word[m][j]) {
						ok = false;
						break;
					}
				if (ok)
					found = true;
			}
			if (found)
				freq[m]++;
		}
	}
	REP(m,0,M)
		printf(" %.6lf", (double)freq[m]/RU);
	printf("\n");
}

int main() {
	int T;
	scanf("%d ", &T);
	for (testcasenr = 1; testcasenr <= T; testcasenr++) {
		fprintf(stderr, "Test %d/%d\n", testcasenr, T);
		printf("Case #%d: ", testcasenr);
		docase();
		fflush(stdout);
		fflush(stderr);
	}
	return 0;
}
