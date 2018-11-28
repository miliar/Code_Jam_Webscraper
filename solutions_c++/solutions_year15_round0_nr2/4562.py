#include <cstdio>
#include <iostream>
#include <algorithm>
#include <deque>
#include <queue>
#include <map>

using namespace std;

#define ll long long

int T, n, a[2000];
int ans;
ll P = 31, p[2000], mod = 1e9 + 7;
map < ll, bool > m;

void go(deque < int > d, int curans = 0) {
	sort(d.begin(), d.end());
	ll hash = 0;

	for(int i = 0; i < d.size(); i++) {
		hash += (p[i] * d[i]) % mod;
		hash %= mod;
	}

	if(m.count(hash))
		return;

	m[hash] = 1;

	int tmpans = 0;

	for(int i = 0; i < d.size(); i++) 
	 	tmpans = max(tmpans, d[i]);
	
	ans = min(ans, tmpans + curans);

	for(int i = 0; i < d.size(); i++) {
		if(d[i] > 3) {
			int tmp = d[i];

			for(int j = 2; j <= d[i] - 2; j++) {
				d[i] = j;
				d.push_back(tmp - j);
				go(d, curans + 1);
				d.pop_back();
				d[i] = tmp;
			}
		}
	}
}

int main() {
	scanf("%d", &T);
	
	p[0] = 1;
	for(int i = 1; i < 100; i++) {
		p[i] = (p[i - 1] * P) % mod;
	}

	for(int t = 1; t <= T; t++) {
		scanf("%d", &n);

		deque < int > d;
		m.clear();

		for(int i = 0; i < n; i++) {
			scanf("%d", &a[i]);
			d.push_back(a[i]);
		}

		ans = (1 << 20);

		go(d);

		printf("Case #%d: %d\n", t, ans);
	}

	return 0;
}