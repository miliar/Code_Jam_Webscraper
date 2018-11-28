// _temp.cpp : Defines the entry point for the console application.
//

#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;

#define MAXN 200000
#define INF 1100000000
#define MOD 1000002013

pair< int, int > inp[MAXN];
pair< int, int > oup[MAXN];
pair< int, int>  t[MAXN];

int n, m;
int k;

ll ans;
ll ans1;

ll dist(int x, int y) {
    ll res = y - x;
	res = res * (n + n - res + 1) / 2;
	return res % 1000002013;
}

int main()
{
	int tc;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%i", &tc);
	for(int tt=1; tt<=tc; ++tt) {
		scanf("%i %i", &n, &m);
		ans1 = 0;
		int cnt = 0;
		for(int i=0; i<m; ++i) {
			int p, q, z;
			scanf("%i %i %i", &p, &q, &z);
			//printf("%i  p=%i q=%i\n", i, p, q);			
			ans1 += (dist(p, q)* (z % MOD)) % MOD;
			if (ans1 < 0) fprintf(stderr, "sadfasf\n");

			inp[cnt] = make_pair(p, z);
			oup[cnt] = make_pair(q, z);
			cnt++;

		}
		inp[cnt] = make_pair(INF + 1, 1);
		oup[cnt] = make_pair(INF, 1);		
		cnt++;
		k = 0;
		ans = 0;

		sort(inp, inp + cnt);
		sort(oup, oup + cnt);

		int i=0;
		int j=0;

		while (i < cnt || j < cnt) {
			while (true) {
			    int x = inp[i].first;
			    int y = oup[j].first;
				if (x <= y) {
					t[k++] = make_pair(x, inp[i].second);
					//printf("i=%i\n", i);
					i = i + 1;
				} else {
					if (y==INF) goto ex;
					int tmp = oup[j].second;
					while (tmp) {						
						if (t[k - 1].second >= tmp) {
							t[k - 1].second -= tmp;
							ans += dist(t[k-1].first, y) * (tmp % MOD);
							ans = (ans % MOD);							
							tmp = 0;
						} else {
							ans += dist(t[k-1].first, y) * (t[k-1].second % MOD);
							ans = (ans % MOD);							
							tmp -= t[k - 1].second;
							k--;
						}
					}
					j++;
				}
			} 			
		}
ex:
		printf("Case #%i: ", tt);
		ans1 = ans1 % 1000002013;
		ans  = ans  % 1000002013;
		int res = ans1 - ans;
		if (res < 0) res += 1000002013;
		printf("%i\n", res);
	}
	return 0;
}

