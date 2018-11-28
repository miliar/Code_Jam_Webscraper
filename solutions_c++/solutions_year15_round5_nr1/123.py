#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1000005;
int T, N, D, as, am, cs, cm, rs, rm;
long long s[MAXN], m[MAXN];
long long e[MAXN];
long long mins[MAXN], maxs[MAXN];

int main() {
	if(fopen("test.in","r")) {
		freopen("test.in", "r", stdin);
		freopen("test.out", "w", stdout);
	}
	cin >> T;
	for(int t=1; t<=T; ++t) {
		memset(e, 0, sizeof(e));
		cin >> N >> D;
		cin >> s[0] >> as >> cs >> rs;
		cin >> m[0] >> am >> cm >> rm;
		for(int i=1; i<N; ++i) {
			s[i] = (s[i-1] * as + cs) % rs;
			m[i] = (m[i-1] * am + cm) % rm;
		}
		for(int x=0; x<N; ++x) {
			long long low = x ? s[0] + mins[m[x]%x] : s[0];
			long long high = x ? s[0] + maxs[m[x]%x] : s[0] + D;
			low = max(low, s[x]);
			high = min(high, s[x] + D);
			mins[x] = low - s[0];
			maxs[x] = high - s[0];
			if(low <= high) {
				++e[mins[x]];
				--e[maxs[x] + 1];
			}
		}
		long long best = 0;
		for(int i=0; i<=D; ++i) {
			e[i+1] += e[i];
			best = max(best, e[i]);
		}
		cout << "Case #" << t << ": ";
		cout << best << '\n';
	}
}

