#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
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
 
using namespace std ;
 
#define forsn(i, s, n) for (int i = s ; i < n ; i++)
#define forn(i, n) forsn(i, 0, n)
#define fore(i, n) forn(i, n.size())
#define fori(i, n) for (auto i = n.begin() ; i != n.end() ; i++)
#define all(n) n.begin(), n.end()
#define pb push_back

typedef pair <int, int> pii ;
#define y first
#define x second

typedef vector <string> vs ;

const int mod = 1000000007 ;

int cpr(const string &a, const string &b)
{
	int s = min(a.size(), b.size()) ;
	forn(i, s) if (a[i] != b[i]) return i ;
	return s ;
}

int test(const vector <int> &f, const vector <string> &s, int n)
{
	int r = 0 ;

	vector <vs> g(n) ;
	fore(i, f) g[f[i]].pb(s[i]) ;

	fore(i, g) if (g[i].empty()) return -1 ;

	fore(i, g)
	{
		fore(u, g[i])
		{
			r += g[i][u].size() ;
			if (u > 0) r -= cpr(g[i][u], g[i][u - 1]) ;
		}
	}

	return r + n ;
}

pii go(const vector <string> &s, int n)
{
	vector <int> f(s.size(), 0) ;

	int r = 0 ;
	int p = 0 ;
	while (f.back() < n)
	{
		int q = test(f, s, n) ;
		if (q == r) p = (p + 1) % mod ;
		else if (q > r)
		{
			r = q ;
			p = 1 ;
		}

		f[0]++ ;
		for (int i = 0 ; i < f.size() - 1 && f[i] == n ; i++)
		{
			f[i] = 0 ;
			f[i + 1]++ ;
		}
	}

	return pii(r, p) ;
}

int main()
{
	int t ; cin >> t ;
	forn(z, t)
	{
		int m, n ; cin >> m >> n ;
		
		vector <string> s(m) ;
		fore(i, s) cin >> s[i] ;
		sort(all(s)) ;

		pii r = go(s, n) ;
		printf("Case #%d: %d %d\n", z + 1, r.y, r.x) ;
	}

	return 0 ;
}

