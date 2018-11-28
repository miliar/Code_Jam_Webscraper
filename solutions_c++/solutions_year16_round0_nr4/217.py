#include<stdio.h>
#include<vector>


int main()
{
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		int K, C, S;
		scanf("%d%d%d", &K, &C, &S);
		if (C * S < K) {
			printf("Case #%d: IMPOSSIBLE\n", t);
			continue;
		}
		std::vector<long long> ans;
		long long cur = 0;
		int i=0;
		for (; i<K; i++) {
			cur *= K;
			cur += i;
			if ((i+1)%C == 0) {
				ans.push_back(cur + 1);
				cur = 0;
			}
		}
		if (i%C != 0) {
			ans.push_back(cur + 1);
		}
		printf("Case #%d:", t);
		for (int i=0; i<ans.size(); i++) {
			printf(" %lld", ans[i]);
		}
		printf("\n");
	}
	return 0;
}