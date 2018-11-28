#ifdef PRAGMA_COMMENT_LINKER
#pragma comment(linker, "/STACK:1999999999")
#endif

#define  _CRT_SECURE_NO_WARNINGS
#define  NDEBUG

#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iomanip>
#include <iostream>
#include <functional>
#include <limits>
#include <list>
#include <map>
#include <memory>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

#define all(v)                  (v).begin(), (v).end()
#define db(x)                   cout << #x << '=' << (x) << "\n"
#define fend(x)                 ((x) & ((x)+1)) - 1
#define fenu(x)                 (x) | ((x)+1)
#define ft                      first
#define len(s)                  s.length()
#define maxV(type)              std::numeric_limits<type>::max()
#define minV(type)              std::numeric_limits<type>::min()
#define mp(a, b)                std::make_pair((a), (b))
#define ord(c)                  ((c) - 'a' + 1)
#define pob()                   pop_back()
#define pof()                   pop_front()
#define pub(s)                  push_back((s))
#define puf(s)                  push_front((s))
#define sc                      second

typedef double                  db;
typedef long double             ld;
typedef long long               ll;
typedef unsigned long long      ull;

const   long double             EPS = 1e-15;
const   long double             PI = 3.14159265358979323846;

inline ll lg2(ll n) { ll h = 0; while ((1ll << h) < n) ++h; return h; }

struct configio {
	configio() { cin.tie(nullptr); ios_base::sync_with_stdio(false); }
} cnfio;

template <typename _Type>
void in(_Type& first_arg) {
	cin >> first_arg;
}

template <typename _Type, typename... Args>
void in(_Type& first_arg, Args&... args) {
	cin >> first_arg;
	in(args...);
}

template <typename _Type>
void out(_Type& first_arg) {
	cout << first_arg << endl;
}

template <typename _Type, typename... Args>
void out(_Type& first_arg, Args&... args) {
	cout << first_arg << " ";
	out(args...);
}

ll diff(ll a, ll b, ll mod) {
	return ((a - b) % mod + mod) % mod;
}

int main() {
	//freopen("input.in", "r", stdin); freopen("output.out", "w", stdout);
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test) {
		int n;
		string str;
		cin >> n >> str;
		int ans = 0, cnt = 0;
		for (int i = 0; i < str.length(); ++i) {
			if (cnt < i) {
				ans += i - cnt;
				cnt = i;
			}
			cnt += str[i] - '0';
		}
		cout << "Case #" << test << ": " << ans << endl;
	}
	return 0;
}