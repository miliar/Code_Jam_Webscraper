#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:66777216")
#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <ctime>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <deque>
#include <cassert>
#include <cstdlib>
#include <bitset>
#include <algorithm>
#include <string>
#include <list>
#include <fstream>
#include <cstring>
#include <climits>
#include <random>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;


#define forn(i, n) for (int i = 0; i < (int)n; i++)
#define for1(i, n) for (int i = 1; i <= (int)n; i++)
#define forq(i, s, t) for (int i = s; i <= t; i++)
#define ford(i, s, t) for (int i = s; i >= t; i--)
#define mk make_pair
#define pk push_back
#define outb pop_back
#define ump unordered_map
#define all(v) v.begin(), v.end()
#define X first
#define Y second
#define TIME clock() * 1.0 / CLOCKS_PER_SEC
#define randint(x,y)
#define randlong(x, y)
#define TASK ""

const double eps = 1e-15;
const double pi = acos(-1.0);

const int MAXN = (int)1e5 + 7;
const int INF = (ll)2e9;
const ll LINF = 2e18;

ll is_simple(ll x)
{
	for (ll i = 2; i * i <= x; i++)
		if (x % i == 0)
			return i;
	return -1;
}

ll st(ll x, int st)
{
	ll cop = 1;
	for (int i = 0; i < st; i++)
		cop *= x;
	return cop;
}
ll t;

string s;

int main()
{
//	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);
	cin >> t;
	forn(i, t)
	{
		cout << "Case #1:" << "\n";
		int n, k;
		cin >> n >> k;
		n--;
		n--;
		string s;
		for (int i = 0; i < n; i++)
			s += '0';
		int ans = 100000;
		bool f = true;
		int kol = 0;
		while (f)
		{
			f = false;
			for (int i = 0; i < n; i++)
			{
				if (s[i] == '0')
				{
					s[i] = '1';
					f = true;
					break;
				}
				else
					s[i] = '0';
			}
			string sl = "1";
			forn(i, s.size())
				sl += s[i];
			sl += '1';
			ll sum = 0;
			bool fl = true;
			vector<ll> ss;
			for (ll kek = 2; kek <= 10; kek++)
			{
				ll qq = 0;
				forn(t, sl.size())
				{
					if (sl[t] == '1')
						qq += st(kek, sl.size() - t - 1);

				}
				ll r = is_simple(qq);
				if (r != -1)
					ss.pk(r);
				else
				{
					ss.clear();
					fl = false;
					break;
				}
			}
			if (fl)
			{
				cout << sl << ' ';
				forn(t, ss.size())
					cout << ss[t] << ' ';
				cout << "\n";
				kol++;
				if (kol == k)
					break;
			}
		}
	}

}
