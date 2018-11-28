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

int n;
char s[1024];
bool a[32][32];
int b[32];
int d[1 << 4][1 << 4];

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
			scanf("%s", s);
			b[i] = 0;
			forn(j, n)
			{
				a[i][j] = s[j] == '1';
				b[i] |= a[i][j] << j;
			}
		}
		clr(d);
		forn(mask1, 1 << n)
		{
			forn(mask2, 1 << n)
			{
				if (__builtin_popcount(mask1) != __builtin_popcount(mask2)) continue;
				forn(i, n)
				{
					if (!(mask1 & (1 << i))) continue;
					forn(j, n)
					{
						if (!(mask2 & (1 << j))) continue;
						d[mask1][mask2] += !a[i][j];
					}
				}
				for (int sm1 = mask1; sm1; sm1 = (sm1 - 1) & mask1)
				{
					for (int sm2 = mask2; sm2; sm2 = (sm2 - 1) & mask2)
					{
						if (__builtin_popcount(sm1) != __builtin_popcount(sm2)) continue;
						bool ok = true;
						forn(i, n)
						{
							if (!(mask1 & (1 << i))) continue;
							if (sm1 & (1 << i)) continue;
							forn(j, n)
							{
								if (!(mask2 & (1 << j))) continue;
								if (!(sm2 & (1 << j))) continue;
								if (a[i][j])
								{
									ok = false;
									break;
								}
							}
						}
						if (!ok) continue;
						forn(i, n)
						{
							if (!(mask1 & (1 << i))) continue;
							if (!(sm1 & (1 << i))) continue;
							forn(j, n)
							{
								if (!(mask2 & (1 << j))) continue;
								if (sm2 & (1 << j)) continue;
								if (a[i][j])
								{
									ok = false;
									break;
								}
							}
						}
						if (!ok) continue;
						d[mask1][mask2] = min(d[mask1][mask2], d[sm1][sm2] + d[mask1 ^ sm1][mask2 ^ sm2]);
					}
				}
			}
		}
		printf("%d\n", d[(1 << n) - 1][(1 << n) - 1]);

		fprintf(stderr, "Case #%d: %0.0lf ms\n", tn, clock() * 1000.0 / CLOCKS_PER_SEC);
	}
	fprintf(stderr, "---\n");
	
	return 0;
}
