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

struct tp{int x, y;};

int qq;
int n, h, w;
tp a[1024][2];
int b[1024][1024];
int d[1024];
bool u[1024];

int get_d(int l1, int r1, int l2, int r2)
{
	if (l1 > r2) return l1 - r2 - 1;
	else if (l2 > r1) return l2 - r1 - 1;
	else return 0;
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
		
		scanf("%d%d%d", &w, &h, &n);
		forn(i, n)
		{
			forn(j, 2)
			{
				scanf("%d%d", &a[i][j].x, &a[i][j].y);
			}
			if (a[i][0].x > a[i][1].x) swap(a[i][0].x, a[i][1].x);
			if (a[i][0].y > a[i][1].y) swap(a[i][0].y, a[i][1].y);
		}
		int st = n;
		int en = n + 1;
		a[st][0].x = -1;
		a[st][0].y = 0;
		a[st][1].x = -1;
		a[st][1].y = h - 1;
		a[en][0].x = w;
		a[en][0].y = 0;
		a[en][1].x = w;
		a[en][1].y = h - 1;
		n += 2;
		forn(i, n)
		{
			forn(j, n)
			{
				int dx = get_d(a[i][0].x, a[i][1].x, a[j][0].x, a[j][1].x);
				int dy = get_d(a[i][0].y, a[i][1].y, a[j][0].y, a[j][1].y);
				b[i][j] = max(dx, dy);
			}
		}
		b[st][en] = w;
/*		forn(i, n)
		{
			forn(j, n)
			{
				cerr << b[i][j] << " ";
			}
			cerr << endl;
		}*/
		clr(u);
		memset(d, 0x3f, sizeof(d));
		d[st] = 0;
		forn(ii, n)
		{
			int mi = 0x3f3f3f3f;
			int mj = -1;
			forn(i, n)
			{
				if (!u[i] && d[i] < mi)
				{
					mi = d[i];
					mj = i;
				}
			}
			if (mj < 0) break;
			u[mj] = true;
			forn(i, n)
			{
				if (d[i] > mi + b[mj][i])
				{
					d[i] = mi + b[mj][i];
				}
			}
		}
		int ans = d[en];
		printf("%d\n", ans);
		
		fflush(stdout);
	}

	return 0;
}
