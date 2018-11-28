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

inline int area(pii a, pii b, pii c)
{
	return (b.first - a.first) * (c.second - a.second) - (b.second - a.second) * (c.first - a.first);
}
 
inline bool intersect_1(int a, int b, int c, int d)
{
	if (a > b)  swap (a, b);
	if (c > d)  swap (c, d);
	return max(a,c) <= min(b,d);
}
 
bool intersect (pii a, pii b, pii c, pii d)
{
	return intersect_1(a.first, b.first, c.first, d.first)
		&& intersect_1(a.second, b.second, c.second, d.second)
		&& area(a,b,c) * area(a,b,d) <= 0
		&& area(c,d,a) * area(c,d,b) <= 0;
}

int nt;
int n;
pii a[11];
int order[11];
int ans[11];

inline void init()
{
	cin >> n;
	for (int i = 0; i < n; ++i)
		cin >> a[i].first >> a[i].second;
}

inline int get_area()
{
	for (int i = 0; i < n; ++i)
	{
		int ni = (i + 1) % n;
		for (int j = 0; j < i; ++j)
		{
			int nj = (j + 1) % n;
			if (i == j || i == nj) continue;
			if (ni == j || ni == nj) continue;
			if (intersect(a[order[i]], a[order[ni]], a[order[j]], a[order[nj]])) return -1;
		}
	}
	int S = 0;
	for (int i = 0; i < n; ++i)
	{
		int j = (i + 1) % n;
		S += a[order[i]].first * a[order[j]].second - a[order[i]].second * a[order[j]].first;
	}
	if (S < 0) S = -S;
	return S;
}

inline int slow_solve()
{
	int res = -1;
	for (int i = 0; i < n; ++i)
		order[i] = i;
	
	do
	{
		int cur = get_area();
		if (cur == -1) continue;
		/*
		for (int i = 0; i < n; ++i)
			cout << order[i] << " ";
		cout << "--> " << cur;
		cout << endl;
		*/
		if (res < cur)
		{
			res = cur;
			for (int i = 0; i < n; ++i)
				ans[i] = order[i];
		}
	} while (next_permutation(order, order + n));
	
	return res;
}

int main()
{
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

	cin >> nt;
	for (int tn = 1; tn <= nt; ++tn)
	{
		cerr << tn << endl;
		init();
		int res = slow_solve();
		cout.precision(15);
		cout << "Case #" << tn << ": "; 
		for (int i = 0; i < n; ++i)
		{
			if (i) cout << " ";
			cout << ans[i];
		}
		cout << endl;
		//cout << res << endl;
	}

    return 0;
}