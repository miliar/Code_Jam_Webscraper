#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/hash_policy.hpp>
using namespace std;
using namespace __gnu_pbds;
typedef long long LL;
LL revNum(LL k)
{
	LL rt = 0;
	while (k) {
		rt = (rt * 10) + (k % 10);
		k /= 10;
	}
	return rt;
}
main()
{
	int t, cs = 0;
	gp_hash_table<LL, bool> v;
	bool f;
	queue<LL> Q;
	LL n, rev, ans, sz, tmp;
	scanf("%d", &t);
	while (t--) {
		f = 0;
		v.clear();
		while (!Q.empty()) Q.pop();
		scanf("%lld", &n);
		if (n == 1) {
			printf("Case #%d: 1\n", ++cs);
			continue;
		}
		Q.push(1), v[1] = 1;
		for (ans = 2 ; ans <= n ; ++ans) {
			sz = Q.size();
			while (sz--) {
				tmp = Q.front();
				Q.pop();
				rev = revNum(tmp);
				if (tmp + 1 == n || rev == n) {
					f = 1;
					break;
				}
				if (!v[tmp + 1]) Q.push(tmp + 1), v[tmp + 1] = 1;
				if (!v[rev]) Q.push(rev), v[rev] = 1;
			}
			if (f) break;
		}
		printf("Case #%d: %d\n", ++cs, ans);
	}
}