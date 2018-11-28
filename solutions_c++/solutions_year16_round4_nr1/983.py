#if 1
#include <functional>
#include <algorithm>
#include <iostream>
#include <iterator>
#include <iomanip>
#include <sstream>
#include <numeric>
#include <string>
#include <vector>
#include <bitset>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <list>

using namespace std;

typedef unsigned long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef pair<int, int> pii;

const LD eps = 1e-9;
const LD pi = acos(-1.0);
const LL inf = 1e+9;

#define mp make_pair
#define pb push_back
#define X first
#define Y second

#define dbg(x) { cerr << #x << " = " << x << endl; }

// extended template
#pragma comment(linker, "/STACK:36777216")
typedef vector<int> vi;
typedef vector<vi> vvi;

#define forn(i, n) for (int i = 0; i < n; ++i)
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()

template<typename T> istream & operator >> (istream &, vector<T> &);
template<typename T> ostream & operator << (ostream &, const vector<T> &);

#define START clock_t _clock = clock();
#define END cerr << endl << "time: " << (clock() - _clock) / LD(CLOCKS_PER_SEC) << endl;

#define NAME "basket"

string g;
string t = "PRS";
string rt = "RSP";

void gen(int l, int r, int win)
{
	if (l == r)
	{
		g[l] = t[win];
		return;
	}
	int tm = (l + r) / 2;

	if (t[win] < rt[win])
	{
		gen(l, tm, win);
		gen(tm + 1, r, (win + 1) % 3);
	}
	else
	{
		gen(l, tm, (win + 1) % 3);
		gen(tm + 1, r, win);
	}
}
int n;
void conv(string &s)
{
	for (int k = 1; k <= n; k++)
		for (int i = 0; i < s.size(); i += (1 << k))
		{
			string t1 = s.substr(i, 1 << (k - 1));
			string t2 = s.substr(i + (1 << (k - 1)), 1 << (k - 1));
			if (t2 < t1)
			{
				for (int j = i; j < i + (1 << (k)); j++)
				{
					if (j - i < t2.size())
						s[j] = t2[j - i];
					else
						s[j] = t1[j - i - (1 << (k - 1))];
				}
			}
		}
}

void solve()
{
	int T;
	scanf("%d", &T);
	for (int q = 0; q < T; q++)
	{
		cerr << q << endl;
		scanf("%d", &n);
		vector <int> v(3);
		for (int i = 0; i < 3; i++)
			scanf("%d", &v[i]);
		swap(v[0], v[1]);
		string ans = "Z";
		for (int i = 0; i < 3; i++)
		{
			g.resize(1 << n);
			gen(0, (1 << n) - 1, i);

			int P = count(all(g), 'P');
			int R = count(all(g), 'R');
			int S = count(all(g), 'S');
			conv(g);
			if (v[0] == P && v[1] == R && v[2] == S)
			{
				//conv(g);
				ans = min(ans, g);
			}
		}

		if (ans == "Z")
			ans = "IMPOSSIBLE";

		cout << "Case #" << q + 1 << ": " << ans << endl;
	}

}

int main()
{
	
	//START
	//freopen(NAME ".in", "r", stdin); freopen(NAME ".out", "w", stdout);
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	ios_base::sync_with_stdio(false);
	solve();
	//END
	return 0;
}
/*******************************************
*******************************************/

template<typename T> istream & operator >> (istream &is, vector<T> &v)
{
	forn(i, v.size())
		is >> v[i];
	return is;
}
template<typename T> ostream & operator << (ostream &os, const vector<T> &v)
{
	forn(i, v.size())
		os << v[i];
	return os;
}
#endif