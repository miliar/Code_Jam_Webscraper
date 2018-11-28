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
char A[N];
char B[N];

void inc(char *S)
{
	int i;
	reps(i, S);
	int d = 1;
	repb(i, i, 0)
	{
		S[i] += d;
		d = 0;
		if(S[i] == '9' + 1)
		{
			d = 1;
			S[i] = '0';
		}
	}
	if(d)
	{
		reps(i, S);
		repb(i, i + 1, 0) S[i + 1] = S[i];
		S[0] = '1';
	}
}

char X[N];
char Y[N];

bool check(char *X, char *S)
{
	int n = strlen(X);
	int m = strlen(S);
	reverse(X, X + n);
	int i, j, k;
	rep(i, 0, m) Y[i] = '0';
	Y[i] = 0;
	rep(i, 0, n) if(X[i] != '0') 
		rep(j, 0, n) if(X[j] != '0') Y[i + j] += (X[i] - '0') * (X[j] - '0');
	reverse(Y, Y + m);
	assert(Y[0] > '0');
	reverse(X, X + n);
	return (string)Y < (string)S;
}

int fnd(char *S)
{
	int n = strlen(S);
	int a;
	int res = 0;
	if(n == 1) 
	{
		sscanf(S, "%d", &a);
		if(1 < a) ++res;
		if(4 < a) ++res;
		return res;
	}
	int i, j, k;
	res = 3;
	for(i = 2; 2 * i - 1 < n; ++i)
	{
		res += 1 + (i & 1);
		int r = 1;
		rep(k, 0, 4)
		{
			res += r * (1 + (i & 1) + (i & 1) * (k < 2));
			r = r * (i / 2 - k - 1) / (k + 1);
		}
	}
	if(2 * i - 1 == n)
	{
		rep(j, 0, i) X[j] = '0';
		X[j] = 0;
		X[0] = X[i - 1] = '2';
		res += check(X, S);
		if(i & 1)
		{
			X[i / 2] = '1';
			res += check(X, S);
			X[i / 2] = '0';
		}
		X[0] = X[i - 1] = '1';
		res += check(X, S);
		if(i & 1)
		{
			X[i / 2] = '1';
			res += check(X, S);
			X[i / 2] = '2';
			res += check(X, S);
			X[i / 2] = '0';
		}
		int k1, k2, k3;
		rep(k1, 1, i / 2)
		{
			X[k1] = X[i - 1 - k1] = '1';
			res += check(X, S);
			if(i & 1)
			{
				X[i / 2] = '1';
				res += check(X, S);
				X[i / 2] = '2';
				res += check(X, S);
				X[i / 2] = '0';
			}
			rep(k2, k1 + 1, i / 2)
			{
				X[k2] = X[i - 1 - k2] = '1';
				res += check(X, S);
				if(i & 1)
				{
					X[i / 2] = '1';
					res += check(X, S);
					X[i / 2] = '0';
				}
				rep(k3, k2 + 1, i / 2)
				{
					X[k3] = X[i - 1 - k3] = '1';
					res += check(X, S);
					if(i & 1)
					{
						X[i / 2] = '1';
						res += check(X, S);
						X[i / 2] = '0';
					}
					X[k3] = X[i - 1 - k3] = '0';
				}
				X[k2] = X[i - 1 - k2] = '0';
			}
			X[k1] = X[i - 1 - k1] = '0';
		}
	}
	return res;
}

int main()
{
#ifdef XDEBUG
	freopen("in.txt", "rt", stdin);
	//freopen("out.txt", "wt", stdout);
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
		cerr << ts << endl;
		in(s, A);
		in(s, B);
		inc(B);
		int res = fnd(B) - fnd(A);
		printf("Case #%d: ", ts);
		out(d, res); nl;
	}

	return 0;
}
