#include <bits/stdc++.h>

using namespace std;
#define For(i,l,r) for (int i = l; i <= r; ++i)

int K, C, S;
int main() {
	int T; cin >> T;
	For(TK,1,T) {
		printf("Case #%d: ", TK);
		scanf("%d%d%d", &K, &C, &S);
		int cnt = 0;
		vector<long long> ans;
		for (int i = 0; i < K; i += C) {
			int nex = min(C, K - i);
			long long res = 0;
			for (int j = 0; j < nex; ++j) res = res * K + i + j;
			ans.push_back(res + 1);
		}
		if (ans.size() > S) puts("IMPOSSIBLE");
		else {
			For(i,1,ans.size()) cout << ans[i - 1] << ' ';
			puts("");
		}
	}
	return 0;
}