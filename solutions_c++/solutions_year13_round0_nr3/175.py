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
#define eprintf(...) fprintf(stderr, __VA_ARGS__)

using namespace std;

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9, PI = 3.1415926535897932384626433832795;

typedef vector<int> bint;

char s[200];
bint a, b;

inline bool read()
{
	assert(scanf("%s", s) == 1);
	a.resize(int(strlen(s)));
	forn(i, sz(a)) a[i] = s[i] - '0';
	assert(scanf("%s", s) == 1);
	b.resize(int(strlen(s)));
	forn(i, sz(b)) b[i] = s[i] - '0';
	return true;
}

inline bint operator* (const bint& a, const bint& b)
{
	bint ans(sz(a) + sz(b) + 1, 0);
	
	forn(i, sz(a))
		forn(j, sz(b))
			ans[i + j] += a[i] * b[j];
			
	int carry = 0;
	
	forn(i, sz(ans))
	{
		int val = ans[i] + carry;
		ans[i] = val % 10;
		carry = val / 10;
	}
	
	assert(carry == 0);
	
	while (sz(ans) > 1 && ans.back() == 0) ans.pop_back();
	
	return ans;
}

inline ostream& operator<< (ostream& out, const bint& x)
{
	forn(i, sz(x)) out << x[i];
	return out;
}

vector<bint> z;

inline void add(bint x)
{
	bint xx = x * x;
	
	forn(i, sz(xx) >> 1)
		if (xx[i] != xx[sz(xx) - 1 - i])
			return;
			
	z.pb(xx);
}

vector<int> msk;

inline void add(bint x, int d)
{
	x[0] = x.back() = d;
	int len = sz(x) >> 1;
	
	forn(p, sz(msk))
	{
		int mask = msk[p];
		if (mask >= (1 << (len - 1))) continue;
		
		int cnt = 0;
		
		forn(i, len - 1)
		{
			x[i + 1] = x[sz(x) - 1 - (i + 1)] = (mask & (1 << i)) ? d : 0;
			if (mask & (1 << i)) cnt++;
		}
		
		if (cnt > 4) continue;
		
		add(x);
	}
}

inline bool cmp(const bint& a, const bint& b)
{
	if (sz(a) != sz(b)) return sz(a) < sz(b);
	return a < b;
}

inline void prepare()
{
	forl(i, 3) z.pb(bint(1, i * i));
	
	const int L = 26;
	
	forn(mask, (1 << L))
	{
		int cnt = 0;
		
		forn(i, L)
			if (mask & (1 << i))
				cnt++;
				
		if (cnt <= 4) msk.pb(mask);
	}
	
	forl(len, L)
	{
		{
    		bint x(2 * len, -1);
    		
    		add(x, 1);
    		
    		{
    			x = vector<int> (sz(x), 0);
    			x[0] = x.back() = 2;
    			add(x);
    		}
		}
		
		{
    		bint x(2 * len + 1, -1);
    		
    		forn(i, 3)
    		{
    			x[len] = i;
    			
    			add(x, 1);
    			
    			{
    				x = vector<int> (sz(x), 0);
    				x[0] = x.back() = 2;
    				x[len] = i;
    				add(x);
    			}
    		}
		}
	}
	
	sort(all(z), cmp);
	
	//forn(i, sz(z)) cerr << z[i] << endl;
}

inline void solve(int test)
{
	printf("Case #%d: ", test + 1);
	
	int l = int(lower_bound(all(z), a, cmp) - z.begin());
	int r = int(upper_bound(all(z), b, cmp) - z.begin());
	
	printf("%d\n", r - l);
}

int main()
{
#ifdef SU2_PROJ
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif
    
    cout << setprecision(10) << fixed;
    cerr << setprecision(5) << fixed;
    
    prepare();
    
    int testCount;
    cin >> testCount;
    
    forn(test, testCount)
    {
        assert(read());
        solve(test);
    }
    
    cerr << clock() / ld(CLOCKS_PER_SEC) << endl;
    
    return 0;
}
