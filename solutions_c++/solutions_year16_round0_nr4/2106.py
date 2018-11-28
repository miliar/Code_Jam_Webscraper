#include<bits/stdc++.h>
using namespace std;

long long ans[100];

int main() {
	int T;
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	scanf("%d",&T);
	for(int tc = 1; tc <= T; tc++) {
		printf("Case #%d: ", tc);
		int K,C,S;
		scanf("%d %d %d",&K,&C,&S);
		if(C * S < K) {
			puts("IMPOSSIBLE");
			continue;
		}
		int bit = K - 1;
		for(int i = 0; i < (K + C - 1)/C; i++) {
			long long num = 0;
			for(int j = 0; j < C && bit >= 0; j++) {
				num = num * K + bit;
				bit--;
			}
			ans[i] = num + 1;
		}
		printf("%lld",ans[0]);
		for(int i = 1; i < (K + C - 1)/C; i++) {
			printf(" %lld",ans[i]);
		}
		puts("");
	}
}




