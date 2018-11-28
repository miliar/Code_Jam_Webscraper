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
const ld eps = 1e-12;

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
inline void read(T &x)
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

#define maxn 110

struct status
{
	ld r, c;
}a[maxn];

ld v, x;
int n;
bool flag;

inline bool cmp1(const status &a, const status &b)
{
	return a.c < b.c;
}

inline bool cmp2(const status &a, const status &b)
{
	return a.c > b.c;
}

inline ld cal_min(ld t)
{
	sort(a + 1, a + n + 1, cmp1);
	ld nowv = 0, ans = 0;
	for (int i = 1; i <= n; i ++)
	{
		if (nowv + a[i].r * t >= v)
		{
			ans = (nowv * ans + (v - nowv) * a[i].c) / v;
			return ans;
		}
		else
		{
			ans = (nowv * ans + a[i].r * t * a[i].c) / (nowv + a[i].r * t);
			nowv += a[i].r * t;
		}
	}
	return 1e50;
}

inline ld cal_max(ld t)
{
	sort(a + 1, a + n + 1, cmp2);
	ld nowv = 0, ans = 0;
	for (int i = 1; i <= n; i ++)
	{
		if (nowv + a[i].r * t >= v)
		{
			ans = (nowv * ans + (v - nowv) * a[i].c) / v;
			return ans;
		}
		else
		{
			ans = (nowv * ans + a[i].r * t * a[i].c) / (nowv + a[i].r * t);
			nowv += a[i].r * t;
		}
	}
	return -1e50;
}

inline bool check(ld t)
{
	ld _min = cal_min(t), _max = cal_max(t);
	if (_min - eps < x && _max + eps > x)
	{
		flag = 1;
		return 1;
	}
	return 0;
}

int main()
{
	int T;
	read(T);
	for (int Case = 1; Case <= T; Case ++)
	{
		printf("Case #%d: ", Case);
		flag = 0;
		read(n);
		cin >> v >> x;
		for (int i = 1; i <= n; i ++)
			cin >> a[i].r >> a[i].c;
		ld l = 0, r = 1e12;
		for (int times = 0; times <= 10000; times ++)
		{
			ld mid = (l + r) / 2;
			if (check(mid))
				r = mid;
			else
				l = mid;
		}
		if (!flag)
			puts("IMPOSSIBLE");
		else
			printf("%.9f\n", (double)l);
		cerr << Case << endl;
	}
	return 0;
}

