//
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <climits>
#include <cmath>
#include <utility>
#include <set>
#include <map>
#include <queue>
#include <ios>
#include <iomanip>
#include <ctime>
#include <numeric>
#include <functional>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <bitset>
#include <cstdarg>
using namespace std;

inline int read() {
	static int r;
	static char c;
	r = 0, c = getchar();
	while (c < '0' || c > '9') c = getchar();
	while (c >= '0' && c <= '9') r = r * 10 + (c - '0'), c = getchar();
	return r;
}

typedef long long ll;
#define pair(x, y) make_pair(x, y)

int T;
ll l, r;
int tc = 0;

inline bool check(ll x) {
	int num[20], tot = 0;
	while (x > 0LL) {
		num[++tot] = x % 10LL;
		x /= 10LL;
	}
	for (int i = 1; i <= tot; ++i)
		if (num[i] != num[tot - i + 1]) return false;
	return true;
}

int main() {
#ifdef KANARI
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

//	cin >> T;
//	while (T--) {
//		cin >> l >> r;
		int ans = 0;
		for (ll i = 1LL; i * i <= (ll)1e14; ++i) {
			if (i * i < l) continue;
			if (check(i) && check(i * i)) ++ans, cout << i * i << endl;
		}
		cout << "Case #" << ++tc << ": " << ans << endl;
//	}

	return 0;
}


