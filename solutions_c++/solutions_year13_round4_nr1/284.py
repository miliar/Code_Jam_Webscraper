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

#define fi first
#define se second
#define fo(i,a,b) for (int i = a; i <= b; i ++)
#define fd(i,a,b) for (int i = a; i >= b; i --)
#define mkp make_pair
#define pb push_back
#define Fill(x,y) memset(x,y,sizeof(x))
#define Cpy(x,y) memcpy(x,y,sizeof(x))

using namespace std;

typedef long long LL;
typedef pair <int,int> PI;
typedef pair <LL, LL> PLL;

int Read()
 {
	char c; while (c = getchar(), (c != '-') && (c < '0' || c > '9'));
	bool neg = (c == '-'); int ret = neg ? 0 : c - 48;
	while (c = getchar(), c >= '0' && c <= '9') ret = ret * 10 + c - 48;
	return neg ? -ret : ret;
 }
 
const int MAXN = 1005, MOD = 1000002013;

pair <int, PI> a[MAXN];
int N, M, n, v[MAXN<<1];
LL ans, cur, cnt[MAXN<<1], cnt2[MAXN<<1];

LL Cal(LL stop) { return (stop * N - (stop * (stop - 1) / 2)) % MOD; }

int main()
 {
	freopen("A.in", "r", stdin), freopen("A.out", "w", stdout);
	int cases = Read(); fo (cas, 1, cases)
	 {
		N = Read(), M = Read(); n = 1; ans = 0;
		fo (i, 1, M)
		 {
			a[i].se.fi = Read(), a[i].se.se = Read(), a[i].fi = Read(), v[i+i-1] = a[i].se.fi, v[i+i] = a[i].se.se;
			LL stop = a[i].se.se - a[i].se.fi;
			(ans += (LL) a[i].fi * Cal(stop)) %= MOD;
		 }
		sort(v + 1, v + M + M + 1); fo (i, 2, M + M) if (v[i] != v[i - 1]) v[++ n] = v[i];
		Fill(cnt, 0), Fill(cnt2, 0);
		fo (i, 1, M)
		 {
			a[i].se.fi = lower_bound(v + 1, v + n + 1, a[i].se.fi) - v, a[i].se.se = lower_bound(v + 1, v + n + 1, a[i].se.se) - v;
			cnt[a[i].se.fi] += a[i].fi, cnt2[a[i].se.se] += a[i].fi;
		 }
		cur = 0;
		fo (i, 1, n) if (cnt2[i])
		 {
			fd (j, i, 1) if (cnt[j])
			 {
				if (cnt2[i] <= cnt[j])
				 {
					(cur += (LL) (cnt2[i] % MOD) * Cal(v[i] - v[j])) %= MOD;
					cnt[j] -= cnt2[i], cnt2[i] = 0;
					break;
				 } else
				 {
					(cur += (LL) (cnt[j] % MOD) * Cal(v[i] - v[j])) %= MOD;
					cnt2[i] -= cnt[j], cnt[j] = 0;
				 }
			 }
		 }
		printf("Case #%d: %lld\n", cas, (ans + MOD - cur) % MOD);
	 }
	return 0;
 }
