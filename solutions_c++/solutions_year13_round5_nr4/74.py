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
int SMASK;
double f[1 << 20];
char was[1 << 20];
int FMASK;

inline void init()
{
	string s;
	cin >> s;
	n = (int)s.length();
	SMASK = 0;
	for (int i = 0; i < n; ++i)
	{
		if (s[i] == 'X') SMASK |= (1 << i);
	}
	FMASK = (1 << n) - 1;
}

double rec(int mask)
{
	if (mask == FMASK) return 0.0;

	if (was[mask]) return f[mask];
	
	was[mask] = 1;
	double res = 0.0;
	double cnt = 0;
	for (int i = 0; i < n; ++i)
	{
		double cost = n;
		for (int j = 0; j < n; ++j)
		{
			int ind = (i + j) % n;
			if (mask & (1 << ind))
			{
				--cost;
				continue;
			}
			res += rec(mask | (1 << ind)) + cost;
			break;
		}
	}
	res /= (double)n;

	return f[mask] = res;
}

inline double slow_solve()
{
	memset(was, 0, sizeof was);
	return rec(SMASK);
}

int main()
{
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

	cin >> nt;
	for (int tn = 1; tn <= nt; ++tn)
	{
		cerr << tn << endl;
		init();
		double res = slow_solve();
		cout.precision(15);
		cout << "Case #" << tn << ": "; 
		cout << fixed << res << endl;
	}

    return 0;
}