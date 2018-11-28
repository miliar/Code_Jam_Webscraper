#include <iostream>
#include <ctime>
#include <string>
#include <vector>
#include <set>
#include <cassert>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <iomanip>
#include <cstdlib>
#include <cstring>
#include <memory>
#include <deque>
#include <stack>
#include <queue>
#include <map>
#include <list>
#include <complex>
#include <hash_map>
#include <hash_set>

#pragma comment (linker, "/STACK:1000000000")

using namespace std;

#define pb push_back
#define pob pop_back
#define rs resize
#define as assign
#define lwb lower_bound
#define upb upper_bound
#define mp make_pair

typedef long long ll;
typedef vector <int> vi;
typedef vector <vi> vvi;
typedef vector <ll> vl;
typedef vector <vl> vvl;
typedef vector <bool> vb;
typedef vector <vb> vvb;
typedef vector <string> vs;
typedef vector <char> vc;
typedef vector <vc> vvc;
typedef vector <vvi> vvvi;
typedef vector <vvvi> vvvvi;
typedef vector <vvl> vvvl;
typedef vector <vvvl> vvvvl;
typedef vector <vvb> vvvb;
typedef double db;
typedef long double ldb;
typedef vector <db> vdb;
typedef vector <ldb> vldb;
typedef pair <int, int> ii;
typedef pair <int, char> ic;
typedef pair <ll, ll> lll;
typedef pair <int, ll> il;
typedef pair <ll, int> li;
typedef vector <ii> vii;
typedef vector <ic> vic;
typedef vector <vic> vvic;
typedef vector <vii> vvii;
typedef vector <lll> vll;
typedef vector <vll> vvll;
typedef set <int> si;
typedef set <ii> sii;
typedef set <pair <int, bool> > sib;
typedef vector <si> vsi;
typedef map <int, int> mii;
typedef map <string, char> msc;
typedef map <char, int> mci;
typedef queue <int> qi;
typedef deque <int> di;
typedef stack <int> sti;

const ll inf = (ll)1e9 + 7;

int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int x = 0; x < t; ++x)
	{
		int n;
		cin >> n;
		vs a(n);
		for (int i = 0; i < n; ++i)
			cin >> a[i];
		vvic q(n);
		ll ans = inf;
		bool f = 0;
		for (int i = 0; i < n; ++i)
		{
			int s = 1;
			for (int j = 1; j < a[i].size(); ++j)
			{
				if (a[i][j] != a[i][j - 1])
				{
					q[i].pb(mp(s, a[i][j - 1]));
					s = 0;
				}
				s++;
			}
			q[i].pb(mp(s, a[i][a[i].size() - 1]));
		}
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < n; ++j)
			{
				if (q[i].size() != q[j].size())
				{
					f = 1;
					break;
				}
				for (int k = 0; k < q[i].size(); ++k)
					if (q[i][k].second != q[j][k].second)
					{
						f = 1;
						break;
					}
				if (f)
					break;
			}
			if (f)
				break;
		}
		if (f)
		{
			cout << "Case #" << x + 1 << ": Fegla Won" << endl;
			continue;
		}
		vi d(q[0].size(), 100000);
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < q[i].size(); ++j)
				d[j] = min(d[j], q[i][j].first);
		ll p = 0;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < q[i].size(); ++j)
				p += ll(q[i][j].first - d[j]);
		ans = min(ans, p);
		for (int i = 0; i < n; ++i)
		{
			p = 0;
			for (int j = 0; j < n; ++j)
				for (int k = 0; k < q[j].size(); ++k)
					p += abs(q[i][k].first - q[j][k].first);
			ans = min(ans, p);
		}
		cout << "Case #" << x + 1 <<": " << ans << endl;
	}
//	system("pause");
	return 0;
}