#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;
typedef long long i64;

int T;
int K, C, S;

int main()
{
	scanf("%d", &T);
	for (int t = 0; t++ < T; ) {
		scanf("%d%d%d", &K, &C, &S);
		printf("Case #%d:", t);
		if (C * S < K) {
			puts(" IMPOSSIBLE");
			continue;
		}
		vector<vector<int> > distr(S, vector<int>(C, 0));
		for (int i = 0; i < K; ++i) {
			distr[i % S][i / S] = i;
		}
		for (int i = 0; i < S; ++i) {
			i64 t = 0;
			for (int j = 0; j < distr[i].size(); ++j) t = t * K + distr[i][j];
			printf(" %lld", t + 1);
		}
		puts("");
	}
	return 0;
}
