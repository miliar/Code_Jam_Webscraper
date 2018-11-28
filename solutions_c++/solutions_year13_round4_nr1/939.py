#include <tuple>
#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
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
#include <utility>
#include <vector>
 
using namespace std ;

#define all(n) n.begin(), n.end()
#define fore(i, n) forn (i, n.size())
#define fori(i, n) for (typeof (n.begin()) i = n.begin() ; i != n.end() ; i++)
#define forn(i, n) forsn (i, 0, n)
#define forsn(i, s, n) for (int i = s ; i < n ; i++)
#define LOG cerr << "[" << __LINE__ << "] "
#define pb push_back

typedef long long tint ;
const tint md = 1000002013ll ;
const tint big = 100000000000000ll ;

typedef pair <int, int> pii ;
#define y first
#define x second

tint F(tint n) { return ((n * n + n - 2) / 2) % md ; }

tint solve()
{
	tint y = 0 ;
	int n, m ; cin >> n >> m ;

	vector <tuple <int, int, int>> q(m) ;
	map <tint, tint> g ;
	forn(i, m)
	{
		int o, e, p ; cin >> o >> e >> p ;
		q[i] = make_tuple(o, e, p) ;

		g[o] = 0 ;
		g[e] = 0 ;

		y = (y + F(e - o + 1) * p) % md ;
	}

	fore(i, q)
	{
		for (auto it = g.lower_bound(get<0>(q[i])) ; it->y < get<1>(q[i]) ; it++)
			it->x = (it->x + get<2>(q[i])) % md ;
	}

	bool f = true ;
	tint r = 0 ;
	while (f)
	{
		f = false ;

		map <tint, tint>::iterator d = g.end() ;
		tint a = big ;
		fori(i, g)
		{
			if (d != g.end())
			{
				if (i->x == 0)
				{
					//r = ((r - F(i->x - d->y + 1) * a) % md + md) % md ;
					//r -= F(i->y - d->y + 1) * a ;
					r = (r + F(i->y - d->y + 1) * a) % md ;

					//LOG << a << " del " << d->y << " al " << i->y << endl ;

					for (map <tint, tint>::iterator it = d ; it != i ; it++)
						it->x -= a ;

					f = true ;
				}

				a = min(a, i->x) ;
			}
			else if (i->x > 0)
			{
				d = i ;
				a = i->x ;
			}
		}
	}

	return ((r - y) % md + md) % md ;
}

int main()
{
	int t ; cin >> t ;
	forn(z, t) printf("Case #%d: %d\n", z + 1, solve()) ;

	return 0 ;
}

