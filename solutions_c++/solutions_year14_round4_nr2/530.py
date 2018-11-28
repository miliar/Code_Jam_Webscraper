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

const int MAXN = 1003;

int nt;
int n;
int a[MAXN];
int b[MAXN];
map <int, int> pos;

inline void init()
{
	pos.clear();
	scanf("%d", &n);
	for (int i = 0; i < n; ++i)
	{
		scanf("%d", &a[i]);
		pos[a[i]] = i;
		b[i] = a[i];
	}
	sort(b, b + n);
}

inline void smart_swap(int x, int y)
{
	int tmp = pos[a[x]];
	pos[a[x]] = pos[a[y]];
	pos[a[y]] = tmp;
	swap(a[x], a[y]);
}

inline int dist(int x, int y)
{
	return abs(x - y);
}

inline int solve()
{
	int L = 0, R = n - 1;
	int res = 0;
	for (int i = 0; i < n; ++i)
	{
		int x = b[i];
		int p = pos[x];
		if (dist(R, p) < dist(L, p))
		{
			res += dist(R, p);
			for (int i = p; i < R; ++i)
				smart_swap(i, i + 1);
			--R;
		} else {
			res += dist(L, p);
			for (int i = p; i > L; --i)
				smart_swap(i, i - 1);
			++L;
		}
	}
	return res;
}

int main()
{	
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	
	scanf("%d", &nt);
	for (int tn = 1; tn <= nt; ++tn)
	{
		init();
		int res = solve();
		printf("Case #%d: %d\n", tn, res);
	}

    return 0;
}