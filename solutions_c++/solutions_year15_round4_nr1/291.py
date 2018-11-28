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

#define map asdfasdf

const int dx[] = {-1, 0, 1, 0};
const int dy[] = {0, 1, 0, -1};

#define maxn 110

int n, m;
int gxx;
int map[maxn][maxn];
int vis[maxn][maxn];
char tmp[maxn];

inline bool out(int x, int y)
{
	if (x <= 0 || x > n)
		return 1;
	if (y <= 0 || y > m)
		return 1;
	return 0;
}

inline bool find(int x, int y, int d)
{
	x += dx[d];
	y += dy[d];
	while (!out(x, y))
	{
		if (map[x][y] != -1)
			return 1;
		x += dx[d];
		y += dy[d];
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
		read(n);
		read(m);
		for (int i = 1; i <= n; i ++)
		{
			scanf("%s", tmp + 1);
			for (int j = 1; j <= m; j ++)
				if (tmp[j] == '^')
					map[i][j] = 0;
				else if (tmp[j] == '>')
					map[i][j] = 1;
				else if (tmp[j] == 'v')
					map[i][j] = 2;
				else if (tmp[j] == '<')
					map[i][j] = 3;
				else
					map[i][j] = -1;
		}
		int ans = 0;
		for (int i = 1; i <= n; i ++)
		{
			for (int j = 1; j <= m; j ++)
			{
				if (map[i][j] == -1)
					continue;
				vis[i][j] = gxx;
				if (find(i, j, map[i][j]))
					continue;
				bool flag = 0;
				for (int d = 0; d < 4; d ++)
					if (find(i, j, d))
						flag = 1;
				if (!flag)
				{
					ans = -1;
					break;
				}
				ans ++;
			}
			if (ans == -1)
				break;
		}
		if (ans == -1)
			puts("IMPOSSIBLE");
		else
			printf("%d\n", ans);
	}
	return 0;
}

