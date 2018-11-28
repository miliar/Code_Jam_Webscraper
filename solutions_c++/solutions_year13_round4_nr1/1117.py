#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <functional>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

int main(int argc, char *argv[])
{
	int T;
	cin >> T;
	for (int ti = 1; ti <= T; ti++) {
		int N, M;
		cin >> N >> M;
		map<pair<int, int>, int> m;
		for (int i = 0; i < M; i++) {
			int o, e, p;
			cin >> o >> e >> p;
			m[make_pair(o, e)] += p;
		}
		long long ans = 0;

		for ( ; ; ) {
			vector<pair<int, int> > a;
			map<pair<int, int>, int>::iterator it;
			for (it = m.begin(); it != m.end(); ++it)
				if (it->second > 0)
					a.push_back(it->first);

			bool found = false;
			for (int i = 0; i < a.size(); i++) {
				for (int j = i + 1; j < a.size(); j++) {
					if (a[j].first <= a[i].first) continue;
					if (a[j].second <= a[i].second) continue;
					if (a[i].second >= a[j].first) {
						int t = a[i].second - a[j].first;
						long long x = ((long long) (a[i].second - a[i].first - t)) * ((long long) (a[j].second - a[j].first - t));
						long long c = min(m[a[i]], m[a[j]]);
						ans += c * x;
						m[a[i]] -= c; m[a[j]] -= c;
						m[make_pair(a[i].first, a[j].second)] += c;
						m[make_pair(a[j].first, a[i].second)] += c;
						found = true;
						break;
					}
				}
				if (found) break;
			}
			if (!found) break;
		}

		printf("Case #%d: %lld\n", ti, ans);
	}
	return 0;
}
