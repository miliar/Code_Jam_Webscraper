#include <stdio.h>

int main(void){
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int testcase = 1; testcase <= T; ++testcase){
		int K, C, S;
		scanf("%d %d %d", &K, &C, &S);
		printf("Case #%d: ", testcase);
		for (int i = 0; i < S; i++){
			long long int n = i;
			for (int j = 1; j < C; j++){
				n = n*K + i;
			}
			printf("%lld ", n + 1);
		}
		printf("\n");
	}
	return 0;
}