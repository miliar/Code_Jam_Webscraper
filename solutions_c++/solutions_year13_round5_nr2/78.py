#undef NDEBUG
#ifdef SU2_PROJ
#define _GLIBCXX_DEBUG
#endif

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
typedef pair<int, int> pti;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9, PI = 3.1415926535897932384626433832795;

struct pt
{
    ld x, y;
    pt(ld x = -1, ld y = -1): x(x), y(y) { }
};

inline ostream& operator<< (ostream& out, const pt& p) { return out << "(" << p.x << ", " << p.y << ")"; }

inline pt operator- (const pt& a, const pt& b)
{
    return pt(a.x - b.x, a.y - b.y);
}

inline bool operator< (const pt& a, const pt& b)
{
    if (abs(a.y - b.y) > EPS)
        return a.y < b.y;
        
    return a.x < b.x;
}

inline bool operator!= (const pt& a, const pt& b)
{
	return abs(a.x - b.x) > EPS || abs(a.y - b.y) > EPS;
}

inline bool operator== (const pt& a, const pt& b)
{
	return abs(a.x - b.x) < EPS && abs(a.y - b.y) < EPS;
}

inline ld dist(const pt& a, const pt& b)
{
    return sqr(a.x - b.x) + sqr(a.y - b.y);
}

inline ld cross(const pt& a, const pt& b)
{
    return a.x * b.y - a.y * b.x;
}

pt pole;

inline bool cmp(const pt& a, const pt& b)
{
    ld v = cross(a - pole, b - pole);
    
    if (abs(v) > EPS)
        return v > 0;
        
    return dist(a, pole) + EPS < dist(b, pole);
}

inline ld det(const ld& a, const ld& b, const ld& c, const ld& d) { return a * d - b * c; }

const int N = 10 + 3;

int n;
pt a[N];

inline bool read()
{
    if (!(cin >> n)) return false;
    
    forn(i, n) assert(cin >> a[i].x >> a[i].y);
    
    return true;
}

inline ld sq(pt pol[N], int n)
{
	ld ans = 0;
	pol[n] = pol[0];
	forn(i, n) ans += (pol[i].x - pol[i + 1].x) * (pol[i].y + pol[i + 1].y);
	return abs(ans) / 2;
}

int sz = 0;
pt ans[N];

inline ld convexHull(pt a[N], int n)
{
    sort(a, a + n);
    pole = a[0];
    sort(a + 1, a + n, cmp);
    
    sz = 0;
    forn(i, n)
    {
        while (sz > 1 && cross(ans[sz - 1] - ans[sz - 2], a[i] - ans[sz - 1]) <= 0)
            sz--;
            
        ans[sz++] = a[i];
    }
    
    return sq(ans, sz);
}

inline ld onsegment(const pt& a, const pt& b, const pt& p)
{
	ld A = b.y - a.y, B = a.x - b.x, C = -(A * a.x + B * a.y);
	ld v = A * p.x + B * p.y + C;
	if (abs(v) > EPS) return false;
	return min(a.x, b.x) < p.x + EPS && p.x < max(a.x, b.x) + EPS &&
			min(a.y, b.y) < p.y + EPS && p.y < max(a.y, b.y) + EPS;
}

int szgp;
pt gp[3];

inline bool good(const pt& p)
{
	forn(i, szgp) if (gp[i] == p) return true;
	return false;
}

inline bool intersect(const pt& a, const pt& b, const pt& c, const pt& d, pt& ans)
{
	if (onsegment(a, b, c) && !good(c)) { ans = c; return true; }
	if (onsegment(a, b, d) && !good(d)) { ans = d; return true; }
	if (onsegment(c, d, a) && !good(a)) { ans = a; return true; }
	if (onsegment(c, d, b) && !good(b)) { ans = b; return true; }
	
	ld A1 = b.y - a.y, B1 = a.x - b.x, C1 = -(A1 * a.x + B1 * a.y);
	ld A2 = d.y - c.y, B2 = c.x - d.x, C2 = -(A2 * c.x + B2 * c.y);
	
	ld dd = det(A1, B1, A2, B2);
	
	if (abs(dd) < EPS) return false;
	
	pt curp(det(-C1, B1, -C2, B2) / dd, det(A1, -C1, A2, -C2) / dd);
	if (onsegment(a, b, curp) && onsegment(c, d, curp) && !good(curp)) { ans = curp; return true; }
	return false;
}

ld S;
int used[N];
int num[N];

bool solve(int cnt)
{
	//cerr << cnt << endl;
	if (cnt == n)
	{
		{
			forn(j, n - 1)
			{
				szgp = 0;
				if (j == 0) gp[szgp++] = a[num[0]];
				if (j == n - 2) gp[szgp++] = a[num[j + 1]];
				
				pt p;
				if (intersect(a[num[j]], a[num[j + 1]], a[num[n - 1]], a[num[0]], p))
					return false;
			}
		}
		
		forn(i, n) ans[i] = a[num[i]];
		if (sq(ans, n) * 2 - EPS > S)
		return true;
	}
	
	forn(i, n)
		if (!used[i])
		{
			num[cnt] = i;
			//if (cnt == 1 && i != 1) continue;
			//if (cnt == 2 && i != 2) continue;
			//if (cnt == 3 && i != 3) continue;
			
			forn(j, cnt - 1)
			{
				szgp = 0;
				if (j == cnt - 2) gp[szgp++] = a[num[j + 1]];
				
				pt p;
				if (intersect(a[num[j]], a[num[j + 1]], a[num[cnt - 1]], a[num[cnt]], p))
				{
					//cerr << a[num[j]] << ' ' << a[num[j + 1]] << endl;
					//cerr << a[num[cnt - 1]] << ' ' << a[num[cnt]] << endl;
					goto bad;
				}
			}
			
			used[i] = true;
			if (solve(cnt + 1)) return true;
			used[i] = false;
			bad:;
		}
		
	return false;
}

pt aa[N];

inline void _solve(int test)
{
	printf("Case #%d:", test + 1);
	
	forn(i, n) aa[i] = a[i];
	S = convexHull(aa, n);
	
	memset(used, 0, sizeof(used));
	
	num[0] = 0;
	used[0] = true;
	assert(solve(1));
	
	forn(i, n) printf(" %d", num[i]);
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
