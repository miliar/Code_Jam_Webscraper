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
typedef pair < ld, ld > PDD;
typedef set < int > SI;
typedef vector < int > VI;
typedef map < string, int > MSI;

// Constants
const ld PI = 3.1415926535897932384626433832795L;
const ld EPS = 1e-11;

struct tp{ld x,y,z;};

tp operator + (tp p1, tp p2)
{
	tp p;
	p.x = (p1.x + p2.x);
	p.y = (p1.y + p2.y);
	p.z = (p1.z + p2.z);
	return p;
}

tp operator - (tp p1, tp p2)
{
	tp p;
	p.x = (p1.x - p2.x);
	p.y = (p1.y - p2.y);
	p.z = (p1.z - p2.z);
	return p;
}

tp operator * (tp p1, ld v)
{
	tp p;
	p.x = (p1.x * v);
	p.y = (p1.y * v);
	p.z = (p1.z * v);
	return p;
}

tp operator * (ld v, tp p1)
{
	tp p;
	p.x = (p1.x * v);
	p.y = (p1.y * v);
	p.z = (p1.z * v);
	return p;
}

int n, m;
tp a[1024];
tp sp[1024];
ld t[1024][1024][2];
tp p0;
ld em[1024];

set < PDD > e[1024];

inline ld dist(tp p1, tp p2)
{
	return sqrt(sqr(p1.x-p2.x) + sqr(p1.y-p2.y) + sqr(p1.z-p2.z));
}

inline ld dist2(tp p1, tp p2)
{
	return sqr(p1.x-p2.x) + sqr(p1.y-p2.y) + sqr(p1.z-p2.z);
}

tp read_point()
{
	double x, y, z;
	scanf("%lf%lf%lf", &x, &y, &z);
	tp p;
	p.x = x;
	p.y = y;
	p.z = z;
	return p;
}

void calc_t(ld r)
{
	ld inf = 1e18;
	forn(i, n)
	{
		t[i][i][0] = t[i][i][1] = -1;
		forn(j, i)
		{
			t[i][j][0] = t[i][j][1] = -1;

			tp p = a[i] - a[j];
			tp v = sp[i] - sp[j];
			ld aa = v.x * v.x + v.y * v.y + v.z * v.z;
			ld bb = 2.0 * (p.x * v.x + p.y * v.y + p.z * v.z);
			ld cc = p.x * p.x + p.y * p.y + p.z * p.z - r * r;
//			cerr << i << " " << j << " " << aa << " " << bb << " " << cc << " " << endl;
			if (fabs(aa) > EPS)
			{
				ld dd = bb * bb - 4.0 * aa * cc;
//				cerr << "dd = " << dd << endl;
				if (dd < 0)
				{
					if (dist2(p0, p) <= r * r)
					{
						t[i][j][0] = 0.0;
						t[i][j][1] = inf;
					}
				}
				else
				{
					dd = sqrt(dd);
					ld t1 = (-bb - dd) / (2.0 * aa);
					ld t2 = (-bb + dd) / (2.0 * aa);
					if (t1 > t2) swap(t1, t2);
//					cerr << "t1, t2: " << t1 << " " << t2 << endl;
					if (t1 < 0) t1 = 0;
					if (t2 < 0) t2 = -1;
					if (t1 <= t2)
					{
						t[i][j][0] = t1;
						t[i][j][1] = t2;
					}
				}
			}
			else
			{
				if (dist2(p0, p) <= r * r)
				{
					t[i][j][0] = 0.0;
					t[i][j][1] = inf;
				}
			}

			t[j][i][0] = t[i][j][0];
			t[j][i][1] = t[i][j][1];
		}
	}
/*
	forn(i, n)
	{
		forn(j, n)
		{
			cerr << t[i][j][0] << " " << t[i][j][1] << "   ";
		}
		cerr << endl;
	}*/
}

void add_seg(set < PDD > &s, ld const &em, PDD t)
{
	if (t.first < em) t.first = em;
	if (t.first > t.second) return;
	__typeof(s.begin()) it = s.lower_bound(mp(t.first, -1.0));
	if (it != s.begin())
	{
		--it;
		if (it->second >= t.first)
		{
			t.first = it->first;
			if (t.second < it->second)
				t.second = it->second;
			s.erase(it);
		}
	}
	for(;;)
	{
		it = s.lower_bound(mp(t.first, -1));
		if (it == s.end()) break;
		
		if (it->first <= t.second)
		{
			if (it->second > t.second)
				t.second = it->second;
			s.erase(it);
		}
		else break;
	}
	s.insert(t);
}

bool check(ld r)
{
	calc_t(r);

	forn(i, n)
	{
		e[i].clear();
		em[i] = 0.0;
	}
	add_seg(e[0], em[0], mp(0, m));
	
	for(;;)
	{
		ld mi = 1e18;
		int mj = -1;
		forn(i, n)
		{
			if (!e[i].empty() && e[i].begin()->first < mi)
			{
				mi = e[i].begin()->first;
				mj = i;
			}
		}
		if (mj < 0) break;
		PDD tmp = *e[mj].begin();
		e[mj].erase(e[mj].begin());
		ld t0 = tmp.first;
		ld t1 = tmp.second;
		if (t0 > 1e4) break;
		em[mj] = t1 + 1e-15;
//		cerr << mj << " " << t0 << " " << t1 << endl;
		forn(i, n)
		{
			if (t[mj][i][0] < 0 || t[mj][i][0] > t1 || t[mj][i][1] < t0) continue;
			if (i == 1) return true;
			add_seg(e[i], em[i], mp(max(t0, t[mj][i][0]), min(t1, t[mj][i][1]) + m));
		}
	}

	return false;
}

ld solve()
{
/*	int z = check(2.0);
	cerr << "check = " << z << endl;
	return 2.0;*/
	ld mi = 0.0;
	ld ma = 2000.0;
	forn(tmp, 143)
	{
		if (ma - mi < 1e-5) break;
		ld q = (mi + ma) * 0.5;
		if (check(q)) ma = q;
		else mi = q;
	}
	return (mi + ma) * 0.5;
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);
	
	p0.x = p0.y = p0.z = 0.0;
	int tc;
	scanf("%d", &tc);
	For(tn, 1, tc)
	{
		printf("Case #%d: ", tn);
		scanf("%d%d", &n, &m);
		forn(i, n)
		{
			a[i] = read_point();
			sp[i] = read_point();
		}
		ld ans = solve();
		printf("%0.9f\n", (double)ans);

		fprintf(stderr, "Case #%d: %0.0lf ms\n", tn, clock() * 1000.0 / CLOCKS_PER_SEC);
	}
	fprintf(stderr, "---\n");
	
	return 0;
}
