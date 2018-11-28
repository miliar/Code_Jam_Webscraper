#pragma comment(linker, "/stack:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES

#include <algorithm>
#include <iostream>
#include <cassert>
#include <iomanip>
#include <climits>
#include <utility>
#include <cstring>
#include <complex>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <bitset>
#include <string>
#include <queue>
#include <cmath>
#include <ctime>
#include <set>
#include <map>

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define forl(i, n) for (int i = 1; i <= int(n); i++)
#define for1(i, n) for (int i = 1; i <= int(n); i++)
#define forn1(i, n) for (int i = 1; i <= int(n); i++)
#define fore(i, l, r) for (int i = int(l); i <= int(r); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define debug(x) cerr << #x << " = " << x << endl;
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(a, b) make_pair((a), (b))
#define X first
#define Y second
#define fs first
#define ft first
#define sc second

using namespace std;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;
typedef pair<ld, ld> ptd;
typedef unsigned char byte;
typedef vector<vector<int> > matrix;

const int INF = INT_MAX / 2;
const ld EPS = 1e-9;
const ld PI = 3.1415926535897932384626433832795;

const int N = 20 + 3;

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

int ans[N];
int used;
bool was;

int z[N];

inline bool checkB()
{
	ford(i, n)
	{
		z[i] = 1;
		
		fore(j, i + 1, n - 1)
			if (ans[i] > ans[j])
				z[i] = max(z[i], z[j] + 1);
				
		if (z[i] != b[i])
			return false;
	}
	
	return true;
}

inline bool checkA()
{
	forn(i, n)
	{
		z[i] = 1;
		
		fore(j, 0, i - 1)
			if (ans[i] > ans[j])
				z[i] = max(z[i], z[j] + 1);
				
		if (z[i] != a[i])
			return false;
	}
	
	return true;
}
inline void brute(int lf, int rg) 
{
	if (was)
		return;
		
	if (lf > rg)
	{
    	if (checkA() && checkB())
    	{
    		was = true;	
    		
    		forn(i, n)
    			printf("%d ", ans[i] + 1);
    			
    		puts("");
    		
    		return;
    	}
    	
    	return;
    }
    
    int val = (lf - 0) + (n - 1 - rg);
    	
    if (val % 2 == 0)
    {
    forn(i, n)
	{
		if ((used & (1 << i)) != 0)
			continue;
			
		int idx = lf;
		
		ans[idx] = i;
		
		int maxv = 1;
		
		fore(j, 0, idx - 1)
			if (ans[j] < ans[idx])
				maxv = max(maxv, a[j] + 1);
				
		if (maxv != a[idx])
			continue;
			
		used ^= (1 << i);
		
		brute(lf + 1, rg);
		
		used ^= (1 << i);
	}
    }
    else
    {
	ford(i, n)
	{
		if ((used & (1 << i)) != 0)
			continue;
			
		int idx = rg;
		
		ans[idx] = i;
		
		int maxv = 1;
		
		fore(j, idx + 1, n - 1)
			if (ans[j] < ans[idx])
				maxv = max(maxv, b[j] + 1);
				
		if (maxv != b[idx])
			continue;
			
		used ^= (1 << i);
		
		brute(lf, rg - 1);
		
		used ^= (1 << i);
	}
	}
}

int IT;

const int M1 = 55 * 1000 * 1000;

const int M2 = 140 * 1000 * 1000;

inline void brute2(int idx) 
{
	if (was)
		return;
		
	if (IT >= M2)
		return;
		
	IT++;
		
	if (idx == -1)
	{
    	if (checkA())
    	{
    		was = true;	
    		
    		forn(i, n)
    			printf("%d ", ans[i] + 1);
    			
    		puts("");
    		
    		return;
    	}
    	
    	return;
    }
    	
	ford(i, n)
	{
		if ((used & (1 << i)) != 0)
			continue;
			
		ans[idx] = i;
		
		int maxv = 1;
		
		fore(j, idx + 1, n - 1)
			if (ans[j] < ans[idx])
				maxv = max(maxv, b[j] + 1);
				
		if (maxv != b[idx])
			continue;
			
		used ^= (1 << i);
		
		brute2(idx - 1);
		
		used ^= (1 << i);
	}
}

inline void brute1(int idx) 
{
	if (was)
		return;
		
	if (IT >= M1)
		return;
		
	IT++;
		
	if (idx == n)
	{
    	if (checkB())
    	{
    		was = true;	
    		
    		forn(i, n)
    			printf("%d ", ans[i] + 1);
    			
    		puts("");
    		
    		return;
    	}
    	
    	return;
    }
    	
	forn(i, n)
	{
		if ((used & (1 << i)) != 0)
			continue;
			
		ans[idx] = i;
		
		int maxv = 1;
		
		fore(j, 0, idx - 1)
			if (ans[j] < ans[idx])
				maxv = max(maxv, a[j] + 1);
				
		if (maxv != a[idx])
			continue;
			
		used ^= (1 << i);
		
		brute1(idx + 1);
		
		used ^= (1 << i);
	}
}


inline void solve(int test)
{
	printf("Case #%d: ", test + 1);

	was = false;
	
	if (!was)
	{
		used = 0;
		IT = 0;
		
		brute1(0);
		
		cerr << ":1" << endl;	
	}	

	if (!was)
	{
		used = 0;
		IT = 0;
		
		brute2(n - 1);
		
		cerr << ":2" << endl;	
	}	

	if (!was)
	{
		used = 0;
		brute(0, n - 1);	
		
		cerr << ":3" << endl;
	}

	assert(was);
	
	cerr << test + 1 << endl;
}

int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int testCnt;

    assert(scanf("%d\n", &testCnt) == 1);

    forn(test, testCnt)
    {
    	assert(read());
		solve(test);
	}

    return 0;
}
