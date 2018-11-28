#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <sstream>

#include <vector>
#include <algorithm>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <queue>
#include <string>
#include <cstring>
#include <string.h>

#include <time.h>
#include <cassert>
#include <memory.h>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define fornd(i, n) for(int i = (int)(n-1); i >= 0; i--)
#define forab(i, a, b) for(int i = (int)a; i <= (int)b; i++)
#define forabd(i, b, a) for(int i = (int)b; i >= (int)a; i--)

#define pb push_back
#define mp make_pair
#define sz(a) ((int)(a).size())
#define _(a, val) memset(a, val, sizeof(a))
#define all(a) (a).begin(), (a).end()

typedef long long lint;
typedef long double ld;

const int INF = 1000*1000*1000;
const lint LINF = (lint)INF*(lint)INF;

void freopen(string s)
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
#else
	if (s != "")
	{
		freopen((s + ".in").c_str(), "r", stdin);
		freopen((s + ".out").c_str(), "w", stdout);
	}
#endif
}

const int NMAX = 100100;

int T;
int n;
int m[NMAX];

void read()
{
	cin >> n;
	forn(i, n)
	{
		cin >> m[i];
	}
}

void solve()
{
	int max_diff = 0;
	forn(i, n-1)
	{
		max_diff = max(max_diff, m[i] - m[i+1]);
	}
	
	int ans1 = 0, ans2 = 0;
	forn(i, n-1)
	{
		ans1 += max(0, m[i] - m[i+1]);
		ans2 += min(max_diff, m[i]);
	}

	cout << "Case #" << T << ": " << ans1 << ' ' << ans2 << endl;
}

int main()
{
	freopen("A-large");

	int t;
	cin >> t;
	forn(i, t)
	{
		T = i + 1;
		read();
		solve();
	}

	return 0;
}