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
#include <cstdio>

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

set <double> t;
double p[MAXN], q[MAXN];
int N, ans1, ans2;

int main()
 {
	freopen("d.in", "r", stdin), freopen("d.out", "w", stdout);
	int cases = Read();
	fo (ca, 1, cases)
	 {
		scanf("%d", &N);
		fo (i, 1, N) scanf("%lf", p + i);
		fo (i, 1, N) scanf("%lf", q + i);
		sort(p + 1, p + N + 1), sort(q + 1, q + N + 1);
		// case 1
		t.clear(), ans1 = ans2 = 0;
		fo (i, 1, N) t.insert(p[i]);
		fo (i, 1, N)
		 {
			set<double>::iterator x = t.lower_bound(q[i]);
			if (x == t.end()) break;
			t.erase(x), ans1 ++;
		 }
		t.clear();
		fo (i, 1, N) t.insert(q[i]);
		fo (i, 1, N)
		 {
			set<double>::iterator x = t.lower_bound(p[i]);
			if (x == t.end()) ++ ans2; else t.erase(x);
		 }
		printf("Case #%d: %d %d\n", ca, ans1, ans2);
	 }
	return 0;
 }
 