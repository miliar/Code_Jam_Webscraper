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

ll t;

string s;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	forn(i, t)
	{
		cin >> s;
		int j = 0;
		int ans = 0;
		while (s[j] == '-')
		{
			s[j] = '+';
			j++;
		}
		if (j != 0)
			ans++;
		j = s.size() - 1;
		while (s[j] == '+')
		{
			j--;
			if (j == -1)
				break;
		}
		string sl = "";
		for (int q = 0; q <= j; q++)
			sl += s[q];
		if (sl.size() == 0)
		{
			cout << "Case #" << i + 1 << ": " << ans << "\n";
			continue;
		}
		for (int q = 1; q < sl.size(); q++)
			if (sl[q] == '-' && sl[q - 1] == '+')
				ans += 2;
		cout << "Case #" << i + 1 << ": " << ans << "\n";
	
	}

}
