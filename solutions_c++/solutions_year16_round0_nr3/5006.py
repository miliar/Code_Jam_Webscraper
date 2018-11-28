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

int n, jj;

inline bool read()
{
	cin >> n >> n >> jj;
	return true;
}

int get(string s, int st)
{
	li cur = 1ll;
	li a = 0;
	for(int i = 0; i < sz(s); i++)
	{
		if(s[i] == '1')
			a += cur;
		cur *= (li)st;
	}
	for(int i = 2; i * 1ll * i <= a; i++)
		if(a % i == 0)
			return i;
	return -1;
}

inline void solve()
{
	vector<pair<string, vector<int> > > ans;
	for(int i = (1 << n) - 1; i >= 0 && sz(ans) < 50; i--)
	{
		string cur = "";
		for(int j = 0; j < n; j++)
			if(i & (1 << j))
				cur += '1';
			else
				cur += '0';
		if(cur[0] != '1' || cur[sz(cur) - 1] != '1')
			continue;
		vector<int>now;
		bool ok = true;
		for(int j = 2; j <= 10; j++)
		{
			int num = get(cur, j);
			if(num == -1)
			{
				ok = false;
				break;
			}
			now.pb(num);
		}
		if(ok)
			ans.pb(mp(cur, now));
	}
	cout << "Case #1:" << endl;
	assert(sz(ans) >= jj);
	for(int i = 0; i < jj; i++)
	{
		reverse(all(ans[i].ft));
		cout << ans[i].ft;
		for(int j = 0; j < sz(ans[i].sc); j++)
		{
			cout << ' ' << ans[i].sc[j];
		}
		cout << endl;
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
	
	assert(read());
	solve();
	
#ifdef SU2_PROJ
	cerr << "=== TIME: " << clock() << " ===" << endl;
#endif

	return 0;
}
