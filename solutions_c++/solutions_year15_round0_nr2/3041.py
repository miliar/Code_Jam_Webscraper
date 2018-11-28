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

int T;
int n;
int vals[1010];

void read()
{
	cin >> n;
	forn(i, n)
	{
		cin >> vals[i];
	}
}

int get_cnt(int max_p)
{
	int cnt = 0;
	forn(i, n)
	{
		cnt += (vals[i] - 1) / max_p;
	}
	return cnt;
}

void solve()
{
	int max_val = 0;
	forn(i, n)
	{
		if (max_val < vals[i])
			max_val = vals[i];
	}

	int ans = INF;
	forab(i, 1, max_val)
	{
		ans = min(ans, i + get_cnt(i));
	}

	cout << "Case #" << T << ": " << ans << endl;
}

int main()
{
	freopen("B-large");

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