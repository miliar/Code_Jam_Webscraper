#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <map>

using namespace std;

const int maxn = 2005;
const long long mod = 1000002013ll;

#define A first
#define B second

map<long long, long long> now, in, out;
map<long long, int> pool;

void work() {
	int N, m; scanf("%d%d", &N, &m);

	long long ans = 0ll, n = N;

	now.clear(); in.clear(); out.clear(); pool.clear();
	for (int i = 0; i < m; ++i) {
		int x, y, p; scanf("%d%d%d", &x, &y, &p);
		in[x] += (long long)p; out[y] += (long long)p; pool[x] = 1; pool[y] = 1;

		long long len = y - x;
		(ans += ((n + n - len + 1ll) * len / 2ll % mod) * (long long) p % mod) %= mod;

		//cout << x << ", " << y << " = " << ans << endl;
	}

	//cout << ans << endl;

	for (map<long long, int>::iterator iter = pool.begin(); iter != pool.end(); ++iter) {
		long long pos = iter -> first;

		now[pos] += in[pos];

		long long v = out[pos];
		for (map<long long, int>::iterator i = iter; v > 0ll; --i) {
			long long k = i -> first;
			long long t = min(v, in[k]);
			if (t == 0ll) continue;

			long long tmp = (n + n + k - pos + 1ll) * (pos - k) / 2ll % mod;
			(tmp *= t) %= mod;
			ans = (ans - tmp + mod) % mod;
			v -= t; in[k] -= t;

			//cout << "GET " << pos << ", " << k << ", " << t << " = " << ans << endl;
		}
	}

	ans = (ans + mod) %mod;
	cout << ans << endl;
}

int main() {
	int T; scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		printf("Case #%d: ", i);
		work();
	}

	return 0;
}
