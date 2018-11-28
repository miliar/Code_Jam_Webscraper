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

const int N = 20 + 1;

int n;
int a[N], b[N];

inline bool read()
{
	if (scanf("%d", &n) != 1)
		return false;
		
	forn(i, n)
		assert(scanf("%d", &a[i]) == 1);
		
	forn(i, n)
		assert(scanf("%d", &b[i]) == 1);
		
	return true;
}

int used[N];
int d[N];
int cur[N];

int bb[N];

bool solve(int idx)
{ 
	if (idx == n)
	{
		ford(i, n)
		{
			bb[i] = 1;
			
			fore(j, i + 1, n - 1)
				if (cur[j] < cur[i])
					bb[i] = max(bb[i], bb[j] + 1);

			if (bb[i] != b[i]) return false;
		}
	
		return true;
	}
	
	forn(i, n)
	{
		if (used[i]) continue;
		
		d[idx] = 1;
		forn(j, idx)
			if (cur[j] < i)
				d[idx] = max(d[idx], d[j] + 1);
				
		if (d[idx] != a[idx]) continue;
		
		int cnt = 1;
		forn(j, i) if (!used[j]) cnt++;
		
		if (b[idx] > cnt) continue;
		
		cur[idx] = i;
		used[i] = true;
		
		if (solve(idx + 1)) return true;
		
		used[i] = false;
		d[idx] = 0;
	}
	
	return false;
}

inline void _solve(int test)
{
	memset(used, false, sizeof used);
	memset(d, 0, sizeof d);
	memset(cur, 0, sizeof cur);
	
	solve(0);
	
	printf("Case #%d:", test + 1);
	forn(i, n) printf(" %d", cur[i] + 1);
	puts("");
}

int main()
{
#ifdef SU2_PROJ
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
        
	cout << setprecision(10) << fixed;
	cerr << setprecision(5) << fixed;
	
	/*
	forn(test, 30)
	{
		n = 20;
		
		vector<int> perm(n);
		forn(i, n) perm[i] = i;
		random_shuffle(all(perm));
		
		forn(i, n)
		{
			a[i] = 1;
			
			forn(j, i)
				if (perm[j] < perm[i])
					a[i] = max(a[i], a[j] + 1);
		}
		
		ford(i, n)
		{
			b[i] = 1;
			fore(j, i + 1, n - 1)
				if (perm[j] < perm[i])
					b[i] = max(b[i], b[j] + 1);					
		}
		
		_solve(test);
	}
	
	return 0;
	*/
        
	int testCount;
	cin >> testCount;	
	
	forn(test, testCount)
	{        
		assert(read());
		_solve(test);
		
		cerr << test + 1 << endl;
	}
        
	return 0;
}