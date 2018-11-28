#pragma comment(linker, "/STACK:134217728") //128mb
#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <cassert>
#include <climits>
#include <ctime>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <cmath>
#include <set>
#include <map>
#include <hash_set>
#include <hash_map>
#include <algorithm>
#include <random>
#include <map>
#include <set>
#include <stack>
#include <bitset>
#include <complex>
using namespace std;


#define input_txt freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout)
#define in_out(x) freopen(x".in", "r", stdin);freopen(x".out", "w", stdout)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz(s) int((s).size())
#define all(x) x.begin(),x.end()

typedef long long ll;
typedef long long llong;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef complex<double> comp;

const long long MOD = 1000000000 + 7; //1e9+7
const long long MAXN = 100000 + 100; //1e5
const long long MAGIC = 123123123;
const double PI = 4 * atan(1.);
const double EPS = 1E-7;



struct cmp_for_set {
	bool operator()(const int & a, const int & b){ return a > b; }
};

void time_elapsed() { cout << "\nTIME ELAPSED: " << (double)clock() / CLOCKS_PER_SEC << " sec\n"; }
#define DOUT_VAR(x) cout << #x << " = " << (x) << endl
template<typename T> void DOUT_VEC(vector<T> & vec) { puts("");  for (auto i : vec) cout << i << " "; puts(""); }
template<typename T> void DOUT_TABLE(vector<vector<T>> & vec) { puts(""); for (auto i : vec) { for (auto j : i) cout << j << " "; cout << endl; }puts(""); }

template<typename T> T gcd(T a, T b){ return ((!b) ? a : gcd(b, a%b)); }
template<typename T>T gcd(T a, T b, T&x, T&y){ if (!a){ x = 0, y = 1; return b; }T x1, y1; T d = gcd(b%a, a, x1, y1); x = y1 - (b / a)*x1; y = x1; return d; }

template<typename T> T lcm(T a, T b) { return (a / gcd(a, b))*b; }
template<typename T, typename M> T neg_mod(T a, M mod) { return ((a%mod) + mod) % mod; }
ll binpow(ll x, ll p) { ll res = 1; while (p){ if (p & 1) res *= x; x *= x; p >>= 1; }return res; }
ll binpow_mod(ll x, ll p, ll m) { ll res = 1; while (p){ if (p & 1) res = (res*x) % m; x = (x*x) % m; p >>= 1; }return res; }

int TESTS_CNT;

ll nodes_cnt;
ll ways_need;

int g[55][55];
ll dp[55];


void read_test() {
	cin >> nodes_cnt >> ways_need;
	for (int i = 0; i < nodes_cnt; ++i) {
		for (int j = 0; j < nodes_cnt; ++j) {
			g[i][j] = 0;
		}
	}
}

ll go(int v) {
	if (dp[v] != -1)return dp[v];
	ll res = 0;
	for (int i = 0; i < nodes_cnt; ++i) {
		if (g[i][v]) {
			res += go(i);
		}
	}
	return dp[v]=res;
}

int used[55];

bool chk(int v) {
	used[v] = 1;
	for (int i = 0; i < nodes_cnt; ++i) {
		if (g[v][i]) {
			if (used[i]==1) {
				return false;
			}
			else if (!chk(i))return false;
		}
	}
	used[v] = 2;
	return true;
}

bool cycles() {
	for (int i = 0; i < 55; ++i) {
		used[i] = 0;
	}

	for (int i = 0; i < 55; ++i) {
		if (!used[i] && !chk(i)) return true;
	}
	return false;
}

bool check() {
	for (int i = 0; i < nodes_cnt; ++i) {
		dp[i] = -1;
	}
	dp[0] = 1;

	if (cycles())return false;

	return go(nodes_cnt - 1) == (ways_need);
}

bool solve_test() {
	vector<pii> ed;
	for (int i = 0; i < nodes_cnt; ++i) {
		for (int j = i+1; j < nodes_cnt; ++j) {
			if (i == j)continue;
			ed.push_back(mp(i, j));
		}
	}
	int tot_ed = ed.size();
	for (int m = 0; m < (1 << tot_ed); ++m) {
		for (int s = m; s; s = ((s - 1)&m)) {
			for (int i = 0; i < tot_ed; ++i) {
				if (m & (1 << i)) {
					if (s & (1 << i)) {
						g[ed[i].first][ed[i].second] = 1;
						g[ed[i].second][ed[i].first] = 0;
					}
					else {
						g[ed[i].second][ed[i].first] = 1;
						g[ed[i].first][ed[i].second] = 0;
					}
				}
				else {
					g[ed[i].first][ed[i].second] = g[ed[i].second][ed[i].first] = 0;
				}
			}

			//graph filled
			bool bad = false;
			for (int i = 0; i < nodes_cnt; ++i) {
				if (g[nodes_cnt - 1][i]) {
					bad = true;
					break;
				}
			}
			if (bad)continue;
			bad |= (!check());
			if (!bad) {
				return true;
			}

		}
	}
	return false;
}

bool solve_fast() {
	if (ways_need > (1LL << (nodes_cnt - 2))) {
		//assert(!solve_test());
		return false;
	}
	for (int i = 0; i < nodes_cnt; ++i) {
		for (int j = 0; j < nodes_cnt; ++j) {
			g[i][j] = 0; 
		}
	}
	for (int i = 1; i < nodes_cnt; ++i) {
		for (int j = i + 1; j < nodes_cnt; ++j) {
			g[i][j] = 1;
		}
	}
	g[0][nodes_cnt - 1] = 1;
	ways_need--;
	for (int i = 0; i < nodes_cnt - 1; ++i) {
		if (ways_need & (1LL << i)) {
			g[0][nodes_cnt - 2 - i] = 1;
		}
	}
	ways_need++;

	//assert(check());
	return true;
}

int main() {
	input_txt;

	cin >> TESTS_CNT;

	for (int TEST_ID = 1; TEST_ID <= TESTS_CNT; ++TEST_ID) {
		read_test();
		printf("Case #%d: ", TEST_ID);
		if (solve_fast()) {
			puts("POSSIBLE");
			for (int i = 0; i < nodes_cnt; ++i) {
				for (int j = 0; j < nodes_cnt; ++j) {
					printf("%d", g[i][j]);
				}
				puts("");
			}
		}
		else {
			puts("IMPOSSIBLE");
		}

		//puts("");
	}


	//time_elapsed();
	return 0;
}