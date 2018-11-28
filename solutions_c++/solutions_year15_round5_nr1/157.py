#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <stack>
using namespace std;

#define mp(a,b) make_pair(a, b)

long long ss[1000006];
long long smin[1000006];
long long smax[1000006];

pair<long long, long long> v[1000006];
int q[2000005];



void Solve() {
	int n, d;
	long long s0, as, cs, rs;
	long long m0, am, cm, rm;
	cin >> n >> d;
	cin >> s0 >> as >> cs >> rs;
	cin >> m0 >> am >> cm >> rm;
	ss[0] = s0;
	smin[0] = s0;
	smax[0] = s0;
	long long s = s0;
	long long m = m0;
	for (int i = 1; i < n; ++i) {
		s = (s * as + cs) % rs;
		m = (m * am + cm) % rm;
		int man = m % i;
		ss[i] = s;
		smin[i] = min(s, smin[man]);
		smax[i] = max(s, smax[man]);
	}
	for (int i = 0; i < n; ++i) {
		v[i] = make_pair(smin[i], smax[i]);
	}
	sort(v, v + n);
	int l = 0, r = 0;
	int ret = 0;


	int sum = 0;
	memset(q, 0, sizeof q);
	while (l < n && v[l].first < s0 - d) {
		++l;
	}
	r = l;
	for (int i = s0 - d; i <= s0; ++i) {
		sum += q[i + d];
		while (l < n && v[l].first < i) {
			--q[v[l].second];
			if (v[l].second <= i + d) {
				--sum;
			}
			++l;
		}
		while (r < n && v[r].first <= i + d) {
			++q[v[r].second];
			if (v[r].second <= i + d) {
				++sum;
			}
			++r;
		}
		ret = max(ret, sum);
	}
	cout << ret << endl;
}


int main() {
	freopen("a_large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int I = 0; I < T; ++I) {
		printf("Case #%d: ", I + 1);
		Solve();
	}
	return 0;
}