//Template
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
#include <string>
#include <vector>
#include <bitset>
#include <cstdarg>
#include <complex>
using namespace std;

typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef long double ld;
#define pair(x, y) make_pair(x, y)
#define runtime() ((double)clock() / CLOCKS_PER_SEC)

inline int read() {
	static int r, sign;
	static char c;
	r = 0, sign = 1;
	do c = getchar(); while (c != '-' && (c < '0' || c > '9'));
	if (c == '-') sign = -1, c = getchar();
	while (c >= '0' && c <= '9') r = r * 10 + (int)(c - '0'), c = getchar();
	return sign * r;
}

template <typename T>
inline void print(T *a, int n) {
	for (int i = 1; i < n; ++i) cout << a[i] << " ";
	cout << a[n] << endl;
}
#define PRINT(_l, _r, _s, _t) { cout << #_l #_s "~" #_t #_r ": "; for (int _i = _s; _i != _t; ++_i) cout << _l _i _r << " "; cout << endl; }

#define N 10
int T, Case = 0, n, m, ans, ways, choose[N + 1];
string s[N + 1];

struct node {
	int s[26];
} tree[100000];
int cnt = 0;

void init() {
	static int size = sizeof tree[0].s;
	for (int i = 1; i <= cnt; ++i)
		memset(tree[i].s, 0, size);
	cnt = 1;
}

void insert(string s) {
	int p = 1;
	for (int i = 0; i < s.length(); ++i) {
		int cur = s[i] - 'A';
		if (!tree[p].s[cur]) tree[p].s[cur] = ++cnt;
		p = tree[p].s[cur];
	}
}

void dfs(int x) {
	if (x > n) {
		int cur = 0;
		for (int k = 1; k <= m; ++k) {
			init();
			for (int i = 1; i <= n; ++i)
				if (choose[i] == k) insert(s[i]);
			if (cnt > 1) cur += cnt;
		}
		if (cur > ans) ans = cur, ways = 1;
		else if (cur == ans) ++ways;
		return ;
	}
	for (int i = 1; i <= m; ++i) {
		choose[x] = i;
		dfs(x + 1);
	}
}

int main(int argc, char *argv[]) {
#ifdef KANARI
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	
	cin >> T;
	while (T--) {
		cin >> n >> m;
		for (int i = 1; i <= n; ++i)
			cin >> s[i];
		ans = 0, ways = 0;
		dfs(1);
		cout << "Case #" << ++Case << ": " << ans << " " << ways << endl;
	}
	
	fclose(stdin);
	fclose(stdout);
	return 0;
}
