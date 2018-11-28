// File Name: A.cpp
// Author: YangYue
// Created Time: Sat Jun  1 22:14:50 2013
//headers 
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <ctime>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <iostream>
#include <vector>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> PII;
typedef pair<double,double> PDD;
typedef pair<LL, LL>PLL;
typedef pair<LL,int>PLI;

#define lch(n) ((n<<1))
#define rch(n) ((n<<1)+1)
#define lowbit(i) (i&-i)
#define sqr(x) ((x)*(x))
#define fi first
#define se second
#define MP make_pair
#define PB push_back

const int MaxN = 200005;
const double eps = 1e-7;
const double DINF = 1e100;
const int INF = 1000000006;
const LL LINF = 1000000000000000005ll;
const int MOD = 1000002013;

LL n;
int m;
PLL a[MaxN];
LL calc(int s, int t) {
	if (s == t) return 0;
	LL len = t - s;
	//cout << s << " " << t << endl;
	return (2 * n - len + 1) * len / 2 % MOD;
}
int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);

	int cases; cin >> cases;

	for (int cas = 1; cas <= cases; ++cas) {
		printf("Case #%d: ", cas);
		cin >> n >> m;
		LL ans = 0;
		int tot = 0;
		for (int i = 1; i <= m; ++i) {
			int s, t, p; scanf("%d%d%d",&s,&t,&p);
			a[tot++] = MP(s, -p);
			a[tot++] = MP(t, p);
			ans += p * calc(s, t);
			ans %= MOD;
		}
		sort(a, a + tot);
	//	cout << calc(6, 7) + calc(1, 9) - calc(1, 7) - calc(6, 9) << endl;
		priority_queue<PLL> heap;
		for (int i = 0; i < tot; ++i) {
			LL p = -a[i].se;
			LL pos = a[i].fi;
			
			if (p > 0) {
				heap.push(MP(pos, p));
			} else {
				p = -p;
				while (!heap.empty() && p > 0) {
					PII t = heap.top();
					heap.pop();
					if (t.se <= p) {
						p -= t.se;
						ans += MOD - t.se * calc(t.fi, pos) % MOD;
					} else {
						t.se -= p;
						ans += MOD - p * calc(t.fi, pos) % MOD;
						heap.push(t);
						p = 0;
					}
					ans %= MOD;
				}
			}
		}
		cout << ans % MOD << endl;
	}
	
	return 0;
}

// hehe ~


