#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <iterator>
#include <list>
#include <set>
#include <queue>
#include <numeric>
#include <cstdlib>
#include <ctime>
#include <limits>

using namespace std;

typedef long long lli;
typedef long li;

template <class T>
T Maximize (T &v, T nv) { if (nv > v) v = nv; return v; }

template <class T>
T Minimize (T &v, T nv) { if (nv < v) v = nv; return v; }

const lli INFLL = numeric_limits<lli>::max();
const li INF = numeric_limits<li>::max(), LEN = 101;

string readString (vector <vector <li> > &v)
{
	string s;
	cin >> s;

	char last = s[0];
	for (li i = 1, j = 0; ; ++ i, ++ j)
	{
		li amount = 0;
		for (; i < s.length() && s[i] == last; ++ i, ++ amount);
		last = s[i];
		v[j].push_back(amount);
		if (i >= s.length()) break;
	}

	s.erase(unique(s.begin(), s.end()), s.end());
	return s;
}

void solve ()
{
	ios::sync_with_stdio(0);
	li tests;
	cin >> tests;

	for (li test = 1; test <= tests; ++ test)
	{
		li n;
		cin >> n;

		vector <vector <li> > a(LEN, vector <li>());

		string tmplt = readString(a);

		bool won = 0;
		for (li i = 1; i < n; ++ i)
		{
			string s = readString(a);

			if (s != tmplt)
			{
				won = 1;
				break;
			}
		}

		cout << "Case #" << test << ": ";
		if (won)
		{
			cout << "Fegla Won";
		}
		else
		{
			li res = 0;
			for (li i = 0, sz = tmplt.length(); i < sz; ++ i)
			{
				sort(a[i].begin(), a[i].end());
				li m = a[i][n / 2];
				for (li j = 0, sz = a[i].size(); j < sz; ++ j)
				{
					res += abs(a[i][j] - m);
				}
			}
			cout << res;
		}
		cout << '\n';
	}
}

void init ()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
}

int main()
{
	init();
	solve();
	return 0;
}
