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
int n;
int a[1024];
int xs[1024];
int d[1024][1024];
int p[1024];
int cl[1024];
int cr[1024];

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
		
		scanf("%d", &n);
		forn(i, n)
		{
			scanf("%d", &a[i]);
			xs[i] = a[i];
		}
		sort(xs, xs + n);
		forn(i, n)
		{
			a[i] = lower_bound(xs, xs + n, a[i]) - xs;
			p[a[i]] = i;
		}
		forn(i, n)
		{
			cl[i] = cr[i] = 0;
			int k = p[i];
			forn(j, k)
			{
				cl[i] += a[j] > i;
			}
			For(j, k + 1, n - 1)
			{
				cr[i] += a[j] > i;
			}
		}

		memset(d, 0x3f, sizeof(d));
		d[1][0] = cl[0];
		d[0][1] = cr[0];

		forn(i, n)
		{
			forn(j, n)
			{
				if (i == j) continue;
				int z = max(i, j);
				d[z + 1][j] = min(d[z + 1][j], d[i][j] + cl[z]);
				d[i][z + 1] = min(d[i][z + 1], d[i][j] + cr[z]);
			}
		}
		int ans = min(d[n][0], d[0][n]);
		forn(i, n)
		{
			ans = min(ans, d[i][n]);
			ans = min(ans, d[n][i]);
		}

		printf("%d\n", ans);
		
		fflush(stdout);
	}

	return 0;
}
