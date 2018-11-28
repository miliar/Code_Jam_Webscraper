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
int n, p, k;
i64 a[10240];
i64 f[10240];
i64 a2[10240];
i64 f2[10240];
//int u[10240];
i64 ans[64];

bool check(i64 x)
{
	if (x == 0)
	{
		forn(i, k)
		{
			if (f[i] & 1) return false;
		}
		forn(i, k)
		{
			f[i] /= 2;
		}
		return true;
	}

	memcpy(f2, f, sizeof(f));
	memcpy(a2, a, sizeof(a));
	int sign = x > 0 ? 1 : -1;
	if (x < 0) x = -x;
	int j = 0;
	bool ok = true;
	forn(i, k)
	{
		if (f[i] <= 0) continue;
		while (j < k && a[j] < a[i] + x) j++;
		if (j >= k || a[j] != a[i] + x || f[j] < f[i])
		{
/*			cerr << "fail " << x << endl;
			forn(r, k)
			{
				cerr << a[r] << " ";
			}
			cerr << endl;
			forn(r, k)
			{
				cerr << f[r] << " ";
			}
			cerr << endl;
			cerr << "---" << endl;*/
			ok = false;
			break;
		}
		f[j] -= f[i];
	}
	if (ok)
	{
		int t = 0;
		forn(i, k)
		{
			if (f[i])
			{
				a[t] = a[i];
				f[t] = f[i];
				t++;
			}
		}
		k = t;
		if (sign < 0)
		{
			forn(i, k)
			{
				a[i] -= x;
			}
		}
	}
	else
	{
		memcpy(f, f2, sizeof(f));
		memcpy(a, a2, sizeof(a));
	}
	return ok;
}

bool rec(int i)
{
	if (i >= n) return true;
/*
			cerr << "vvv" << endl;
			forn(r, k)
			{
				cerr << a[r] << " ";
			}
			cerr << endl;
			forn(r, k)
			{
				cerr << f[r] << " ";
			}
			cerr << endl;
			cerr << "---" << endl;
*/
	forn(j, p)
	{
//		if (u[j] >= f[j]) continue;
		i64 x = a[j];
//		cerr << "? " << i << " " << x << endl;
		if (!check(x)) continue;
//		cerr << i << " " << x << endl;

		ans[i] = x;
//		u[j]++;
		if (rec(i + 1)) return true;
		else return false;
//		u[j]--;
	}
	return false;
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
		
		scanf("%d", &p);
		forn(i, p)
		{
			scanf("%lld", &a[i]);
		}
		i64 sum = 0;
		forn(i, p)
		{
			scanf("%lld", &f[i]);
			sum += f[i];
		}
		n = 1;
		while ((1LL << n) < sum) n++;

//		clr(u);
		k = p;
		bool bb = rec(0);
		if (!bb)
		{
			cerr << "Botwa !!" << endl;
			for(;;);
		}

		forn(i, n)
		{
			printf(" %lld", ans[i]);
		}
		puts("");
		
		fflush(stdout);
	}

	return 0;
}
