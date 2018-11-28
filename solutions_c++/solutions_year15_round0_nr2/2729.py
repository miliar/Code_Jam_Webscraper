#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cmath>
#include <ctime>
#include <cctype>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <deque>
#include <bitset>
#include <iostream>
#include <sstream>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair <int, int> pii;
typedef pair <int, pii> piii;
typedef long double ld;

#define x first
#define y second
#define mp make_pair
#define pb push_back
#define sz(X) ((int)((X).size()))

const int int_inf = 0x3f3f3f3f;
const ll ll_inf = 0x3f3f3f3f3f3f3f3fll;
const double pi = acos(-1.0);
const double eps = 1e-8;

template <class T>
inline T abs(const T x)
{
	return x < 0 ? -x : x;
}

template <class T>
inline void get_min(T &a, T b)
{
	if (a > b)
		a = b;
}

template <class T>
inline void get_max(T &a, T b)
{
	if (a < b)
		a = b;
}

template <class T>
inline void fix(T &a, T mo)
{
	while (a >= mo)
		a -= mo;
	while (a < 0)
		a += mo;
}

template <class T>
inline void inc(T &a, T b, T mo)
{
	a += b;
	fix(a, mo);
}

template <class T>
inline void dec(T &a, T b, T mo)
{
	a -= b;
	fix(a, mo);
}

template <class T>
inline T sqr(T x)
{
	return x * x;
}

template <class T>
inline int sgn(T x)
{
	if (x > eps)
		return 1;
	if (x < -eps)
		return -1;
	return 0;
}

template <class T>
inline void read_int(T &x)
{
	x = 0;
	char ch;
	bool flag = 0;
	while (ch = getchar(), !isdigit(ch) && ch != '-');
	if (ch == '-')
		flag = 1;
	else
		x = ch - '0';
	while (ch = getchar(), isdigit(ch))
		x = (x << 3) + x + x + ch - '0';
	if (flag)
		x = -x;
}

int a[2010];

int main()
{
	int T;
	read_int(T);
	for (int Case = 1; Case <= T; Case ++)
	{
		printf("Case #%d: ", Case);
		int n;
		read_int(n);
		memset(a, 0, sizeof(a));
		for (int i = 1; i <= n; i ++)
		{
			int x;
			read_int(x);
			a[x] ++;
		}
		int ans = int_inf;
		for (int _max = 1000; _max; _max --)
		{
			int now = 0;
			for (int i = 1000; i > _max; i --)
			{
				int x = (i + _max - 1) / _max - 1;
				now += x * a[i];
			}
			get_min(ans, now + _max);
		}
		printf("%d\n", ans);
	}
	return 0;
}

