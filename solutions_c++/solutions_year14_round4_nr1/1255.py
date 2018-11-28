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

int main()
{
	int t ; cin >> t ;
	forn(z, t)
	{
		int n, x ; cin >> n >> x ;
		vector <int> s(n) ;

		forn(i, n) cin >> s[i] ;
		sort(all(s)) ;

		int q = 0, w = s.size() - 1 ;
		int r = 0 ;
		while (q < w + 1)
		{
			if (s[q] + s[w] <= x) q++ ;
			w-- ;
			r++ ;
		}

		printf("Case #%d: %d\n", z + 1, r) ;
	}

	return 0 ;
}

