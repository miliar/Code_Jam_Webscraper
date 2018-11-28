#define TASK "fire"
#define _CRT_SECURE_NO_WARNINGS

#pragma comment(linker, "/STACK:66777216")
#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <ctime>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <deque>
#include <cassert>
#include <cstdlib>
#include <bitset>
#include <algorithm>
#include <string>
#include <list>
#include <fstream>
#include <cstring>
#include <climits>
#include <stack>
#include <random>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef pair<string, int> psi;
typedef vector<string> vs;
typedef pair<ll, ll> pll;
typedef vector<ll> vll;
typedef vector<char> vc;
typedef vector<pii> vpii;
typedef vector<pair<ll, ll> > vpll;
typedef long double ld;

#define forn(i, n) for (int i = 0; i < (int)n; i++)
#define for1(i, n) for (int i = 1; i <= (int)n; i++)
#define forq(i, s, t) for (int i = s; i <= t; i++)
#define ford(i, s, t) for (int i = s; i >= t; i--)
#define mk make_pair
#define inb push_back
#define outb pop_back
#define ump unordered_map
#define all(v) v.begin(), v.end()
#define X first
#define Y second
#define TIME clock() * 1.0 / CLOCKS_PER_SEC
#define randint(x,y)
#define randlong(x, y)
#define double long double
#define sqr(x) (x) * (x)
#define y1 amdknkgsdaasdwapgnpikn
//
#define mp make_pair
#define pb push_back
#define XX first
#define YY second
//

const ld EPS = 1e-9;
const ld pi = acos(-1.0);

const int MAXN = (int)1e5 + 7;
const ll INF = (ll)2147483647;
const ll LINF = (ll)8e18;
const int MOD = (ll)1e9 + 7;
const int CHASH = (ll)239017;
const ld DINF = (ld)1000000000000000.0;

void gen();
int solve();

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
#ifdef _DEBUG
	gen();
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	freopen("test.txt", "w", stderr);
	ld tstart = TIME;
#else
	//freopen(TASK".in", "r", stdin), freopen(TASK".out", "w", stdout);
	//freopen("input.txt", "r", stdin), freopen("output.txt", "w", stdout), freopen("test.txt", "w", stderr);
	srand(228);
#endif
	solve();
#ifdef _DEBUG
	ld tend = TIME;
	cerr << tend - tstart << " s.\n";
#endif
	return 0;
}

void gen()
{
	freopen("input.txt", "a+", stdout);
	srand(time(0));
	return;
}

bool equal(double a, double b) { return abs(a - b) < EPS; }

struct Point
{// vector
	double x, y;
	Point() {};
	Point(double x, double y) : x(x), y(y) {};
	//point mul by double 
	Point operator*(double d) { return Point(x * d, y * d); }
	//point + vector
	Point operator+(Point p) { return Point(x + p.x, y + p.y); }
	Point operator-(Point p) { return Point(x - p.x, y - p.y); }
	//dotProduct
	double operator%(Point p) { return x * p.x + y * p.y; }
	// crossProduct
	double operator*(Point p) { return x * p.y - y * p.x; }
	// rasstoyanie
	double distancetoPoint(Point p)
	{
		return sqrt((x - p.x) * (x - p.x) + (y - p.y) * (y - p.y));
	}
	// vector length \ distance from zero to Point
	double len() { return sqrt(x * x + y * y); }
	double angle(Point p) { return atan2((*this) * p, (*this) % p); }
	// turnByAngle
	Point turnByAngle(double a) {
		double cosa = cos(a); double sina = sin(a);
		return Point(x * cosa - y * sina, x * sina + y * cosa);
	}
};

Point makeV(Point a, Point b) { return a - b; }
const Point NULLP = Point(-239239, 1488228);
const Point SOVP = Point(13888, 888283);

struct Line {
	double a, b, c;

	Line(Point p, Point t) {
		a = t.y - p.y; // -n.y
		b = p.x - t.x; // n.x
		c = -a * p.x - b * p.y;
	}

	// oriented!!!
	double distanceFromPoint(Point p) {
		return (a * p.x + b * p.y + c) / Point(a, b).len();
	}

	bool operator||(Line l) {
		return equal(Point(a, b) * Point(l.a, l.b), 0);
	}

	Point operator^(Line l) {
		if (equal(l.a, a) && equal(l.b, b) && equal(l.c, c))
			return SOVP;
		double d = Point(a, b) * Point(l.a, l.b);
		if (equal(d, 0)) return NULLP;
		double x = (b * l.c - l.b * c) / d;
		double y = (c * l.a - l.c * a) / d;
		return Point(x, y);
	}
};

int n, ans, t;
string s;
int cnt[26], dig[10];

int solve()
{
	cin >> t;
	for1(tested, t)
	{
		cin >> s;
		cout << "Case #" << tested << ": ";
		forn(i, s.size())
			++cnt[s[i] - 'A'];
		int zc = cnt[25];
		forn(i, zc)
		{
			++dig[0];
			--cnt[25];
			--cnt['O' - 'A'];
			--cnt['E' - 'A'];
			--cnt['R' - 'A'];
		}
		int wc = cnt['W' - 'A'];
		forn(i, wc)
		{
			++dig[2];
			--cnt['T' - 'A'];
			--cnt['W' - 'A'];
			--cnt['O' - 'A'];
		}
		int c6 = cnt['X' - 'A'];
		forn(i, c6)
		{
			++dig[6];
			--cnt['S' - 'A'];
			--cnt['I' - 'A'];
			--cnt['X' - 'A'];
		}
		int c4 = cnt['U' - 'A'];
		forn(i, c4)
		{
			++dig[4];
			--cnt['F' - 'A'];
			--cnt['O' - 'A'];
			--cnt['U' - 'A'];
			--cnt['R' - 'A'];
		}
		int c5 = cnt['F' - 'A'];
		forn(i, c5)
		{
			++dig[5];
			--cnt['F' - 'A'];
			--cnt['I' - 'A'];
			--cnt['V' - 'A'];
			--cnt['E' - 'A'];
		}
		int c7 = cnt['V' - 'A'];
		forn(i, c7)
		{
			++dig[7];
			--cnt['S' - 'A'];
			--cnt['E' - 'A'];
			--cnt['V' - 'A'];
			--cnt['E' - 'A'];
			--cnt['N' - 'A'];
		}
		int c8 = cnt['G' - 'A'];
		forn(i, c8)
		{
			++dig[8];
			--cnt['E' - 'A'];
			--cnt['I' - 'A'];
			--cnt['G' - 'A'];
			--cnt['H' - 'A'];
			--cnt['T' - 'A'];
		}
		int c3 = cnt['T' - 'A'];
		forn(i, c3)
		{
			++dig[3];
			--cnt['E' - 'A'];
			--cnt['E' - 'A'];
			--cnt['R' - 'A'];
			--cnt['H' - 'A'];
			--cnt['T' - 'A'];
		}
		int c1 = cnt['O' - 'A'];
		forn(i, c1)
		{
			++dig[1];
			--cnt['E' - 'A'];
			--cnt['N' - 'A'];
			--cnt['O' - 'A'];
		}
		int c9 = cnt['I' - 'A'];
		forn(i, c9)
		{
			++dig[9];
			--cnt['N' - 'A'];
			--cnt['I' - 'A'];
			--cnt['N' - 'A'];
			--cnt['E' - 'A'];
		}
		forn(i, 10)
		{
			forn(j, dig[i])
				cout << i;
		}
		cout << "\n";
		forn(i, 10)
			dig[i] = 0;
	}
	return 0;
}