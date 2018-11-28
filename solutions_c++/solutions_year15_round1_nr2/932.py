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
int n, m;
lint d[NMAX];

void read()
{
	cin >> n >> m;
	forn(i, n)
	{
		cin >> d[i];
	}
}

lint f(lint k)
{
	lint cnt = 0;
	forn(i, n)
	{
		cnt += (k + d[i] - 1) / d[i];
	}
	return cnt;
}

void solve()
{
	int ans = 0;
	
	lint l = 0, r = LINF;
	while (r - l > 1)
	{
		lint c = (l + r) / 2;
		
		if (f(c) >= m)
			r = c;
		else
			l = c;
	}

	lint cnt = 0;
	vector< pair<lint, int> > v;
	forn(i, n)
	{
		lint p = (l + d[i] - 1) / d[i];
		cnt += p;
		v.pb(mp(p * d[i], i));
	}

	sort(all(v));

	ans = v[m - cnt - 1].second + 1;
	
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