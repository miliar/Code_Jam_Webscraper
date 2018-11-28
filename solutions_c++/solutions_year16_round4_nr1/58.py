#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <string>
#include <cstring>
#include <ctime>
#include <cassert>
#include <queue>
#include <stack>
#include <bitset>
#define y1 y11
#define fs first
#define sc second
#define mp make_pair
#define pb push_back
#define mt make_tuple
#define NAME ""

using namespace std;
	
typedef long long ll;
typedef long double ld;

const ld PI = acos(-1.0);

//r  p   s
bool go(int& a, int &b, int &c)
{
	assert((a + b + c) % 2 == 0);
	int na = (a + c - b) / 2, nb = (a + b - c) / 2, nc = (b + c - a) / 2;
	if ((na < 0) || (nb < 0) || (nc < 0)) return false;
	assert(na + nb == a);
	assert(na + nc == c);
	assert(nb + nc == b);
	a = na, b = nb, c = nc;
	return true;
}

string dfs(int v, int n)
{
	if (n == 0)
	{
		char c = "RPS"[v];
		string ans = "";
		ans += c;
		return ans;
	}
	string s1 = dfs(v, n - 1);
	string s2;
	if (v == 0) s2 = dfs(2, n - 1);
	if (v == 1) s2 = dfs(0, n - 1);
	if (v == 2) s2 = dfs(1, n - 1);
	return min(s1, s2) + max(s1, s2);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++)
	{
		int n, r, p, s;
		cin >> n >> r >> p >> s;
		cout << "Case #" << test << ": ";
		bool ok = true;
		for (int i = 0; i < n; i++)
		{
			if (!go(r, p, s))
			{
				cout << "IMPOSSIBLE" << endl;
				ok = false;
				break;
			}
		}
		if (ok) 
		{
			if (r == 1) cout << dfs(0, n) << endl;
			if (p == 1) cout << dfs(1, n) << endl;
			if (s == 1) cout << dfs(2, n) << endl;
		}
	}
	return 0;
}