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
#define x first
#define y second

typedef long long int64;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const int64 inf64 = ((int64)1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;
const string task = "";

template <class T> T sqr (T x) {return x * x;}

typedef long double ldb;
typedef pair<ldb, ldb> pii;

pii operator + (pii a, pii b) {
	return pii(a.fs + b.fs, a.sc + b.sc);
}

pii operator - (pii a, pii b) {
	return pii(a.fs - b.fs, a.sc - b.sc);
}

pii operator * (pii a, ldb b) {
	return pii(a.fs * b, a.sc * b);
}

pii operator / (pii a, ldb b) {
	return pii(a.fs / b, a.sc / b);
}

ldb dist(pii a, pii b) {
	return sqrtl(sqr(a.fs - b.fs) + sqr(a.sc - b.sc));
}

struct line {
	ldb a, b, c;

	line () {}

	line (pii v, pii u) {
		a = v.y - u.y;
		b = u.x - v.x;
		c = - v.x * a - v.y * b;
	}
};

int sgn(ldb a) {
	if (a < -eps) return -1;
	if (a > eps) return 1;
	return 0;
}

ldb side(line l, pii v) {
	return l.a * v.x + l.b * v.y + l.c;
}

bool ls (pii a, pii b) {
	if (fabs(a.fs - b.fs) > eps)
		return a.fs < b.fs;
	if (fabs(a.sc - b.sc) > eps)
		return a.sc < b.sc;
	return 0;
}

ldb det(ldb a, ldb b, ldb c, ldb d) {
	return a * d - b * c;
}

bool cross(line l1, line l2, pii &w) {
	double o = det(l1.a, l1.b, l2.a, l2.b);
	double o1 = det(-l1.c, l1.b, -l2.c, l2.b);
	double o2 = det(l1.a, -l1.c, l2.a, -l2.c);
	if (fabs(o) < eps) return 0;
	w = mp(o1 / o, o2 / o);
	return 1;
}

bool cross(pii a, pii b, pii c, pii d) {
	if (ls(b, a)) swap(a, b);
	if (ls(d, c)) swap(c, d);
	line l1(a, b);
	line l2(c, d);
	pii w;
	if (sgn(side(l1, c)) == 0)
		if (a < c && c < b) return 1;
	if (sgn(side(l1, d)) == 0)
		if (a < d && d < b) return 1;
	if (sgn(side(l2, a)) == 0)
		if (c < a && a < d) return 1;
	if (sgn(side(l2, b)) == 0)
		if (c < b && b < d) return 1;
	if (!cross(l1, l2, w)) return 0;
	if (ls(w, c) || ls(d, w) || ls(w, a) || ls(b, w)) return 0;
	if (ls(a, w) && ls(w, b)) return 1;
	return 0;
}

const int nmax = 1010;

int n;
pii p[nmax];
double g[nmax][nmax];
//double dp[1 << nmax][nmax];
vector<int> res;
double bst;
int us[nmax];

void go(vector<int> a, double cur) {
	if (a.size() == n) {
			bool done = 1;
			for (int k = 0; k + 1 < a.size(); k ++) 
				if (cross(p[a[k]], p[a[k+1]], p[a.back()], p[a[0]])) {
					done = 0;
					break;
				}
			if (!done) return;

		cur += g[a.back()][0];
		if (cur > bst) {
			bst = cur;
			res = a;
		}
		return;
	}
	forn(j, n)
		if (!us[j]) {
			bool done = 1;
			for (int k = 0; k + 1 < a.size(); k ++) 
				if (cross(p[a[k]], p[a[k+1]], p[a.back()], p[j])) {
					done = 0;
					break;
				}
			if (!done) continue;
			us[j] = 1;
			vector<int> now = a;
			now.pb(j);
			go(now, cur + g[a.back()][j]);
			us[j] = 0;			
		}
}
           
void solve(){
	cin >> n;
	forn(i, n)
		cin >> p[i].x >> p[i].y;
	forn(i, n)
		forn(j, n)
			g[i][j] = (p[j].x - p[i].x) * (p[j].y + p[i].y) / 2;
	bst = 0;
	vector<int> now;
	us[0] = 1;
	now.pb(0);
	go(now, 0);
	cerr << bst << endl;
	forn(i, res.size())
		cout << " " << res[i];
	cout << endl;
}

int main ()
{
//	freopen("input.txt", "r", stdin);
//   freopen("res", "w", stdout);

	int n;
	cin >> n;

	forn(i, n){
		printf("Case #%d:", i + 1);
		solve();
//		puts("");
	}

	
	return 0;
}
