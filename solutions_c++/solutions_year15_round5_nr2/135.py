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
typedef long long i64;
typedef __int128 i128;
typedef unsigned long long u64;
typedef set < int > SI;
typedef vector < int > VI;
typedef map < string, int > MSI;
typedef pair < int, int > PII;

int qq;
int n, k;
int a[102400];
int x[102400];
int mi[102400];
int ma[102400];

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
		
		scanf("%d%d", &n, &k);
		forn(i, n - k + 1)
		{
			scanf("%d", &a[i]);
		}
		forn(i, k - 1)
		{
			x[i] = 0;
		}
		For(i, k - 1, n - 1)
		{
			x[i] = a[i - (k - 1)];
			forn(j, k - 1)
			{
				x[i] -= x[i - j - 1];
			}
		}
		forn(i, k)
		{
			mi[i] = x[i];
			ma[i] = x[i];
		}
		int ans = 0;
		forn(i, n)
		{
			mi[i % k] = min(mi[i % k], x[i]);
			ma[i % k] = max(ma[i % k], x[i]);
		}
		forn(i, k)
		{
			ans = max(ans, ma[i] - mi[i]);
		}

		int zz = 0;
		forn(i, k)
		{
			zz += mi[i];
		}
		zz = (zz + k * 1000000000LL) / k - 1000000000LL;
		int diff = 0;
		forn(i, k)
		{
			int r = zz - mi[i];
			mi[i] += r;
			ma[i] += r;
			diff += r;
		}
		forn(i, k)
		{
			if (!diff) break;
			sort(ma, ma + k);
			ma[0]++;
			diff++;
		}
		if (diff) for(;;);
		int mma = ma[0];
		forn(i, k)
		{
			mma = max(mma, ma[i]);
		}
		ans = max(ans, mma - mi[0]);

		printf("%d\n", ans);
		
		fflush(stdout);
	}

	return 0;
}
