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
 
const int MAXN = 10005;

set <PI> t;
int N, M, a[MAXN];
bool clear[MAXN];

int main()
 {
 	freopen("a.in", "r", stdin), freopen("a.out", "w", stdout);
 	int cases = Read();
 	fo (ca, 1, cases)
 	 {
 	 	scanf("%d%d", &N, &M);
 	 	fo (i, 1, N) a[i] = Read();
 	 	sort(a + 1, a + N + 1);
 	 	Fill(clear, 0);
 	 	int ans = 0;
 	 	t.clear();
 	 	
 	 	fo (i, 1, N) t.insert(mkp(a[i], i));
 	 	
 	 	fd (i, N, 1) if (!clear[i])
 	 	 {
 	 	 	clear[i] = 1; ans ++;
 	 	 	set<PI>::iterator ws = t.lower_bound(mkp(a[i], i));
 	 	 	t.erase(ws);
 	 	 	ws = t.lower_bound(mkp(M - a[i] + 1, 0));
 	 	 	if (ws != t.begin())
 	 	 	 {
 	 	 	 	ws --;
 	 	 	 	clear[ws->se] = 1;
 	 	 	 	t.erase(ws);
 	 	 	 }

 	 	 }
 	 	printf("Case #%d: %d\n", ca, ans);
 	 }
 	return 0;
 }

