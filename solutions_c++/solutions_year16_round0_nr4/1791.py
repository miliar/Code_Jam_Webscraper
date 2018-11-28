#include <cstdio>

int main()
{
	int T;	scanf("%d", &T);
	int K, C, S, ans;
	for(int i = 0; i < T; ++i) {
		scanf("%d%d%d", &K, &C, &S);
		if(K == 1) {
			ans = 1;
		} else if(C == 1) {
			ans = K;
		} else {
			ans = K - 1;
		}
		
		if(ans > S) {
			printf("Case #%d: IMPOSSIBLE\n", i + 1);
		} else {
			if(K == 1) {
				printf("Case #%d: 1\n", i + 1);
			} else if(C == 1) {
				printf("Case #%d:", i + 1);
				for(int i = 1; i <= K; ++i)
					printf(" %d", i);
				puts("");
			} else {	// C != 1
				printf("Case #%d:", i + 1);
				for(int i = 2; i <= K; ++i)
					printf(" %d", i);
				puts("");
			}
		}
	}
	return 0;
}