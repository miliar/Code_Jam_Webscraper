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

const int dx[4] = {1, 1, -1, -1};
const int dy[4] = {1, -1, -1, 1};

struct tp{int x, y;};

int n, m, k;
char a[102][102];
int pa[404];
bool u[404];

void get_p(int k, tp *p)
{
	if (k < m)
	{
		p[0].x = 0;
		p[0].y = k;
		p[1].x = 0;
		p[1].y = k + 1;
	}
	else if (k < m + n)
	{
		p[0].x = k - m;
		p[0].y = m;
		p[1].x = k - m + 1;
		p[1].y = m;
	}
	else if (k < m + n + m)
	{
		p[0].x = n;
		p[0].y = m - (k - m - n);
		p[1].x = n;
		p[1].y = m - (k - m - n) - 1;
	}
	else
	{
		p[0].x = n - (k - m - n - m);
		p[0].y = 0;
		p[1].x = n - (k - m - n - m) - 1;
		p[1].y = 0;
	}
}

tp get_a(tp p, int dir)
{
	tp ans = p;
	if (dir == 0) {}
	else if (dir == 1)
	{
		ans.y--;
	}
	else if (dir == 2)
	{
		ans.x--;
		ans.y--;
	}
	else if (dir == 3)
	{
		ans.x--;
	}
	return ans;
}

bool check_p(tp p)
{
	return p.x >= 0 && p.x < n && p.y >= 0 && p.y < m;
}

bool go(tp &p, tp f, int &dir)
{
	if (p.x == f.x && p.y == f.y) return true;
	forn(i, 4)
	{
		tp ap = get_a(p, dir);
		if (!check_p(ap))
		{
			dir = (dir + 1) & 3;
			continue;
		}
		char &ch = a[ap.x][ap.y];
		char nc = "\\/\\/"[dir];
		if (ch == ' ' || ch == nc)
		{
			ch = nc;
			p.x += dx[dir];
			p.y += dy[dir];
			dir = (dir + 3) & 3;
			return true;
		}
		else
		{
			dir = (dir + 1) & 3;
			continue;
		}
	}
	return false;
}

bool solve(tp p1, tp p2)
{
	tp p = p1;
	int dir = 0;
	if (p.x == 0) dir = 0;
	else if (p.y == m) dir = 1;
	else if (p.x == n) dir = 2;
	else if (p.y == 0) dir = 3;
	int cnt = 0;
	while (p.x != p2.x || p.y != p2.y)
	{
		if (++cnt > (n + 2) * (m + 2) * 2) return false;
		if (!go(p, p2, dir)) return false;
	}
	return true;
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
		printf("Case #%d:\n", tn);
		scanf("%d%d", &n, &m);
		k = (n + m) * 2;
		forn(i, n + m)
		{
			int x, y;
			scanf("%d%d", &x, &y);
			x--;
			y--;
			pa[x] = y;
			pa[y] = x;
		}
		memset(a, ' ', sizeof(a));
		forn(i, n)
		{
			a[i][m] = '\0';
		}
		bool ok = true;
		clr(u);
		forn(i, n + m)
		{
			int x = -1, y = -1;
			forn(j, k)
			{
				if (u[j]) continue;
				int l = j;
				For(l1, 1, k - 1)
				{
					if (++l == k) l = 0;
					if (!u[l])
					{
						break;
					}
				}
				if (pa[j] == l)
				{
					x = j;
					y = l;
					break;
				}
			}
			if (x < 0 || y < 0)
			{
				ok = false;
				break;
			}
			tp pl[2], pr[2];
			u[x] = true;
			u[y] = true;
			get_p(x, pl);
			get_p(y, pr);
//			cerr << "x = " << x << "  " << "y = " << y << endl;
			if (!solve(pl[1], pr[0]) || !solve(pl[0], pr[1]))
			{
				ok = false;
				break;
			}
		}
		if (!ok)
		{
			puts("IMPOSSIBLE");
		}
		else
		{
			forn(i, n)
			{
				forn(j, m)
				{
					if (a[i][j] == ' ') a[i][j] = '/';
				}
				puts(a[i]);
			}
		}

		fprintf(stderr, "Case #%d: %0.0lf ms\n", tn, clock() * 1000.0 / CLOCKS_PER_SEC);
	}
	fprintf(stderr, "---\n");
	
	return 0;
}
