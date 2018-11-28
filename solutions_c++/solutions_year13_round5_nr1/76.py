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
const ld EPS = 1e-11;

// Types
typedef signed   long long i64;
typedef unsigned long long u64;
typedef set < int > SI;
typedef vector < int > VI;
typedef map < string, int > MSI;
typedef pair < int, int > PII;

int qq, n;
i64 a[1024];
i64 x;
int cnt;

ld calc(i64 z)
{
	i64 need = 0;
	forn(k, cnt)
	{
		need += z - a[k];
	}
	if (need > x) return -1e18;
	For(k, cnt, n - 1)
	{
		if (a[k] < z + 1)
		{
			need += z + 1 - a[k];
		}
	}
	if (need > x) return -1e18;
	ld w = -need;
	forn(k, cnt)
	{
		w += 1.0 / cnt * 36 * (z - a[k]);
	}
	return w;
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	scanf("%d", &qq);
	forn(ii, qq)
	{
		printf("Case #%d: ", ii+1);
		fprintf(stderr, "Case #%d:\n", ii+1);
		
		scanf("%I64d%d", &x, &n);
		forn(i, n)
		{
			scanf("%I64d", &a[i]);
		}
		while (n < 37)
		{
			a[n++] = 0;
		}
		sort(a, a + n);
		ld ans = 0.0;

		forn(i, n)
		{
			i64 mi1 = a[i];
			cnt = i + 1;
			i64 need = 0;
			forn(k, cnt)
			{
				need += mi1 - a[k];
			}
			if (need > x) continue;
			i64 z = mi1;
			i64 zmi = z, zma = z - 1;
//			i64 zb = -1;
//			ld tmp = -1e18;
			i64 mi = z - 1;
			i64 ma = 1e15;
			while (mi < ma)
			{
				i64 q = (mi + ma + 1) / 2;
				i64 need = 0;
				forn(k, cnt)
				{
					need += q - a[k];
				}
				For(k, cnt, n - 1)
				{
					if (a[k] < q + 1)
					{
						need += q + 1 - a[k];
					}
				}
				if (need > x) ma = q - 1;
				else mi = q;
			}
			zma = mi;
			ans = max(ans, calc(zmi));
			ans = max(ans, calc(zma));
			while (zma - zmi > 3)
			{
				i64 q1 = (zmi + zma) / 2;
				i64 q2 = q1 + 1;
				ld w1 = calc(q1);
				ld w2 = calc(q2);
				ans = max(ans, w1);
				ans = max(ans, w2);
				if (w1 < w2) zmi = q1;
				else zma = q2;
			}
			for(i64 q = zmi; q <= zma; q++)
			{
				ld w = calc(q);
				ans = max(ans, w);
			}
/*			for(;;)
			{
				i64 need = 0;
				forn(k, cnt)
				{
					need += z - a[k];
				}
				if (need > x) break;
				For(k, cnt, n - 1)
				{
					if (a[k] < z + 1)
					{
						need += z + 1 - a[k];
					}
				}
				if (need > x) break;
				ld w = -need;
				forn(k, cnt)
				{
					w += 1.0 / cnt * 36 * (z - a[k]);
				}
				if (ans < w) ans = w;
				if (w > tmp)
				{
					tmp = w;
					zb = z;
				}
				zma = z;
				z++;
			}
			if (zmi <= zma && zb != zmi && zb != zma)
				cerr << cnt << " " << zmi << " " << zma << " " << zb << endl;*/
		}

		printf("%0.9lf\n", (double)ans);
		
		fflush(stdout);
	}

	return 0;
}
