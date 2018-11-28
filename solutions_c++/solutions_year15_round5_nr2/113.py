#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1005;
int T, N, K;
long long sum[MAXN], diff[MAXN], sdiff[MAXN];
long long up[MAXN], down[MAXN];

int main() {
	if(fopen("test.in","r")) {
		freopen("test.in", "r", stdin);
		freopen("test.out", "w", stdout);
	}
	cin >> T;
	for(int t=1; t<=T; ++t) {
		memset(up, 0, sizeof(up));
		memset(down, 0, sizeof(down));
		memset(sdiff, 0, sizeof(sdiff));
		cin >> N >> K;
		long long nsum = N - K + 1;
		for(int i=0; i<nsum; ++i) cin >> sum[i];
		for(int i=0; i<N-K; ++i) diff[i] = sum[i+1] - sum[i];
		for(int i=0; i<N-K; ++i) {
			sdiff[i%K] += diff[i];
			if(sdiff[i%K] > 0) up[i%K] = max(up[i%K], sdiff[i%K]);
			else down[i%K] = min(down[i%K], sdiff[i%K]);
		}
		long long maxdiff = 0;
		for(int i=0; i<K; ++i) {
			maxdiff = max(maxdiff, up[i] - down[i]);
		}
		long long tot = sum[0];
		for(int i=0; i<K; ++i) tot += up[i];
		long long less = 0;
		for(int i=0; i<K; ++i) {
			less += maxdiff - (up[i] - down[i]);
		}
		long long extra = -tot % K;
		if(extra<0) extra += K;
		long long off = 0;
	 	if (extra > less) off = 1;
		cout << "Case #" << t << ": ";
		cout << off + maxdiff << '\n';
	}
}

