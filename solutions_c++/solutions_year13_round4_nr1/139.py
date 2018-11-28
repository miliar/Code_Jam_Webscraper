#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <cstring>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <cassert>
#include <ctime>


using namespace std;

#ifdef WIN32
    #define LLD "%I64d"
#else
    #define LLD "%lld"
#endif

typedef pair<int, int> pii;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<ll> vll;
typedef vector<vll> vvll;

ll rdtsc() {
    ll tmp;
    asm("rdtsc" : "=A"(tmp));
    return tmp;
}

#define TASKNAME "text"
#define pb push_back
#define mp make_pair
#define EPS (1e-9)
#define INF ((int)1e9)
#define sqr(x) ((x) * (x))         
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define sz(x) ((int)(x).size())

const int MOD = 1000002013;
inline void add(int &x, int y) {
	if ((x += y) >= MOD)
		x -= MOD;
}
 
inline int sign(int x) {
	return (x < 0) ? -1 : (x > 0);
}

struct station {
	int pos, cnt;

	station() {}
	station(int _pos, int _cnt) : pos(_pos), cnt(_cnt) {}


	inline bool operator < (const station &s) const {
		return pos != s.pos ? pos < s.pos : sign(cnt) != sign(s.cnt) ? (sign(cnt) == 1) : 0;
	}
};

const int maxn = 2000;
station sts[maxn], qu[maxn];

inline int payment(int l, int r, int cnt, int N) {
	ll res = ((ll)N * (r - l) - (ll)(r - l - 1) * (r - l) / 2) % MOD;
	res *= cnt;
	res %= MOD;
	if (res < 0)
		res += MOD;
	return res;
}

void solve(int testCase) {
	printf("Case #%d: ", testCase);
	int n, m;
	scanf("%d%d", &n, &m);
	assert(m * 2 <= maxn);
	int cnt = 0;
	int res = 0;
	for (int i = 0; i < m; i++) {
		int s, t, p;
		scanf("%d%d%d", &s, &t, &p);
		assert(1 <= s && s <= t && t <= n);
		sts[cnt++] = station(s, p);
		sts[cnt++] = station(t, -p);
		add(res, payment(s, t, p, n));
	}

	sort(sts, sts + cnt);
	int r = 0;
	for (int i = 0; i < cnt; i++) {
		if (sign(sts[i].cnt) == 1) {
			qu[r++] = sts[i];
			continue;
		}
		sts[i].cnt = -sts[i].cnt;
		while (r > 0 && sts[i].cnt) {
		  int curcnt = min(sts[i].cnt, qu[r - 1].cnt);
		  add(res, MOD - payment(qu[r - 1].pos, sts[i].pos, curcnt, n));
		  sts[i].cnt -= curcnt, qu[r - 1].cnt -= curcnt;
		  if (!qu[r - 1].cnt)
		  	--r;
		}
		assert(!sts[i].cnt);
	} 
	assert(!r);

	printf("%d\n", res);
}

int main() {
	srand(rdtsc());
#ifdef DEBUG
	freopen(TASKNAME".in", "r", stdin);
	freopen(TASKNAME".out", "w", stdout);
#endif
	
	int testCase = 0, n;
	while (scanf("%d", &n) >= 1) {
		for (int i = 0; i < n; i++)
			solve(++testCase);
		//break;
	}
	return 0;
}
