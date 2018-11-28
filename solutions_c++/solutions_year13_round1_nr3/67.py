#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <sstream>
using namespace std;
#pragma comment(linker, "/STACK:255000000")

typedef long long ll;

#define rep(i, a, b) for(i = (a); i < (b); ++i)
#define repb(i, a, b) for(i = (a) - 1; i >= (b); --i)
#define repd(i, a, b, d) for(i = (a); i < (b); i += (d))
#define repbd(i, a, b, d) for(i = (a) - 1; i >= (b); i -= (d))
#define reps(i, s) for(i = 0; (s)[i]; ++i)
#define repl(i, l) for(i = l.begin(); i != l.end(); ++i)

#define in(f, a) scanf("%"#f, &(a))

bool firstout = 1;

#define out(f, a) printf("%"#f, (a))
#define outf(f, a) printf((firstout) ? "%"#f : " %"#f, (a)), firstout = 0
#define nl printf("\n"), firstout = 1

#define all(x) (x).begin(),(x).end()
#define sqr(x) ((x) * (x))
#define mp make_pair

template<class T>
T &minn(T &a, T b)
{
	if(b < a) a = b;
	return a;
}

template<class T>
T &maxx(T &a, T b)
{
	if(a < b) a = b;
	return a;
}

#define inf 1012345678
#define eps 1e-9


#ifdef XDEBUG
#define mod 23
#else
#define mod 1000000007
#endif

int &madd(int &a, int b)
{
	a += b;
	if(a >= mod) a -= mod;
	return a;
}

int &msub(int &a, int b)
{
	a -= b;
	if(a < 0) a += mod;
	return a;
}

int &mmult(int &a, int b)
{
	return a = (ll)a * b % mod;
}

int mdiv(ll a, ll b, ll m)
{
	a = (a % m + m) % m;
	b = (b % m + m) % m;
	if(a % b == 0) return a / b;
	return (a + m * mdiv(-a, m, b)) / b;
}

#define N 1012
#define M 1012

int n, m, q;
int A[N];

int main()
{
#ifdef XDEBUG
	freopen("in.txt", "rt", stdin);
#else
	freopen("x.in", "rt", stdin);
	freopen("x.out", "wt", stdout);
#endif

	int i, j, k;
	char c;
	int a, d;
	
	int ts;	
	in(d, ts);
	printf("Case #%d:\n", ts);
#if 1
	int tss;
	in(d, tss);
	in(d, n); in(d, m); in(d, q);
	int qq = q;
	rep(ts, 1, tss + 1)
#else
	for(ts = 1; in(d, n) > 0; ++ts)
#endif
	{
#ifndef XDEBUG
		cerr << ts << endl;
#endif
		int res = 0;
		int p[10];
		rep(i, 0, 10) p[i] = 0;
		q = qq;
		for(; q--;)
		{
			in(d, a);
			int x = 0;
			x = 0;
			k = 2;
			for(; a % k == 0; a /= k) ++x;
			maxx(p[k], x);
			x = 0;
			k = 3;
			for(; a % k == 0; a /= k) ++x;
			maxx(p[k], x);
			x = 0;
			k = 5;
			for(; a % k == 0; a /= k) ++x;
			maxx(p[k], x);
		}
		rep(i, 0, n) A[i] = 2;
		rep(i, 0, p[3]) A[i] = 3;
		rep(i, i, p[3] + p[5]) A[i] = 5;
		for(; n - i < p[2];) A[i++] = 4, p[2] -= 2;
		rep(i, 0, n) out(d, A[i]); nl;
	}

	return 0;
}
