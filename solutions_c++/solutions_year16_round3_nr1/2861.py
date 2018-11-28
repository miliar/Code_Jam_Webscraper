#ifndef PRAGMA_COMMENT_LINKER
#pragma comment(linker, "/STACK:199999999")
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
const   long double             EPS = 1e-20;
const   long double             PI = 3.14159265358979323846;

inline int lg2(ll n) { int h = 0; while ((1ll << h) < n) ++h; return h; }

struct config_io { config_io() { cin.tie(nullptr); ios_base::sync_with_stdio(false); } } cnf_io;
struct config_rand { config_rand() { srand(chrono::duration_cast<chrono::nanoseconds>(chrono::high_resolution_clock::now().time_since_epoch()).count()); } } cnf_rand;

namespace std
{
	template<>
	struct hash < pair<int, int> > {
		size_t operator()(const pair<int, int> &x) const {
			return (x.first * 31 + x.second) % ((int)1e9 + 7);
		}
	};
}

inline void scan(int &x) { scanf("%d", &x); }
inline void scan(int &x, int &y) { scanf("%d%d", &x, &y); }
inline void scan(int &x, int &y, int &z) { scanf("%d%d%d", &x, &y, &z); }
inline void print(int x) { printf("%d\n", x); }
inline void print(int x, int y) { printf("%d %d\n", x, y); }
inline void print(int x, int y, int z) { printf("%d %d %d\n", x, y, z); }

//void build(int s) {
//	for (int i = nn; i < 2*nn; ++i) {
//		t[s][i] = a[s][i - nn + 1];
//	}
//	for (int i = nn - 1; i > 0; --i) {
//		t[s][i] = min(t[s][i << 1], t[s][i << 1 | 1]);
//	}
//}
//
//double rmq(int s, int l, int r) {
//	double ans = 1e100;
//	for (l += nn-1, r += nn-1; l <= r; ) {
//		if (l & 1) ans = min(ans, t[s][l]);
//		if (!(r & 1)) ans = min(ans, t[s][r]);
//		l = (l + 1) / 2;
//		r = (r - 1) / 2;
//	}
//	return ans;
//}

void solve(int test) {
	int n;
	scan(n);
	priority_queue<pair<int, int>> p;
	int sum = 0;
	for (int i = 1; i <= n; ++i) {
		int pi;
		scan(pi);
		p.push(mp(pi, i));
		sum += pi;
	}
	printf("Case #%d: ", test);
	while (!p.empty()) {
		pair<int, int> p1 = p.top();
		p.pop();
		pair<int, int> p2 = p.top();
		p.pop();
		if (p2.first > (sum - 1) / 2) {
			printf("%c%c ", ('A' + p1.second - 1), ('A' + p2.second - 1));
			sum -= 2;
			auto np2 = mp(p2.first - 1, p2.second);
			auto np1 = mp(p1.first - 1, p1.second);
			if (np1.first > 0) {
				p.push(np1);
			}
			if (np2.first > 0) {
				p.push(np2);
			}
		}
		else {
			printf("%c ", ('A' + p1.second - 1));
			sum -= 1;
			auto np1 = mp(p1.first - 1, p1.second);
			auto np2 = mp(p2.first, p2.second);
			if (np1.first > 0) {
				p.push(np1);
			}
			if (np2.first > 0) {
				p.push(np2);
			}
		}
	}
	printf("\n");
}

int main() {
#ifdef HOME
#define TASK "home"
	freopen(TASK".in", "r", stdin); freopen(TASK".out", "w", stdout);
#endif

	int tt;
	scan(tt);
	for (int i = 1; i <= tt; ++i) {
		solve(i);
	}

#ifdef HOME	
	cout << "\n\nTime: " << clock() / (double)CLOCKS_PER_SEC << endl;
#endif
	return 0;
}