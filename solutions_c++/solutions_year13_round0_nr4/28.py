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
#define M 222

int n, m, q;
vector<int> A[N];
vector<int> X[M];
int I[N];
bool B[N];
int C[M];
int R[N];

int CC[M];
bool BB[N];
bool BBB[M];

void dfs(int i);

void dfss(int i)
{
	BBB[i] = 1;
	int j, k;
	rep(k, 0, X[i].size())
	{
		j = X[i][k];
		if(!BB[j]) dfs(j);
	}
}

void dfs(int i)
{
	BB[i] = 1;
	int j, k;
	rep(k, 0, A[i].size())
	{
		j = A[i][k];
		if(!BBB[j]) dfss(j);
	}
}

bool can()
{
	int i, j, k;
	rep(i, 0, M) CC[i] = C[i];
	rep(i, 0, n) if(!B[i]) --CC[I[i]];
	rep(i, 0, n) if(!B[i]) rep(k, 0, A[i].size())
	{
		j = A[i][k];
		++CC[j];
	}
	rep(i, 0, M) if(CC[i] < 0) return 0;
	rep(i, 0, n) BB[i] = B[i];
	rep(i, 0, M) BBB[i] = 0;
	rep(i, 0, M) if(C[i] && !BBB[i]) dfss(i);
	rep(i, 0, n) if(!BB[i]) return 0;
	return 1;
}

bool fnd(int t = 0)
{
	if(t == n) return 1;
	if(!can()) return 0;
	int i, j, k;
	rep(i, 0, n) if(!B[i] && C[I[i]])
	{
		B[i] = 1;
		--C[I[i]];
		rep(k, 0, A[i].size())
		{
			j = A[i][k];
			++C[j];
		}
		R[t] = i;
		if(fnd(t + 1)) return 1;
		B[i] = 0;
		++C[I[i]];
		rep(k, 0, A[i].size())
		{
			j = A[i][k];
			--C[j];
		}
	}
	cerr << "error" << endl;
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
#ifndef XDEBUG
		cerr << ts << endl;
#endif
		in(d, m); in(d, n);
		rep(i, 0, M) X[i].clear(), C[i] = 0;
		rep(i, 0, n) B[i] = 0, A[i].clear();
		rep(i, 0, m) in(d, a), ++C[a];
		rep(i, 0, n)
		{
			in(d, I[i]);
			X[I[i]].push_back(i);
			in(d, m);
			rep(k, 0, m) in(d, a), A[i].push_back(a);
		}
		int res = fnd();
		printf("Case #%d: ", ts);
		if(!res) out(s, "IMPOSSIBLE");
		else rep(i, 0, n) outf(d, R[i] + 1);
		nl;
	}

	return 0;
}
