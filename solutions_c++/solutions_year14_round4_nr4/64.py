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

const int MOD = 1000000007;

int qq;
int n, m;
char s[1024];
string a[1024];
int b[1024];
int c[1024][1024];
int d[1024][2];
int dn[1024][2];

void solve(int n, int m, int &ans, int &sum)
{
	int k = min(n, m);

	clr(b);
	memset(d, 0xff, sizeof(d));
	d[0][0] = 1;
	d[0][1] = 0;
	forn(i, n)
	{
		memset(dn, 0xff, sizeof(dn));
		clr(dn);
		int len = 0;
		int mi = b[0];
		int cnt_mi = 0;
		forn(j, m)
		{
			if (b[j] < mi)
			{
				mi = b[j];
				cnt_mi = 1;
			}
			else if (b[j] == mi)
			{
				cnt_mi++;
			}
		}
		forn(j, m + 1)
		{
			if (d[j][0] < 0) continue;
			if (j < m)
			{
				if (dn[j + 1][0] < 0)
				{
					dn[j + 1][0] = 1;
					dn[j + 1][1] = 0;
				}

				dn[j + 1][0] = dn[j + 1][0] * (i64)(m - j) % MOD;
				dn[j + 1][1] = d[j][1] + a[i].sz;
			}
			if (mi > 0 || cnt_mi > )
			if (dn[j][0] < 0)
			{
				dn[j][0] = 1;
				dn[j][1] = 0;
			}
			dn[j][0] = dn[j][0] * (i64)(m - j) % MOD;
			dn[j][1] = d[j][1] + (a[i].sz - mi);
		}
		ans = ans * (i64)cnt_mi % MOD;
		sum += a[i].sz - mi;
		if (i < n - 1)
		{
			while (len < a[i].sz && len < a[i + 1].sz && a[i][len] == a[i + 1][len]) len++;
		}
		forn(j, m)
		{
			b[j] = min(b[j], len);
		}
		memmove(d, dn, sizeof(d));
	}

	ans = d[k][0];
	sum = k + d[k][1];
	if (ans < 0) cerr << "Botwa !!!" << endl;
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	clr(c);
	forn(i, 1024)
	{
		c[i][i] = c[i][0] = 1;
		For(j, 1, i - 1)
		{
			c[i][j] = c[i - 1][j - 1] + c[i - 1][j];
			if (c[i][j] >= MOD) c[i][j] -= MOD;
		}
	}

	scanf("%d", &qq);
	forn(ii, qq)
	{
		printf("Case #%d: ", ii+1);
		fprintf(stderr, "Case #%d:\n", ii+1);
		
		scanf("%d%d", &n, &m);
		forn(i, n)
		{
			scanf("%s", s);
			a[i] = s;
		}
		sort(a, a + n);

		int ans, sum;
		solve(n, m, ans, sum);
/*		if (n < m)
		{
			ans = ans * (i64)c[m][n] % MOD;
		}*/
		printf("%d %d\n", sum, ans);
		
		fflush(stdout);
	}

	return 0;
}
