#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES

#include <algorithm>
#include <cstdio>
#include <ctime>
#include <map>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <stack>
#include <queue>
#include <deque>
#include <cassert>
#include <iostream>
#include <cmath>
#include <sstream>
#include <complex>
#include <memory.h>

using namespace std;

#pragma comment(linker, "/STACK:128000000")

typedef long long int64;
typedef unsigned long long uint64;

#define y1 _dsfkjdsfksdj
#define y0 _sfsdkfdop

typedef unsigned uint;
typedef vector<int64> vi64;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
typedef pair<int,string> pis;
typedef pair<int64,int64> pii64;
typedef pair<int,pii> piii;
typedef pair<pii,pii> piiii;
typedef vector<pii> vpii;
typedef vector<vpii> vvpii;
typedef pair<double,int> pdi;
typedef pair<double,double> pdd;
typedef pair<int,string> pis;

int nt;
int n, m;
string a[8];
int b[8];
int res;
int cnt;

inline void init()
{
	cin >> n >> m;
	for (int i = 0; i < n; ++i)
		cin >> a[i];
	sort(a, a + n);
}

inline int lcp(string &s1, string &s2)
{
	int l = min((int)s1.length(), (int)s2.length());
	for (int i = 0; i < l; ++i)
		if (s1[i] != s2[i])
			return i;
	return l;
}

inline int get()
{
	int res = 0;
	for (int i = 0; i < n; ++i)
	{
		int p = 0;
		for (int j = 0; j < i; ++j)
			if (b[i] == b[j])
				p = max(p, lcp(a[i], a[j]));
		res += ((int)a[i].length() - p);
	}
	return res;
}

inline int check()
{
	set <int> was;
	was.clear();
	for (int i = 0; i < n; ++i)
		was.insert(b[i]);
	return ((int)was.size() == m);
}

void rec(int x)
{
	if (x == n)
	{
		if (!check()) return;
		int cur = get();
		if (cur > res)
		{
			res = cur;
			cnt = 0;
		}
		if (cur == res)
			++cnt;
		return;
	}

	for (int t = 0; t < m; ++t)
	{
		b[x] = t;
		rec(x + 1);
	}
}

inline void solve()
{
	res = 0;
	cnt = 0;
	memset(b, -1, sizeof b);
	rec(0);
}

int main()
{	
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	
	cin >> nt;
	for (int tn = 1; tn <= nt; ++tn)
	{
		cerr << tn << endl;
		init();
		solve();
		res += m;
		printf("Case #%d: %d %d\n", tn, res, cnt);
	}

    return 0;
}