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

const int MAXN = 10004;

int nt;
int a[MAXN];
int n, X;

inline void init()
{
	scanf("%d%d", &n, &X);
	for (int i = 0; i < n; ++i)
		scanf("%d", &a[i]);
	sort(a, a + n);
}

inline int solve()
{
	int res = 0;
	int i = 0, j = n - 1;
	while (i <= j)
	{
		if (i == j)
		{
			++res;
			break;
		}
		if (a[i] + a[j] <= X)
		{
			++i;
			--j;
			++res;
			continue;
		}
		--j;
		++res;
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