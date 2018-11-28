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
typedef long double ld;
typedef long long i64;
typedef unsigned long long u64;
typedef pair < int, int > PII;
typedef set < int > SI;
typedef vector < int > VI;
typedef map < string, int > MSI;

// Constants
const ld PI = 3.1415926535897932384626433832795L;
const ld EPS = 1e-11;

int z;
int a[1 << 13];

map < u64, bool > w;
int win[3][3] = {
{-1,0,2},
{0,-1,1},
{2,1,-1}
};

bool go(int k)
{
	if (k == 1) return true;
	if (!(k & 1)) return true;
	int t = k >> 1;
	a[t] = win[a[t * 2]][a[t * 2 + 1]];
	if (a[t] < 0) return false;
	return go(t);
}

bool solve(int n, int p, int r, int s)
{
	int c[3] = {p, r, s};
	int k = (1 << n) - p - r - s;
	if (k == (1 << n)) return true;
	bool res = false;
	u64 hh = k;
	int q = z + k - 1;
	if (q >= 0)
	{
		forn(i, n + 1)
		{
			hh = hh * 217;
			if (!(q & 1))
			{
				hh += a[q];
				if (!(q & (q - 1))) break;
				q--;
			}
			q >>= 1;
		}
	}
	else
	{
		hh *= 21987;
	}
	forn(i, 3)
	{
		hh = hh * 311 + c[i];
	}
	if (w.find(hh) != w.end()) return w[hh];

	int t = z + k;
	forn(i, 3)
	{
		if (!c[i]) continue;
		a[t] = i;
		if (!go(t)) continue;
/*		cerr << t << " " << i << endl;
		For(i, 1, z + z - 1)
		{
			cerr << a[i] << " ";
		}
		cerr << endl;*/
		c[i]--;
		if (solve(n, c[0], c[1], c[2]))
		{
			res = true;
			break;
		}
		c[i]++;
	}
	
	return w[hh] = res;
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
		int n, pp, rr, ss;
		scanf("%d%d%d%d", &n, &rr, &pp, &ss);
		z = 1 << n;
		w.clear();
		if (!solve(n, pp, rr, ss)) puts("IMPOSSIBLE");
		else
		{
			int c[3];
			c[0] = pp;
			c[1] = rr;
			c[2] = ss;
			forn(i, 1 << n)
			{
				forn(j, 3)
				{
					if (!c[j]) continue;
					a[z + i] = j;
					if (!go(z + i)) continue;
					c[j]--;
					if (solve(n, c[0], c[1], c[2])) break;
					c[j]++;
				}
			}
			forn(i, 1 << n)
			{
				putchar("PRS"[a[z + i]]);
			}
			puts("");
		}

		fprintf(stderr, "Case #%d: %0.0lf ms\n", tn, clock() * 1000.0 / CLOCKS_PER_SEC);
	}
	fprintf(stderr, "---\n");
	
	return 0;
}
