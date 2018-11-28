#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <string>
#include <cstring>

using namespace std;

typedef pair<int, int> ii;
typedef long long ll;

const int maxn = 2010;
const int mod = 1000002013;
int s[maxn];
int f[maxn];
int p[maxn];
pair<int, ii> a[maxn];
pair<int, ll> d[maxn];

int calc(int n, int dist) {
	int res = (1ll * n * dist) % mod;
	int sub = (1ll * (dist - 1) * dist / 2) % mod;
	res -= sub;
	if(res < 0)
		res += mod;
	return res;
}

void solve() {
	int n, m;
	scanf("%d %d", &n, &m);
	int sum = 0;
	for(int i = 0; i < m; ++i) {
		scanf("%d %d %d", s + i, f + i, p + i);
		int add = (1ll * p[i] * calc(n, f[i] - s[i])) % mod;
		sum = (sum + add) % mod;
		a[i] = make_pair(s[i], make_pair(0, p[i]));
		a[m + i] = make_pair(f[i], make_pair(1, p[i]));
	}
	m *= 2;
	sort(a, a + m);
	int count = 0;
	int sum2 = 0;
	for(int i = 0; i < m; ++i) {
		if(a[i].second.first == 0) {
			if(count > 0 && d[count - 1].first == a[i].first) {
				d[count - 1].second += a[i].second.second;
			} else {
				d[count] = make_pair(a[i].first, a[i].second.second);
				++count;
			}
		} else {
			ll total = a[i].second.second;
			while(total > 0) {
				int dist = a[i].first - d[count - 1].first;
				int current = min(d[count - 1].second, total);
				total -= current;
				if((d[count - 1].second -= current) == 0) {
					--count;
				}
				int add = (1ll * current * calc(n, dist)) % mod;
				sum2 = (sum2 + add) % mod;
			}
		}
	}
	int ans = sum - sum2;
	if(ans < 0)
		ans += mod;
	cout << ans << endl;
}

int main(int argc, char **argv) {
//	freopen("A-sample.in", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int tt;
	scanf("%d", &tt);
	for(int t = 0; t < tt; ++t) {
		printf("Case #%d: ", t + 1);
		solve();
	}

	return 0;
}
