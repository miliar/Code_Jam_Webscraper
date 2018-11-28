#include <cstdio>
#include <algorithm>
using namespace std;

typedef long long ll;
typedef pair <int, int> ii;

const int Maxm = 2005;
const ll mod = 1000002013ll;

int t;
int n, m;
ii p[Maxm];
int res1, res2;
int a[Maxm], b[Maxm], len;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		scanf("%d %d", &n, &m);
		res1 = res2 = 0;
		for (int i = 0; i < m; i++) {
			int o, e, q; scanf("%d %d %d", &o, &e, &q);
			p[2 * i] = ii(o, -q); p[2 * i + 1] = ii(e, q);
			res1 = (res1 + ll(2ll * n - (e - o) + 1) * ll(e - o) / 2ll % mod * ll(q) % mod) % mod;
		}
		sort(p, p + 2 * m);
		len = 0;
		for (int i = 0; i < 2 * m; i++) {
			if (i) {
				int vsum = 0, bsum = 0;
				for (int j = 0; j < len; j++) {
					vsum = (vsum + ll(a[j]) * ll(b[j]) % mod) % mod;
					bsum = (bsum + b[j]) % mod;
				}
				int trav = p[i].first - p[i - 1].first;
				int cost = (ll(vsum) * ll(trav) % mod - ll(trav) * ll(trav - 1) / 2ll % mod * ll(bsum) % mod + mod) % mod;
				res2 = (res2 + cost) % mod;
				for (int j = 0; j < len; j++) a[j] -= trav;
			}
			if (p[i].second < 0) { a[len] = n; b[len] = -p[i].second; len++; }
			else for (int j = len - 1; j >= 0 && p[i].second; j--) {
				int tak = min(b[j], p[i].second); b[j] -= tak; p[i].second -= tak;
				if (b[j] == 0) len--;
			}
		}
		printf("Case #%d: %d\n", tc, (res1 - res2 + mod) % mod);
	}
	return 0;
}