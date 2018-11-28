#include <cstdio>
#include <cstring>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <utility>
#include <queue>
#include <functional>
#include <map>
#include <set>

#define fi first
#define se second
#define fo(i,a,b) for (int i = a; i <= b; i ++)
#define fd(i,a,b) for (int i = a; i >= b; i --)
#define fe(i,x,y) for (int i = x, y = lnk[i]; i; i = nxt[i], y = lnk[i])
#define mkp make_pair
#define pb push_back
#define Fill(x,y) memset(x,y,sizeof(x))
#define Cpy(x,y) memcpy(x,y,sizeof(x))
#define Bit(x,y) ((((x) >> (y)) & 1))
#define mit map<int,SI>::iterator
#define sit SI::iterator
#define SQR(x) ((x) * (x))

using namespace std;
 
typedef long long LL;
typedef long double DB;
typedef pair <DB, DB> PD;
typedef pair <LL, LL> PLI;
typedef pair <PD, int> PDI;
typedef pair <int, int> PI;
typedef pair <int, PI> PII;
typedef pair <PI, PI> PIII;
typedef set <PI> SI;
typedef vector <int> VI;
 
int Read()
 {
    char c; while (c = getchar(), (c != '-') && (c < '0' || c > '9'));
    bool neg = (c == '-'); int ret = (neg ? 0 : c - 48);
    while (c = getchar(), c >= '0' && c <= '9') ret = ret * 10 + c - 48;
    return neg ? -ret : ret;
 }
 
const int MAXN = 1005;

struct Block
 {
 	int xa, ya, xb, yb;
 } a[MAXN];
int N, W, H, dist[MAXN][MAXN], d[MAXN];
bool kill[MAXN];

bool in(int x, int l, int r) { return x >= l && x <= r; }

int Dist(int la, int ra, int lb, int rb)
 {
 	if (in(la, lb, rb) || in(ra, lb, rb) || in(lb, la, ra) || in(rb, la, ra)) return 0;
 	return min(abs(rb - la), abs(ra - lb)) - 1;
 }
 
int main()
 {
 	freopen("c.in", "r", stdin), freopen("c.out", "w", stdout);
 	int cases = Read();
 	fo (ca, 1, cases)
 	 {
 	 	scanf("%d%d%d", &W, &H, &N);
 	 	fo (i, 1, N)
 	 	 	a[i].xa = Read(), a[i].ya = Read(), a[i].xb = Read(), a[i].yb = Read();
 	 	fo (i, 1, N)
 	 	 {
 	 	 	dist[i][N + 1] = dist[N + 1][i] = a[i].xa;
 	 	 	dist[i][N + 2] = dist[N + 2][i] = W - a[i].xb - 1;
 	 	 	
 	 	 	fo (j, 1, N)
 	 	 		dist[i][j] = max(Dist(a[i].xa, a[i].xb, a[j].xa, a[j].xb), Dist(a[i].ya, a[i].yb, a[j].ya, a[j].yb));
 	 	 }
 	 	Fill(d, 60), d[N + 1] = 0, Fill(kill, 0), dist[N + 1][N + 2] = dist[N + 2][N + 1] = W;
 	 	fo (i, 1, N + 2)
 	 	 {
 	 	 	int mi = 1e9, mp = 0;
 	 	 	fo (j, 1, N + 2) if (!kill[j] && d[j] < mi) mi = d[j], mp = j;
 	 	 	kill[mp] = 1;
 	 	 	fo (j, 1, N + 2) d[j] = min(d[j], d[mp] + dist[mp][j]);
 	 	 }
 	 	printf("Case #%d: %d\n", ca, d[N + 2]);
 	 }
 	return 0;
 }

