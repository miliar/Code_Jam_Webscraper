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

#pragma comment(linker, "/STACK:64000000")

typedef long long int64;
typedef unsigned long long uint64;

#define y1 _dsfkjdsfksdj
#define y0 _sfsdkfdop

typedef unsigned uint;
typedef vector<int64> vi64;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef pair<int,string> pis;
typedef pair<int64,int64> pii64;
typedef pair<pii,int> piii;
typedef pair<pii,pii> piiii;
typedef vector<pii> vpii;
typedef vector<vpii> vvpii;
typedef pair<double,int> pdi;
typedef pair<double,double> pdd;

int nt;
int n;
int64 m;
int64 N;

inline void init()
{
	scanf("%d%lld", &n, &m);
	N = (1LL << n);
}

inline int64 check1(int64 X)
{
	int64 Place = 0;
	int64 Y = X - 1;
	for (int i = 0; i < n; ++i)
	{
		if (Y)
		{
			--Y;
			Place += (1LL << (n - i - 1));
		}
		Y >>= 1;
	}
	return Place < m;
}

inline int64 check2(int64 X)
{
	int64 Place = N - 1;
	int64 Y = N - X;
	for (int i = 0; i < n; ++i)
	{
		if (Y)
		{
			--Y;
			Place -= (1LL << (n - i - 1));
		}
		Y >>= 1;
	}
	return Place < m;
}

inline pii64 solve()
{
	pii64 res(-1, -1);
	int64 l = 1, r = N;
	while (l <= r)
	{
		int64 mid = (l + r) >> 1;
		if (check1(mid))
		{
			res.first = mid;
			l = mid + 1;
		} else {
			r = mid - 1;
		}
	}
	l = 1, r = N;
	while (l <= r)
	{
		int64 mid = (l + r) >> 1;
		if (check2(mid))
		{
			res.second = mid;
			l = mid + 1;
		} else {
			r = mid - 1;
		}
	}
	--res.first, --res.second;
	return res;
}

int main()
{
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

    scanf("%d", &nt);
	for (int tn = 1; tn <= nt; ++tn)
	{
		init();
		pii64 res = solve();
		printf("Case #%d: %lld %lld\n", tn, res.first, res.second);
	}

    return 0;
}