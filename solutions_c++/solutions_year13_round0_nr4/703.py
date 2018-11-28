#pragma warning(disable: 4996)
#pragma comment(linker,"/STACK:64000000")
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <memory.h>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <cassert>
#include <time.h>
#include <bitset>
#include <exception>
#include <functional>

using namespace std;

#define mp make_pair
#define pb push_back
#define _(a,b) memset( (a), b, sizeof( a ) )
#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()
#define fori(i,n) for (int i = 0; i < (n); ++ i)
#define forv(i,v) for (int i = 0; i < (sz(v)); ++ i)
typedef unsigned long long ull;
typedef long long lint;
typedef pair < int , int > pii;
typedef long double ld;

const int INF = 1000 * 1000 * 1000;
const lint LINF = 1000000000000000000LL;
const double eps = 1e-9;

void prepare(string s)
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
#else
	if (s == "input_txt")
	{
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	}
	else if (sz(s) != 0)
	{
		freopen((s + ".in").c_str(),"r",stdin);
		freopen((s + ".out").c_str(),"w",stdout);
	}
#endif
}
	

void read(vector< string > &a)
{
	string s;
	cin >> s;
	cin >> s;
	while (s != "}")
	{
		a.push_back(s.substr(1, sz(s) - 2));
		cin >> s;
	}
}
void read(string &s)
{
	cin >> s;
	s = s.substr(1, sz(s) - 2);
}

void read(vector< int > &a)
{
	string s;
	cin >> s;
	cin >> s;
	while (s != "}")
	{
		a.push_back(atoi(s.c_str()));
		cin >> s;
	}
}

void Add(map<lint, int> &a, map<lint, int> &b)
{
	for (auto it = b.begin(); it != b.end(); ++ it)
		a[it->first] += it->second;
}


bool solve()
{
	int cnt_start, n;
	cin >> cnt_start >> n;
	map<lint, int> start;
	for (int i = 0; i < cnt_start; ++ i)
	{
		lint k;
		cin >> k;
		start[k] ++ ;
	}
	vector<int> open(n);
	vector< map<lint, int> > add(n);
	for (int i = 0; i < n;++ i)
	{
		int cur_cnt;
		cin >> open[i] >> cur_cnt; 
		for (int j = 0; j < cur_cnt; ++ j)
		{
			lint k;
			cin >> k;
			add[i][k]++;
		}
	}

	vector<int> dp(1 << n, INF);
	dp[0] = 0;
	queue<int> q;
	q.push(0);

	while (!q.empty())
	{
		int msk = q.front();
		q.pop();
		map<lint, int> keys = start;
		for (int i = 0; i < n; ++ i)
		{
			if (msk & (1 << i))
			{
				Add(keys, add[i]);
				keys[open[i]] --;
			}
		}

		for (int i = 0; i < n; ++ i)
		{
			int nxt = msk | (1 << i);
			if (keys[open[i]] > 0 && dp[nxt] == INF)
			{
				dp[nxt] = i;
				q.push(nxt);
			}
		}
	}

	if (dp.back() == INF)
	{
		cout << "IMPOSSIBLE";
		return false;
	}

	int cur = dp.size() - 1;

	vector<int> ans;
	while (cur != 0)
	{
		ans.push_back(dp[cur]);
		cur ^= 1 << dp[cur];
	}

	reverse(all(ans));

	for (int i = 0; i < sz(ans); ++ i)
	{
		if (i)
			cout << ' ';
		cout << ans[i] + 1;
	}

	return false;
}

int main()
{
	prepare("input_txt");

	int T;
	cin >> T;
	for (int i = 0; i < T; ++ i)
	{
		cout << "Case #" << i + 1 << ": ";
		solve();
#ifndef _DEBUG
		cerr << "Case #" << i + 1 << " is done." << endl;
#endif
		cout << endl;
	}
	return 0;
}
