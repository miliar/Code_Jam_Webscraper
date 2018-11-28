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
typedef pair <int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const int64 inf64 = ((int64)1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;
const string task = "";

template <class T> T sqr (T x) {return x * x;}

int n;
int64 x[50];
int64 y[50];
int64 b;

long double calc() {
	long double res = 0;
	int64 mn = inf64;
	forn(i, n)
		mn = min(mn, x[i] + y[i]);
	int cnt = 0;
	forn(i, n)
		if (x[i] + y[i] == mn)
			cnt ++;
	forn(i, n) {
		if (x[i] + y[i] == mn)
			res += y[i] * 35. / cnt - 1.0 * y[i] * (cnt - 1) / cnt;
		else
			res -= y[i];
	}
	return res;
}

long double check(int64 we, int64 b) {
	forn(i, n)
		y[i] = 0;
	forn(i, n) {
		int64 now = min(b, we - x[i]);
		now = max(now, 0ll);
		y[i] = now;
		b -= now;
	}
	long double res = calc();
	ford(i, n) {
		if (x[i] + y[i] > we) continue;
		if (b == 0) break;
		y[i] ++;
		b --;
		res = max(res, calc());
	}
	return res;
}

void solve(){
	n = 37;
	int m;
	cin >> b >> m;
	forn(i, n)
		x[i] = 0;
	forn(i, m)
		cin >> x[i];
	sort(x, x + n);
	long double res = 0;
	vector<int64> dw;
	for (int i = 1; i <= n; i ++)
		for (int j = 0; i + j <= n; j ++) {
			int64 up = b - j;
			forn(e, i + j)
				up += x[e];
			int64 we = up / (i + j);
			dw.pb(we);
		}
	dw.pb(0);
	dw.pb(b);
//	forn(i, 1001)
//		dw.pb(i);
	forn(k, n)
		dw.pb(x[k]);
	int qe = dw.size();
	forn(i, qe)
		for (int j = -5; j <= 5; j ++)
			dw.pb(dw[i] + j);
	sort(all(dw));
	dw.erase(unique(all(dw)), dw.end());						
	
	forn(k, dw.size())
		res = max(res, check(dw[k], b));
	printf("%0.9lf\n", (double)res);
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
	}

	
	return 0;
}
