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
 
VI c[10];
char s[10][20];
int M, N, id, ans1, ans2, bel[20], vis[100][26], t[100][20], len[20];

void DFS(int d)
 {
 	if (d > N)
 	 {
 	 	fo (i, 1, M) c[i].clear();
 	 	fo (i, 1, N) c[bel[i]].pb(i);
 	 	int sum = 0;
 	 	// checkbad
 	 	fo (i, 1, M) if (!c[i].size()) return;
 	 	fo (i, 1, M)
 	 	 {
 	 	 	++ id, ++ sum; int n = 1;
 	 	 	fo (j, 0, (int) c[i].size() - 1)
 	 	 	 {
 	 	 	 	int k = c[i][j], x = 1;
 	 	 	 	fo (p, 1, len[k])
 	 	 	 	 {
 	 	 	 	 	if (vis[x][s[k][p] - 'A'] < id) vis[x][s[k][p] - 'A'] = id, ++ sum, t[x][s[k][p] - 'A'] = ++ n;
 	 	 	 	 	x = t[x][s[k][p] - 'A'];
 	 	 	 	 }
 	 	 	 }
 	 	 }
 	 	if (sum > ans1) ans1 = sum, ans2 = 1; else if (sum == ans1) ans2 ++;
 	 	return;
 	 }
 	fo (i, 1, M) bel[d] = i, DFS(d + 1);
 }
 
int main()
 {
 	freopen("d.in", "r", stdin), freopen("d.out", "w", stdout);
 	int cases = Read();
 	fo (ca, 1, cases)
 	 {
 	 	scanf("%d%d", &N, &M);
 	 	fo (i, 1, N)
 	 	 	scanf("%s", s[i] + 1), len[i] = strlen(s[i] + 1);
 	 	ans1 = 0, ans2 = 0, DFS(1);
 	 	printf("Case #%d: %d %d\n", ca, ans1, ans2);
 	 }
 	return 0;
 }

