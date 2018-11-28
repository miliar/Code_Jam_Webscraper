#ifdef PRAGMA_COMMENT_LINKER
#pragma comment(linker, "/STACK:1999999999")
#endif

#define  _CRT_SECURE_NO_WARNINGS
//#define  NDEBUG

#pragma warning(error : 4700)
#pragma warning(error : 4715)
#pragma warning(error : 4716)

#include <algorithm>
#include <cassert>
#include <cctype>
#include <chrono>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <functional>
#include <limits>
#include <list>
#include <map>
#include <memory>
#include <queue>
#include <random>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

#define all(v)                  v.begin(), v.end()
#define db(x)                   cout << #x << " = " << (x) << "\n"
#define fend(x)                 ((x) & ((x)+1)) - 1
#define fenu(x)                 (x) | ((x)+1)
#define forn(i, n)              for (int i = 0; i < (int)n; ++i)
#define ft                      first
#define len(s)                  s.length()
#define maxV(type)              std::numeric_limits<type>::max()
#define minV(type)              std::numeric_limits<type>::min()
#define mp                      std::make_pair
#define popb                    pop_back
#define popf                    pop_front
#define popcnt                  __popcnt
#define popcnt64                __popcnt64
#define pushb                   push_back
#define pushf                   push_front
#define sc                      second

#ifdef _WIN32
#define LL "%I64d"
#else
#define LL "%lld"
#endif

typedef double                  dbl;
typedef long double             ldbl;
typedef long long               ll;
typedef unsigned long long      ull;

const   long long               MILLER_RABIN = 3215031751;
//const   long double             EPS = 1e-20;
const   long double             PI = 3.14159265358979323846;

inline int lg2(ll n) { int h = 0; while ((1ll << h) < n) ++h; return h; }

struct config_io { config_io() { cin.tie(nullptr); ios_base::sync_with_stdio(false); } } cnf_io;
struct config_rand { config_rand() { srand(chrono::duration_cast<chrono::nanoseconds>(chrono::high_resolution_clock::now().time_since_epoch()).count()); } } cnf_rand;

namespace std
{
	template <>
	struct hash < pair<int, int> >
	{
		size_t operator()(const pair<int, int>& x) const
		{
			return (x.first * 31 + x.second) % ((int)1e9 + 7);
		}
	};
}

int solve1(int t, string s) {
	//string s;
	//cin >> s;
	int n = s.length();
	vector<bool> st(n);
	for (int i = 0; i < n; ++i) {
		if (s[i] == '+') st[i] = 1;
		else st[i] = 0;
	}
	int ans = 0;
	for (int i = n - 1; i >= 0; --i) {
		if (st[i]) continue;
		if (st[0]) ans++, st[0] = 0;
		reverse(st.begin(), st.begin() + i + 1);
		for (int j = i; j >= 0; --j) st[j] = !st[j];
		ans++;
		/*for (int j = 0; j < st.size(); ++j) {
		cout << st[j] << " ";
		}
		cout << endl;*/
	}
	//cout << "Case #" << t << ": " << ans << endl;
	return ans;
}

vector<int> moves(int st, int n) {
	vector<int> res;
	for (int i = n - 1; i >= 0; --i) {
		int cur = st;
		for (int j = n - 1; j >= i; --j) {
			bool bit = cur & (1 << j);
			cur -= (bit << j);
			bit ^= 1;
			cur += (bit << j);
		}
		res.push_back(cur);
	}
	return res;
}

int solve2(int t, string s) {
	//string s;
	//cin >> s;
	int n = s.length();
	int init = 0;
	for (int i = 0; i < n; ++i) {
		init <<= 1;
		if (s[i] == '+') init += 1;
	}
	vector<int> d(2000, 0);
	vector<int> used(2000, 0);
	queue<int> q;
	q.push(init);
	used[init] = 1;
	d[init] = 0;
	while (!q.empty()) {
		int state = q.front();
		q.pop();
		if (state == (1 << n) - 1) {
			return d[state];
		}
		vector<int> mov = moves(state, n);
		for (int i = 0; i < mov.size(); ++i) {
			int to = mov[i];
			if (!used[to]) {
				d[to] = d[state] + 1;
				used[to] = 1;
				q.push(to);
			}
		}
	}
	return -1;
}

int solve3(int t, string s) {
	int n = s.length();
	vector<int> dp1(n), dp2(n);
	dp1[0] = (s[0] == '+' ? 0 : 1);
	dp2[0] = (s[0] == '-' ? 0 : 1);
	for (int i = 1; i < n; ++i) {
		dp1[i] = (s[i] == '+' ? dp1[i - 1] : dp2[i - 1] + 1);
		dp2[i] = (s[i] == '-' ? dp2[i - 1] : dp1[i - 1] + 1);
	}
	return dp1[n - 1];
}

int main() {
#define TASK "home"
	//freopen(TASK".in", "r", stdin); freopen(TASK".out", "w", stdout);

	time_t start = clock();

	int t, n;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		string s;
		cin >> s;
		//int s1 = solve1(i, s);
		//int s2 = solve2(i, s);
		int s3 = solve3(i, s);
		/*if (s2 != s3) {
			db(i), db(s), db(s2), db(s3);
		}*/
		/*if (s1 != s2) {
			db(s);
			db(s1);
			db(s2);
		}*/
		cout << "Case #" << i << ": " << s3 << endl;
	}

	time_t end = clock();
	cout << fixed << setprecision(3);
	//cout << (end - start) / (double)CLOCKS_PER_SEC << endl;

	return 0;
}