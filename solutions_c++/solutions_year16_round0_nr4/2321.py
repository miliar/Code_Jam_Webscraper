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

void solve(int t) {
	int k, c, s;
	cin >> k >> c >> s;
	cout << "Case #" << t << ": ";
	for (int i = 1; i <= k; ++i) {
		cout << i << " ";
	}
	cout << endl;
}

int main() {
#define TASK "home"
	//freopen(TASK".in", "r", stdin); freopen(TASK".out", "w", stdout);

	time_t start = clock();

	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		solve(i);
	}

	time_t end = clock();
	//cout << (end - start) / (double)CLOCKS_PER_SEC << endl;

	return 0;
}