#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <algorithm>
#include <cmath>
#include <vector>
#include <deque>
#include <functional>
#include <iterator>
#include <utility>
#include <bitset>
#include <cstdlib>
#include <ctime>
#include <complex>
#include <cctype>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> ii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<ll> vll;

#define FOR(i, a, b) for(int i = (a); i <= (b); ++i)
#define FORD(i, a, b) for(int i = (a); i >= (b); --i)
#define REP(i, a, b) for (int i = (a); i < (b); ++i)
#define REPD(i, a, b) for (int i = (a) - 1; i >= (b); --i)
#define SZ(x) ((int)x.size())
#define openfile {freopen("inp.txt","rt",stdin);freopen("out.txt","wt",stdout);}
#define debug 0

template <typename T> inline void next_int(T &x) {
	x = 0; char c; bool neg = false;
	while (!isdigit(c = getchar())) if (c == '-') neg = true;
	do x = x*10 + c - 48; while (isdigit(c = getchar()));
	if (neg) x = -x;
}

template <typename T> inline void write_int(T x, char last = 0) {
	if (x < 0) putchar('-'), x = abs(x);
	char tmp[20]; int cnt = 0;
	while (x >= 10) tmp[cnt++] = x % 10 + 48, x /= 10;
	tmp[cnt] = x + 48;
	FORD(i, cnt, 0) putchar(tmp[i]);
	if (last) putchar(last);
}

int n, k, a[1005];
char s[1005];

int check() {
	int cnt = 0;
	FOR(i, 1, n - k + 1) if (!a[i]) {
		++cnt;
		FOR(j, i, i + k - 1) a[j] = 1 - a[j];
	}
	FOR(i, n - k + 2, n) if (!a[i]) return -1;
	return cnt;
}

int main() {
	freopen("A-large.in", "rt", stdin);
	freopen("out.txt", "wt", stdout);
	int t; scanf("%d", &t);
	FOR(kase, 1, t) {
		scanf("%s", s + 1); scanf("%d", &k);
		n = strlen(s + 1);
		FOR(i, 1, n) a[i] = (s[i] == '+');
		printf("Case #%d: ", kase);
		int tmp = 0;
		if ((tmp = check()) != -1) printf("%d\n", tmp);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}
