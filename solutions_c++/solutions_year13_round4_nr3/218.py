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
int A[N], B[N];
int X[N];
int AA[N], BB[N];
bool D[N];

bool good(int l)
{
	int i, j;
	rep(i, 0, l)
	{
		AA[i] = 0;
		rep(j, 0, i) if(X[i] > X[j]) maxx(AA[i], AA[j] + 1);
	}
	rep(i, 0, l) if(AA[i] != A[i]) return 0;
	if(l == n)
	{
		repb(i, n, 0)
		{
			BB[i] = 0;
			repb(j, n, i) if(X[i] > X[j]) maxx(BB[i], BB[j] + 1);
		}
		rep(i, 0, l) if(BB[i] != B[i]) return 0;
	}
	return 1;
}

bool fnd(int i)
{
	if(!good(i)) return 0;
	if(i == n) return 1;
	int res = A[i] + B[i];
	int j, k;
	rep(j, 0, n) D[j] = 0;
	rep(j, 0, i) D[X[j]] = 1;
	int a = B[i];
	rep(j, 0, n) if(!D[j]) if(--a < 0)
	{
		maxx(res, j);
		break;
	}
	int r = A[i] == 0 ? 0 : inf;
	rep(j, 0, i) if(A[j] == A[i] - 1) minn(r, X[j] + 1);
	maxx(res, r);
	rep(j, res, n) if(!D[j])
	{
		D[j] = 1;
		X[i] = j;
		//rep(k, 0, i) if(X[k] == j) break;
		if(fnd(i + 1))
			return 1;
		D[j] = 0;
	}
	return 0;
}

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
#if 1
	int tss;
	in(d, tss);
	rep(ts, 1, tss + 1)
#else
	for(ts = 1; in(d, n) > 0; ++ts)
#endif
	{
		printf("Case #%d: ", ts);
#ifndef XDEBUG
		cerr << ts << endl;		
#endif
		in(d, n);
		rep(i, 0, n) in(d, A[i]), --A[i];
		rep(i, 0, n) in(d, B[i]), --B[i];
		fnd(0);
		int res = 0;
		rep(i, 0, n) outf(d, X[i] + 1);
		nl;
	}

	return 0;
}
