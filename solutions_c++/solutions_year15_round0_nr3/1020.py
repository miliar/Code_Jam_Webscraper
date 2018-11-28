#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker,"/STACK:64000000")
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <memory.h>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <cassert>
#include <time.h>
#include <bitset>

using namespace std;

#define mp make_pair
#define pb push_back
#define _(a,b) memset( (a), b, sizeof( a ) )
#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()
#ifdef WIN32
#define dbg(...) {fprintf(stderr, __VA_ARGS__); fflush(stderr);}
#define dbgx(x) {cerr << #x << " = " << x << endl;}
#define dbgv(v) {cerr << #v << " = {"; for (typeof(v.begin()) it = v.begin(); it != v.end(); it ++) cerr << *it << ", "; cerr << "}"; cerr << endl;}
#else
#define dbg(...) { }
#define dbgx(x) { }
#define dbgv(v) { }
#endif

typedef unsigned long long ull;
typedef long long lint;
typedef pair < int , int > pii;
typedef long double ld;

const int INF = 1000 * 1000 * 1000;
const lint LINF = 1000000000000000000LL;
const double eps = 1e-9;

void prepare()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
}

const int nmax = 10005;

const string alpha = "1ijk";
const string ops[] = 
{
	"1ijk",
	"i1kj",
	"jk1i",
	"kji1"
};
const string opsSign[] = 
{
	"++++",
	"+-+-",
	"+--+",
	"++--"
};

int getIndex(const char &val)
{
	return alpha.find(val);
}

int getSign(char a, char b)
{
	if (a == '+' && b == '+' ||
		a == '-' && b == '-')
	{
		return '+';
	}
	return '-';
}

struct Vec
{
	char val, sign;

	Vec()
	{
		val = '1';
		sign = '+';
	}

	Vec (char _val, char _sign)
	{
		val = _val;
		sign = _sign;
	}

	Vec (char _val)
	{
		val = _val;
		sign = '+';
	}

	Vec operator * (const Vec &oth) const
	{
		int i = getIndex(val);
		int j = getIndex(oth.val);
		int resVal = ops[i][j];
		int resSign = getSign(getSign(sign, oth.sign), opsSign[i][j]);
		return Vec(resVal, resSign);
	}
};

int n;
char s[nmax];
lint x;
Vec a[nmax];

void read()
{
	scanf("%d%lld", &n, &x);
	scanf("%s", s);
	for (int i = 0; i < n; i ++)
		a[i] = Vec(s[i]);
}

Vec calcTotal()
{
	Vec single = Vec('1');
	for (int i = 0; i < n; i ++)
		single = single * a[i];
	
	Vec cur = single, result = Vec('1');
	for (lint i = 0; (1LL << i) <= x; i ++)
	{
		if (x & (1LL << i))
		{
			result = result * cur;
		}
		cur = cur * cur;
	}
	return result;
}

bool check()
{
	Vec cur = Vec('1');
	bool was_i = false;
	bool was_j_after_i = false;

	for (int iter = 0; iter <= (int)min(1000LL, x); iter ++)
	{
		for (int i = 0; i < n; i ++)
		{
			cur = cur * a[i];
			if (cur.val == 'i' && cur.sign == '+')
			{
				was_i = true;
			}
			if (was_i && cur.val == 'k' && cur.sign == '+')
			{
				was_j_after_i = true;
			}
		}
	}
	return was_i && was_j_after_i;
}

bool solve()
{
	Vec total = calcTotal();
	if (!(total.val == '1' && total.sign == '-'))
	{
		printf("NO\n");
		return false;
	}

	if (!check())
	{
		printf("NO\n");
		return false;
	}
	printf("YES\n");
	return false;
}

int main()
{
	prepare();
	int t;
	scanf("%d",&t);
	for (int i = 0; i < t; i ++)
	{
		dbg("Test %d\n", i);
		printf("Case #%d: ", i + 1);
		read();
		solve();
	}
	return 0;
}
