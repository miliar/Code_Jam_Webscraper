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
 
const int MAXN = 100005;

double C, F, X, ans, cost;

int main()
 {
	freopen("b.in", "r", stdin), freopen("b.out", "w", stdout);
	int cases = Read();
	fo (ca, 1, cases)
	 {
		scanf("%lf%lf%lf", &C, &F, &X);
		cost = 0, ans = X / 2.0;
		fo (i, 1, MAXN)
		 {
			cost += C / (2.0 + F * (i - 1));
			if (cost >= ans) break;
			ans = min(ans, cost + X / (2.0 + F * i));
		 }
		printf("Case #%d: %.10f\n", ca, ans);
	 }
	return 0;
 }
