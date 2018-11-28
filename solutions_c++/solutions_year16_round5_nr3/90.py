#include <bits/stdc++.h>

using namespace std;

#define REP(i, a, b) for (int i = (a), _end_ = (b); i < _end_; ++i)
#define debug(...) fprintf(stderr, __VA_ARGS__)
#define mp make_pair
#define x first
#define y second
#define pb push_back
#define SZ(x) (int((x).size()))
#define ALL(x) (x).begin(), (x).end()

template<typename T> inline bool chkmin(T &a, const T &b) { return a > b ? a = b, 1 : 0; }
template<typename T> inline bool chkmax(T &a, const T &b) { return a < b ? a = b, 1 : 0; }

typedef long long LL;

const int oo = 0x3f3f3f3f;

const int maxn = 1000;

struct point
{
	int x, y, z;

	point() { }
	point(int _x, int _y, int _z): x(_x), y(_y), z(_z) { }

};

inline int sqr(int x) { return x * x; }

inline int dis(const point &a, const point &b)
{
	return sqr(a.x - b.x) + sqr(a.y - b.y) + sqr(a.z - b.z);
}

int n;
point a[maxn + 5];

int fa[maxn + 5];

struct Edge
{
	int x, y, dis;

	Edge() { }
	Edge(int _x, int _y, int _dis): x(_x), y(_y), dis(_dis) { }

};

int edn = 0;
Edge ed[maxn * maxn + 5];

inline bool operator<(const Edge &x, const Edge &y) { return x.dis < y.dis; }

int get(int x) { return fa[x] == x ? x : fa[x] = get(fa[x]); }

int main()
{
#ifdef matthew99
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	scanf("%d", &T);
	for (int cc = 1; cc <= T; ++cc)
	{
		printf("Case #%d: ", cc);
		scanf("%d%*d", &n);
		REP(i, 0, n) scanf("%d%d%d%*d%*d%*d", &a[i].x, &a[i].y, &a[i].z);
		edn = 0;
		REP(i, 0, n) REP(j, 0, i) ed[edn++] = Edge(i, j, dis(a[i], a[j]));
		sort(ed, ed + edn);
		REP(i, 0, n) fa[i] = i;
		REP(i, 0, edn)
		{
			fa[get(ed[i].x)] = get(ed[i].y);
			if (get(0) == get(1))
			{
				printf("%.15f\n", sqrt(ed[i].dis));
				break;
			}
		}
	}
	return 0;
}
