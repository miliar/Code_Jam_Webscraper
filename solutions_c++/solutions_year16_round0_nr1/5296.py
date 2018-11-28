#include <stdio.h>
int N;
int main(void){
	int T;
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for (int testcase = 1; testcase <= T; ++testcase){
		scanf("%d", &N);
		printf("Case #%d: ", testcase);
		if (N == 0){
			printf("INSOMNIA\n", N);
			continue;
		}
		int chk = 0;
		int name;
		for (int i = 1; i < 100 && chk < 1023; ++i){
			name = N*i;
			while (name){
				chk = chk | (1 << (name % 10));
				name /= 10;
			}
			name = N*i;
		}
		printf("%d\n", name);
	}
	return 0;
}