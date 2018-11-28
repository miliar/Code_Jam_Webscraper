#undef NDEBUG
#ifdef SU2_PROJ
#define _GLIBCXX_DEBUG
#endif

#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define forl(i, n) for (int i = 1; i <= int(n); i++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define fore(i, l, r) for (int i = int(l); i <= int(r); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(x, y) make_pair((x), (y))
#define ft first
#define sc second
#define x first
#define y second

using namespace std;

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }
inline ostream& operator<< (ostream& out, const pt& p) { return out << '(' << p.x << ", " << p.y << ')'; }

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9, PI = 3.1415926535897932384626433832795;

string s;
map<string, int> was;

inline bool read()
{
	cin >> s;
	return true;
}

void printans(int test, int ans)
{
	printf("Case #%d: %d\n", test, ans);
}

inline void solve(int tt)
{
	queue<string>q;
	was.clear();
	q.push(s);
	was[s] = 0;
	while(!q.empty())
	{
		string v = q.front();
		q.pop();
		bool fl = 1;
		for(int i = 0; i < sz(v); i++)
			if(v[i] == '-')
			{
				fl = 0;
				break;
			}
		if(fl)
		{
			printans(tt, was[v]);
			return;
		}
		for(int i = 0; i < sz(v); i++)
		{
			string pref = v.substr(0, i + 1);
			reverse(all(pref));
			for(int j = 0; j < sz(pref); j++)
				if(pref[j] == '-')
					pref[j] = '+';
				else
					pref[j] = '-';
			string to = v;
			for(int j = 0; j < sz(pref); j++)
				to[j] = pref[j];
			if(was.count(to))
				continue;
			was[to] = was[v] + 1;
			q.push(to);
		}
	}
}

int main()
{
#ifdef SU2_PROJ
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	cout << setprecision(10) << fixed;
	cerr << setprecision(5) << fixed;
	
	int T;
	cin >> T;
	for(int t1 = 0; t1 < T; t1++)
	{		
		assert(read());
		solve(t1 + 1);
	}
	
#ifdef SU2_PROJ
	cerr << "=== TIME: " << clock() << " ===" << endl;
#endif

	return 0;
}
