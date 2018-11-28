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
 
typedef long long LL;
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

#include <unordered_map>
unordered_map<string, int> sp;

int conv(const string &s)
{
	if (sp.count(s))
		return sp[s];
	int sz = sp.size();
	sp[s] = sz;
	return sz;
}

void solve()
{
	int T;
	cin >> T;
	for (int q = 0; q < T; q++)
	{
		cerr << q << endl;
		sp.clear();
		int n;
		cin >> n;
		string s;
		vector <vector <int> > a(n);
		int j = 0;
		vector <pair<int, int> > res1(5000);
		getline(cin, s);
		for (int j = 0; j < n; j++)
		{
			getline(cin, s);
			stringstream O(s);
			string t;
			while (O >> t)
			{
				a[j].pb(conv(t));
				if (j == 0)
					res1[conv(t)].X = 1;
				if (j == 1)
					res1[conv(t)].Y = 1;
			}
		}

		a.erase(a.begin());
		a.erase(a.begin());
		n = a.size();
		
		int ans = inf;
		for (int mask = 0; mask < (1 << n); mask++)
		{	
			vector <pair<int, int> >  res = res1;
			for (int i = 0; i < n; i++)
			{
				int v =((mask & (1 << i)) > 0);
				for (int j = 0; j < a[i].size(); j++)
				{
					int &cur = v == 0 ? res[a[i][j]].X : res[a[i][j]].Y;
					cur = 1;
				}
			}
			int cnt = 0;
			for (int i = 0; i < res.size(); i++)
			{
				cnt += (res[i].X && res[i].Y);
			}

			ans = min(ans, cnt);
		}
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
        os << v[i] << " ";
    return os;
}
#endif