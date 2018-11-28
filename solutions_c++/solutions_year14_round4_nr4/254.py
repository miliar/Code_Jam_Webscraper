#if 1
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
using namespace std;

typedef long long LL;
typedef long double LD;
typedef pair<int , int> pii;
typedef vector <int> veci;
typedef vector <veci> graph;
const LD eps = 1e-9;
const LD pi = acos(-1.0);
const int inf = 1000 * 1000 * 1000;
const LL inf64 = LL(inf) * inf;

#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define iss istringstream
#define oss ostringstream
#define dbg(x) {cerr << #x << " = " << x << endl;}
#define dbgv(x) {cerr << #x << " ={"; for (int _i = 0; _i < x.size(); _i++) {if (_i) cerr << ", "; cerr << x[_i];} cerr << "}" << endl;}
#define NAME "problem"

template<class T> string to_str(const T &a) { oss os; os << a; return os.str(); }
template<> string to_str<LD>(const LD& a) { oss os; os.precision(10); os.setf(ios::fixed); os << a; return os.str(); }
template<class T> T from_str(const string &s) { iss is; T val; is >> val; return val; }
string T(int test) { ostringstream os; os << "Case #" << test << ":"; return os.str(); }
int _test_start = -1, _test_end = -1;
bool need_to_run(int test) { return _test_start == -1 || _test_start <= test && test <= _test_end; }

struct trie_t {
	static const int maxn = 512;
	static const int maxa = 26;
	static int code(char c) { return c - 'A'; }

	int b[maxn][maxa];

	int states;

	void init() {
		states = 2;
		memset(b[1], 0, sizeof b[1]);
	}

	void add(const string &s) {
		int cur = 1;
		for(int i = 0; i < s.size(); ++i) {
			int a = code(s[i]);
			if(!b[cur][a]) {
				memset(b[states], 0, sizeof b[states]);
				b[cur][a] = states++;
			}
			cur = b[cur][a];
		}

	}
	int get_states() const
	{
		return states - 1;
	}
};

trie_t tries[4];

void solve(int test)
{
	// read
	int s, n;
	cin >> s >> n;
	vector<string> a(s);
	for (int i = 0; i < s; ++i)
		cin >> a[i];
	
	if (!need_to_run(test)) return;
	// solve
	int max_nodes = -1, cnt = 0;
	for (int i = 0; i < (1 << (2 * s)); ++i)
	{
		vector<int> st(s);
		for (int j = 0; j < s; ++j)
			st[j] = (i >> (2 * j)) & 3;
		bool bad = false;
		bool exist[4] ={0,0,0,0};
		for (int j = 0; j < s; ++j)
		{
			
			if (st[j] >= n)
				bad = true;
			exist[st[j]] = true;
		}
		for (int j = 0; j < n; ++j)
			if (!exist[j])
				bad = true;
		if (bad)
			continue;

		for (int j = 0; j < n; ++j)
			tries[j].init();
		for (int j = 0; j < s; ++j)
			tries[st[j]].add(a[j]);
		int cur_nodes = 0;
		for (int j = 0; j < n; ++j)
			cur_nodes += tries[j].get_states();
		if (cur_nodes > max_nodes)
		{
			max_nodes = cur_nodes;
			cnt = 1;
		} else if (cur_nodes == max_nodes)
			++cnt;
	}
	// write
	cout << T(test) << " " << max_nodes << " " << cnt << endl;
}

int main(int argc, char *argv[])
{
	//freopen("input.txt", "r", stdin); //freopen("output.txt", "w", stdout);
	//freopen(NAME ".in","r",stdin); freopen(NAME ".out","w",stdout);
	if (argc == 2) { _test_start = _test_end = from_str<int>(argv[1]); }
	if (argc == 3) { _test_start = from_str<int>(argv[1]); _test_end = from_str<int>(argv[2]); }

	clock_t tstart = clock();
	
	int tests;
	scanf("%d", &tests);
	for(int test = 1; test <= tests; ++test)
	{
		clock_t tprev = clock();
		solve(test);
		if (need_to_run(test))
			dbg("elapsed for #" << test << ": " << (clock() - tprev) / LD(CLOCKS_PER_SEC));
	}

	dbg("elapsed: " << (clock() - tstart) / LD(CLOCKS_PER_SEC));
	return 0;
}
/*************************
*************************/
#endif

