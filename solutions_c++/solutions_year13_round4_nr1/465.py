#include <iostream>
#include <cstring>
#include <set>
#include <cstdlib>
#include <cstdio>
#include <algorithm>

using namespace std;

const int modulo = 1000002013;
const int MAXM = 1050;

int n, m;
long long calc(int st, int en)
{
	return (long long)(n + n + 1 - (en - st)) * (en - st) / 2;
}
pair<int, int> e[MAXM * 2];
int st[MAXM], en[MAXM], p[MAXM];

int main()
{
	int cases;
	cin >> cases;
	for (int tcase = 1; tcase <= cases; ++tcase) {
		cin >> n >> m;
		long long ans = 0;
		for (int i = 0; i < m; ++i)
		{
			scanf("%d%d%d", &st[i], &en[i], &p[i]);
			e[i * 2]  = make_pair(st[i], -p[i]);
			e[i * 2 + 1] = make_pair(en[i], p[i]);
			ans = (ans + calc(st[i], en[i]) * p[i]) % modulo;
		}
		sort(e, e + 2 * m);
		multiset<pair<int ,int> > s;
		long long t0 = 0, t1 = 0;
		for (int i  = 0; i < 2 * m; ++i) 
		{
			if (e[i].second < 0) {
				t0 -= e[i].second;
				s.insert(make_pair(-e[i].first, -e[i].second));
			} else {
				t1 += e[i].second;
				int k = e[i].second;
				while (k > 0)
				{
					pair<int, int> now = *s.begin();
					int tt;
					tt = min(now.second, k);
					k -= tt;
					ans = (ans - calc(-now.first, e[i].first) * tt) % modulo;
					now.second -= tt;
					s.erase(s.begin());
					if (now.second > 0) s.insert(now);
				}
			}
		}
		ans = (ans % modulo + modulo) % modulo;
		cout << "Case #" << tcase << ": " << ans << endl;
	}
	return 0;
}
