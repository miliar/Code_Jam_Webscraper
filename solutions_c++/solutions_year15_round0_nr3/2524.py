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

const int f[5][5] = {
{0,0,0,0,0},
{0,1,2,3,4},
{0,2,-1,4,-3},
{0,3,-4,-1,2},
{0,4,3,-2,-1},
};

int qq;
int n;
i64 k;
char s[2024000];
int a[2024000];

int op(int l, int r)
{
	int sign = 1;
	if (l < 0) l *= -1, sign *= -1;
	if (r < 0) r *= -1, sign *= -1;
	return sign * f[l][r];
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
		
		scanf("%d%lld", &n, &k);
		scanf("%s", s);
		int m = 0;
		if (k > 12)
		{
			k = 12 + k % 4;
		}
		forn(i, k)
		{
			forn(j, n)
			{
				a[m++] = (s[j] - 'i') + 2;
			}
		}
		int li = m + 1, ri = -1;
		int z = 1;
		forn(i, m)
		{
			z = op(z, a[i]);
		}
		if (z != -1)
		{
			puts("NO");
			goto l1;
		}
		z = 1;
		forn(i, m)
		{
			z = op(z, a[i]);
			if (z == 2)
			{
				li = i;
				break;
			}
		}
		z = 1;
		ford(i, m)
		{
			z = op(a[i], z);
			if (z == 4)
			{
				ri = i;
				break;
			}
		}
		puts(li < ri - 1 ? "YES" : "NO");
l1:;		
		fflush(stdout);
	}

	return 0;
}
