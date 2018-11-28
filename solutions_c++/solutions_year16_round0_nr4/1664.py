#include <bits/stdc++.h>

using namespace std;

int TC, K, C, S;
vector<long long> ans;


int main() {
	scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++) {
		scanf("%d %d %d", &K, &C, &S);
		ans.clear();

		// Small dataset
		long long gap = pow(K, C-1);
		for (int i = 0; i <= S; i++) {
			ans.push_back(gap*i + 1);
		}
		
		printf("Case #%d:", tc);
		for (int i = 0; i < S; i++) {
			printf(" %lld", ans[i]);
		}
		printf("\n");
	}
	return 0;
}