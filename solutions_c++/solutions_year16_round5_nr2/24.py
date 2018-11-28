#include "bits/stdc++.h"

using namespace std;

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

#ifdef ROOM_311
__attribute__((destructor)) void fini_main()
{
	fprintf(stderr, "Execution time = %0.0lf ms\n", clock() * 1000.0 / CLOCKS_PER_SEC);
}
#endif

#define MY_RAND 1
#if MY_RAND
uint64_t rnd_data = 0xDEADBEEFDULL;
inline void my_srand(int seed) { rnd_data = ((uint64_t)seed << 16) | 0x330E; }
inline int my_rand() { rnd_data = rnd_data * 0x5DEECE66DULL + 0xB; return (rnd_data >> 17) & 0x7FFFFFFF; }
#define rand my_rand
#define srand my_srand
#endif

template <class _T> inline _T sqr(const _T &x) { return x * x; }
template <class _T> inline string tostr(const _T &a) { ostringstream os(""); os << a; return os.str(); }

// Types
typedef double ld;
typedef long long i64;
typedef unsigned long long u64;
typedef pair < int, int > PII;
typedef set < int > SI;
typedef vector < int > VI;
typedef map < string, int > MSI;

// Constants
const ld PI = 3.1415926535897932384626433832795L;
const ld EPS = 1e-11;

int n, m, l;
int pa[128];
VI a[128];
char f[128];
char s[128];
bool u[128];
int p[128];
int cs[128];
ld c[128][128];
ld d[128];

void calc_pref(char *a, int n, int *p)
{
	int q = -1;
	p[0] = q;
	For(i, 1, n - 1)
	{
		while (q != -1 && a[i] != a[q + 1]) q = p[q];
		if (a[i] == a[q + 1]) q++;
		p[i] = q;
	}
}

void dfs(int k)
{
	u[k] = true;
	cs[k] = 0;
	d[k] = 1;
	forn(i1, a[k].sz)
	{
		int i = a[k][i1];
		if (!u[i]) dfs(i);
		cs[k] += cs[i];
		d[k] *= d[i] * c[cs[k]][cs[i]];
	}
	cs[k]++;
}

void precalc()
{
	l = strlen(s);
	calc_pref(s, l, p);
	clr(u);
	clr(cs);
	clr(c);
	forn(i, 101)
	{
		c[i][0] = c[i][i] = 1;
		For(j, 1, i - 1)
		{
			c[i][j] = c[i - 1][j - 1] + c[i - 1][j];
		}
	}
	dfs(n);
}

bool check()
{
	int q = -1;
	clr(u);
	u[n] = true;
	forn(tmp, n)
	{
		ld ns[128];
		clr(ns);
		int sum = 0;
		ld total = 1;
		forn(i, n)
		{
			if (u[i]) continue;
			if (!u[pa[i]]) continue;
			sum += cs[i];
			total *= c[sum][cs[i]];
		}
		ld sns = 0;
		forn(i, n)
		{
			if (u[i]) continue;
			if (!u[pa[i]]) continue;
			ns[i] = total;
			ns[i] /= c[sum][cs[i]] * d[i];
			int ls = sum - cs[i];
			forn(j1, a[i].sz)
			{
				int j = a[i][j1];
				ls += cs[j];
				ns[i] *= c[ls][cs[j]] * d[j];
			}
			sns += ns[i];
		}
		ld z = rand() * 1.0 / 0x80000000U * sns;
		bool bb = false;
		int last = 0;
		forn(i, n)
		{
			if (u[i]) continue;
			if (!u[pa[i]]) continue;
			last = i;
			z -= ns[i];
			if (z < 0)
			{
				last = i;
				bb = true;
				break;
			}
		}
		if (!bb)
		{
			cerr << "Botwa !!!" << endl;
		}
		char cc = f[last];
//		cerr << cc;
		u[last] = true;
		while (q != -1 && s[q + 1] != cc) q = p[q];
		if (s[q + 1] == cc) q++;
		if (q == l - 1)
		{
//			cerr << endl;
			return true;
		}
	}
//	cerr << endl;
	return false;
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);
	
	int tc;
	scanf("%d", &tc);
	For(tn, 1, tc)
	{
		printf("Case #%d: ", tn);
		
		scanf("%d", &n);
		forn(i, n)
		{
			scanf("%d", &pa[i]);
			pa[i]--;
			if (pa[i] < 0)
				pa[i] = n;
			a[pa[i]].pb(i);
		}
		scanf("%s", f);

		scanf("%d", &m);
		const int cnt = 2000;
		forn(i, m)
		{
			scanf("%s", s);
			precalc();
			int sum = 0;
			forn(tmp, cnt)
			{
				sum += check();
			}
			printf("%0.2f%c", (double)sum / cnt, " \n"[i == m - 1]);
		}

		forn(i, n + 1)
		{
			a[i].clear();
		}

		fprintf(stderr, "Case #%d: %0.0lf ms\n", tn, clock() * 1000.0 / CLOCKS_PER_SEC);
	}
	fprintf(stderr, "---\n");
	
	return 0;
}
