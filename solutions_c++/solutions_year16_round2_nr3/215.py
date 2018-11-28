﻿#pragma comment (linker, "/STACK:256000000")
 
#define _USE_MATH_DEFINES
#define _CRT_NO_DEPRECEATE
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <iomanip>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <vector>
#include <utility>
#include <algorithm>
#include <functional>
#include <set>
#include <map>
#include <cmath>
#include <memory.h>
#include <sstream>
#include <cassert>
#include <ctime>
#include <complex>
#include <random>
 
using namespace std;
 
typedef unsigned int uint32;
typedef long long int64;
typedef unsigned long long uint64;
typedef pair<int, int> pii;
typedef pair<int64, int64> pll;
typedef pair<pii, pii> piiii;
typedef pair<int64, int> pli;
typedef pair<double, double> pdd;
 
#define pb push_back
#define sq(x) ((x)*(x))
#define tmin(x,y,z) (min(min((x),(y)),(z)))
#define tmax(x,y,z) (max(max((x),(y)),(z)))
#define rand32() (((unsigned int)(rand()) << 16) | (unsigned int)(rand()))
#define rand64() (((unsigned int64)(rand32()) << 16) | (unsigned int64)(rand32()))
#define bit(mask, b) ((mask >> b) & 1)
#define biton(mask, bit) (mask | (((uint64)(1)) << bit))
#define bitoff(mask, bit) (mask & (~(((uint64)(1)) << bit)))
#define bitputon(mask, bit) (mask |= (((uint64)(1)) << bit))
#define bitputoff(mask, bit) (mask &= (~(((uint64)(1)) << bit)))
#define FAIL() (*((int*)(0)))++
#define INF ((int)(1e9) + 1337)
#define EPS (1e-11)
#define y1 yy1
#define y0 yy0
#define j0 jj0

//#define HMOD (1000000000000000003LL)
//#ifdef _MY_DEBUG
//#define HMOD 1000000007
//#endif
//#define HBASE 524287

//mt19937 ggen;

const long double PI = acosl((long double)-1.0);
const int64 LINF = 8e18;
const int MOD = 1000000007;

const int MAXN = 1010;

int test;

int n;
map <string, int> words1, words2;
string s1[MAXN], s2[MAXN];
int num1[MAXN], num2[MAXN];
vector <vector <int> > g;
bool used[MAXN];
int mt[MAXN];
int k;

bool try_kuhn (int v)
{
	if (used[v])
	{
		return false;
	}
	used[v] = true;
	for (int i = 0; i < g[v].size(); i++)
	{
		int to = g[v][i];
		if (!mt[to] || try_kuhn (mt[to]))
		{
			mt[to] = v;
			return true;
		}
	}
	return false;
}

char buf[MAXN];

inline int get_num(map <string, int> &words, string &s)
{
	auto it = words.find(s);
	if (it == words.end())
	{
		int val = words.size() + 1;
		return words[s] = val;
	}
	else
	{
		return it->second;
	}
}

inline string read()
{
	scanf ("%s", &buf);
	return buf;
}

void solve()
{
	words1.clear();
	words2.clear();
	scanf ("%d", &n);
	for (int i = 1; i <= n; i++)
	{
		s1[i] = read();
		num1[i] = get_num(words1, s1[i]);
		s2[i] = read();
		num2[i] = get_num(words2, s2[i]);
	}
	g.clear();
	g.resize(words1.size() + 1);
	for (int i = 1; i <= n; i++)
	{
		g[num1[i]].push_back(num2[i]);
	}
	memset(used, 0, sizeof(bool) * (words1.size() + 5));
	memset(mt, 0, sizeof(int) * (words2.size() + 5));
	int k = 0;
	for (int i = 1; i <= words1.size(); i++)
	{
		memset(used, 0, sizeof(int) * (words1.size() + 5));
		if (try_kuhn(i))
		{
			k++;
		}
	}
	int good = words1.size() + words2.size() - k;
	int failed = n - good;
	printf("Case #%d: %d\n", test, failed);
}

#define TASK "substr"

int main()
{
    //ios_base::sync_with_stdio(false); cin.tie(0);
#ifdef _MY_DEBUG
    freopen("input.txt", "rt", stdin); freopen("output.txt", "wt", stdout);
#else
    //freopen(TASK ".in", "rt", stdin); freopen(TASK ".out", "wt", stdout);
#endif
    srand(1313);
    
	int tests = 1;
	scanf ("%d", &tests);
	for (test = 1; test <= tests; test++)
	{
		solve();
	}
    return 0;
}