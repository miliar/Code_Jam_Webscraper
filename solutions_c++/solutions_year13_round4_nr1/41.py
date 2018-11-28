#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <sstream>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)

typedef long long int64;
typedef pair <int64, int64> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const int64 inf64 = ((int64)1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;
const string task = "";

template <class T> T sqr (T x) {return x * x;}

vector<pii> now;
int cur;
int64 res = 0;
int64 n, m;
vector<pii> e;

const int64 mod = 1000002013;

int64 cost(int64 n) {
	return ((n * n + n - 2) / 2) % mod;
}

int64 cost(int64 n, int64 m) {
	return (cost(n) - cost(n - m) + mod) % mod;
}

void upd(int t) {
	forn(i, now.size()) {
		res = (res + now[i].fs * cost(now[i].sc, t - cur)) % mod;
		now[i].sc -= (t - cur);
	}
	cur = t;
}

void add(int64 a) {
	now.pb(mp(a, n));
}

void rem(int64 a) {
	while (a > 0) {
		int64 n = min(a, now[now.size() - 1].fs);
		a -= n;
		now[now.size() - 1].fs -= n;
		if (now[now.size() - 1].fs == 0) now.pop_back();
	}
}

void solve(){
	res = 0;
	cin >> n >> m;
	int64 ALL = 0;
	e.clear();
	forn(i, m) {
		int x, y, w;
		cin >> x >> y >> w;
		x --; y --;
		e.pb(mp(x, -w));
		e.pb(mp(y, w));
		ALL = (ALL + w * cost(n, y - x)) % mod;
	}
	sort(all(e));
	cur = 0;
	now.clear();
	forn(i, e.size()) {
		upd(e[i].fs);
		if (e[i].sc < 0)
			add(-e[i].sc);
		else
			rem(e[i].sc);
	}
	cout << (ALL - res + mod) % mod << endl;
}

int main ()
{
//	freopen("input.txt", "r", stdin);
//   freopen("res", "w", stdout);

	int n;
	cin >> n;

	forn(i, n){
		printf("Case #%d: ", i + 1);
		solve();
	//	puts("");
	}

	
	return 0;
}
