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
#include <cmath>

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

int T, a[5][5], b[5][5];

int main()
 {
	freopen("a.in", "r", stdin), freopen("a.out", "w", stdout);
	scanf("%d", &T);
	fo (ca, 1, T)
	 {
		int r1, r2;
		scanf("%d", &r1);
		fo (i, 1, 4) fo (j, 1, 4) scanf("%d", &a[i][j]);
		scanf("%d", &r2);
		fo (i, 1, 4) fo (j, 1, 4) scanf("%d", &b[i][j]);
		int ans = 0, cnt = 0;
		fo (i, 1, 4)
			if (a[r1][i] != ans)
				fo (j, 1, 4) if (b[r2][j] == a[r1][i])
				 {
					ans = a[r1][i], ++ cnt;
					break;
				 }
		printf("Case #%d: ", ca);
		if (!cnt) puts("Volunteer cheated!");
		else if (cnt > 1) puts("Bad magician!");
		else printf("%d\n", ans);
	 }
	return 0;
 }
