#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#define N 1002
#define inf 1000000000
using namespace std;
int T, D;
int P[N];
int main() {
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin>>T;
	int maxP = 0;
	for (int cas = 1; cas <= T; ++cas) {
		cin>>D;
		for (int i = 0; i < D; ++i) {
			cin>>P[i];
			maxP = max(maxP, P[i]);
		}
		int ans = inf;
		for (int i = 1; i <= maxP; ++i) {
			int tot = 0;
			int maxE = 0;
			for (int j = 0; j < D; ++j) {
				if (P[j] > i) {
					maxE = max(maxE, i);
					int q = (P[j] - i) / i;
					int r = (P[j] - i) % i;
					tot += (q + (r > 0));
				} else {
					maxE = max(maxE, P[j]);
				}
			}
			ans = min(ans, maxE + tot);
		}
		printf("Case #%d: ", cas);
		cout<<ans<<endl;
	}
	return 0;
}
