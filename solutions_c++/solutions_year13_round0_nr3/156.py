#include <iostream>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <climits>
#include <cstring>
#include <ctime>
#include <cmath>
#include <cassert>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <utility>
#include <numeric>
#include <functional>

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

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9, PI = 3.1415926535897932384626433832795;

vector <string> v[2], ans;

inline bool paly (const string& s)
{
	int fin = (sz(s) >> 1);
	forn(i, fin) if (s[i] != s[sz(s) - 1 - i]) return false;
	return true;
}

const int base = 1000;

inline string toStr (li a, int len)
{
	string ans = "";
	while (a) ans.pb(a % 10 + '0'), a /= 10;
	while (sz(ans) < len) ans.pb('0');
	reverse(all(ans));
	return ans;
}

inline string operator * (const string& s1, const string& s2)
{
	vector <int> a;
	for (int i = sz(s1) - 1; i >= 0; )
	{
		int t = 0, deg = 1;
		forn(it, 3)
		{
			t += (s1[i] - '0') * deg;
			deg *= 10;
			if (--i < 0) break;
		}
		a.pb(t);
	}
	
	//forn(i, sz(a)) cerr << a[i] << endl;
	//cerr << endl;
	
	vector <li> c(2 * sz(a), 0);
	
	forn(i, sz(a))
		forn(j, sz(a))
			c[i + j] += a[i] * a[j];
			
	//forn(i, sz(c)) cerr << c[i] << endl;
	//cerr << endl;
			
	li carry = 0;
	
	forn(i, sz(c))
	{
		c[i] += carry;
		carry = c[i] / base;
		c[i] %= base;
	}
	
	while (carry)
	{
		c.pb(carry % base);
		carry /= base;
	}
	
	while (sz(c) > 1 && c.back() == 0) c.pop_back();
	
	string ans = toStr(c.back(), 1);
	ford(i, sz(c) - 1)
		ans += toStr(c[i], 3);
		
	return ans;	
}

inline void prepare()
{
	ans.pb("1");
	ans.pb("4");
	ans.pb("9");
	v[0].pb("11");
	v[0].pb("22");
	v[1].pb("101");
	v[1].pb("111");
	v[1].pb("121");
	v[1].pb("202");
	v[1].pb("212");
	
	int iter = 0;
	
	while (sz(ans.back()) < 100)
	{
		vector <string> oldv = v[iter];
		
		forn(i, sz(oldv)) ans.pb(oldv[i] * oldv[i]);
		
		set <string> nv;
		set <string> used;
		
		forn(i, sz(oldv))
			forn(dig, 3)
				forl(pos, sz(oldv[i]) / 2)
				{
					string cur = oldv[i];
					cur.insert(pos, string(1, '0' + dig));
					cur.insert(sz(cur) - pos, string(1, '0' + dig));
					
					//cerr << oldv[i] << ' ' << cur << ' ' << pos << endl;
						
					if (used.count(cur)) continue;
					used.insert(cur);
					if (paly(cur * cur)) nv.insert(cur);
				}
				
		v[iter] = vector <string> (all(nv));
		iter ^= 1;
	}
}

string a, b;

inline bool read()
{
	return cin >> a >> b;
}

inline bool cmp (const string& a, const string& b)
{
	if (sz(a) != sz(b)) return sz(a) < sz(b);
	return a < b;
}

inline void solve(int test)
{
	int lf = int(lower_bound(all(ans), a, cmp) - ans.begin());
	int rg = int(lower_bound(all(ans), b, cmp) - ans.begin());
	if (rg >= sz(ans) || ans[rg] != b) rg--;
	printf("Case #%d: %d\n", test + 1, rg - lf + 1);
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	cout << setprecision(10) << fixed;
	cerr << setprecision(5) << fixed;
	
	prepare();
	//forn(i, sz(ans)) cerr << ans[i] << endl;
	
	int testCount;
	cin >> testCount;
	
	forn(test, testCount)
	{
		assert(read());
		solve(test);
	}
	
	return 0;
}
