#include <cstdio>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	freopen("r1a\\B-large.in", "r", stdin);
	freopen("r1a\\B-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int N=1; N<=T; ++N) {
		map<int, int> cnt;
		int n;
		scanf("%d", &n);
		for (int c=0; c<2*n-1; ++c) {
			for (int i=0; i<n; ++i) {
				int x;
				scanf("%d", &x);
				++cnt[x];
			}
		}
		vector<int> ans;
		for (auto &kv : cnt)
			if (kv.second & 1)
				ans.push_back(kv.first);
		sort(ans.begin(), ans.end());
		printf("Case #%d:", N);
		for (int i=0; i<n; ++i)
			printf(" %d", ans[i]);
		puts("");
	}
}
