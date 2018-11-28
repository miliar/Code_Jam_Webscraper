#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#define bublic public
#define clr(x) memset((x), 0, sizeof(x))
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define sz size()
#define For(i, st, en) for(int i=(st); i<=(int)(en); i++)
#define Ford(i, st, en) for(int i=(st); i>=(int)(en); i--)
#define forn(i, n) for(int i=0; i<(int)(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)
#define fori(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); it++)

template <class _T> inline _T sqr(const _T& x) { return x * x; }
template <class _T> inline string tostr(const _T& a) { ostringstream os(""); os << a; return os.str(); }

typedef long double ld;

// Constants
const ld PI = 3.1415926535897932384626433832795;
#define EPS 0

// Types
typedef signed   long long i64;
typedef unsigned long long u64;
typedef set < int > SI;
typedef vector < int > VI;
typedef map < string, int > MSI;
typedef pair < int, int > PII;

struct tp{int x,y;};

int qq;
int n;
tp a[12];
tp b[12];
bool u[12];
int p[12];
int s;
tp p0;

ld vp(tp p, tp p1, tp p2)
{
	p1.x -= p.x;
	p1.y -= p.y;
	p2.x -= p.x;
	p2.y -= p.y;
	return p1.x * p2.y - p1.y * p2.x;
}

ld sp(tp p, tp p1, tp p2)
{
	p1.x -= p.x;
	p1.y -= p.y;
	p2.x -= p.x;
	p2.y -= p.y;
	return p1.x * p2.x + p1.y * p2.y;
}

bool segseg(tp p1, tp p2, tp p3, tp p4)
{
	if (max(min(p1.x, p2.x), min(p3.x, p4.x)) > min(max(p1.x, p2.x), max(p3.x, p4.x)) + EPS) return false;
	if (max(min(p1.y, p2.y), min(p3.y, p4.y)) > min(max(p1.y, p2.y), max(p3.y, p4.y)) + EPS) return false;
	ld d1 = vp(p1, p2, p3);
	ld d2 = vp(p1, p2, p4);
	if ((d1 < 0 - EPS && d2 < 0 - EPS) || (d1 > 0 + EPS && d2 > 0 + EPS)) return false;
	d1 = vp(p3, p4, p1);
	d2 = vp(p3, p4, p2);
	if ((d1 < 0 - EPS && d2 < 0 - EPS) || (d1 > 0 + EPS && d2 > 0 + EPS)) return false;
	return true;
}

bool onseg(tp p, tp p1, tp p2)
{
	if (vp(p, p1, p2)) return false;
	return sp(p1, p2, p) >= 0 && sp(p2, p1, p) >= 0;
}

bool rec(int k, int ss)
{
	if (k == n)
	{
		ss += vp(p0, a[p[k - 1]], a[0]);
		if (ss < 0) ss = -ss;
		if (ss * 2 <= s) return false;

		bool ok = true;
		p[k] = 0;
		forn(j, k - 1)
		{
			if (!j) continue;
			if (onseg(a[p[j]], a[p[k - 1]], a[p[k]]))
			{
				ok = false;
				break;
			}
		}
		forn(j, k - 2)
		{
			if (!j) continue;
			if (segseg(a[p[j]], a[p[j + 1]], a[p[k - 1]], a[p[k]]))
			{
				ok = false;
				break;
			}
		}

		return ok;
	}
	forn(i, n)
	{
		if (!u[i])
		{
			bool ok = true;
			p[k] = i;
			forn(j, k - 1)
			{
				if (onseg(a[p[j]], a[p[k - 1]], a[p[k]]))
				{
					ok = false;
					break;
				}
			}
			forn(j, k - 2)
			{
				if (segseg(a[p[j]], a[p[j + 1]], a[p[k - 1]], a[p[k]]))
				{
					ok = false;
					break;
				}
			}
			if (ok)
			{
				u[i] = true;
				if (rec(k + 1, ss + vp(p0, a[p[k - 1]], a[p[k]]))) return true;
				u[i] = false;
			}
		}
	}
	return false;
}

bool operator < (tp p1, tp p2)
{
	return p1.y < p2.y || (p1.y == p2.y && p1.x < p2.x);
}

int conv()
{
	int k = 0;
	tp c[12];
	tp l[12];
	tp r[12];
	int ll = 0, rr = 0;
	forn(i, n)
	{
		c[i] = a[i];
	}
	sort(c, c + n);
	forn(i, n)
	{
		while (ll > 1 && vp(l[ll - 2], l[ll - 1], c[i]) >= 0) ll--;
		l[ll++] = c[i];
		while (rr > 1 && vp(r[rr - 2], r[rr - 1], c[i]) <= 0) rr--;
		r[rr++] = c[i];
	}
	forn(i, rr)
	{
		b[k++] = r[i];
	}
	Ford(i, ll - 2, 1)
	{
		b[k++] = l[i];
	}
	return k;
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	scanf("%d", &qq);
	forn(ii, qq)
	{
		printf("Case #%d:", ii+1);
		fprintf(stderr, "Case #%d:\n", ii+1);
		
		p0.x = p0.y = 0;
		scanf("%d", &n);
		forn(i, n)
		{
			scanf("%d%d", &a[i].x, &a[i].y);
		}
		a[n] = a[0];
		int k = conv();
		b[k] = b[0];
		s = 0;
		forn(i, k)
		{
			s += vp(p0, b[i], b[i + 1]);
		}
		if (s < 0) s = -s;
		clr(u);
		p[0] = 0;
		u[0] = true;
		cerr << rec(1, 0) << endl;

		forn(i, n)
		{
			printf(" %d", p[i]);
		}
		puts("");
		
		fflush(stdout);
	}

	return 0;
}
