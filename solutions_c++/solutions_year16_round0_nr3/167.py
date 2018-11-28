#include <cstdio>

int main(){
	int cas;
	scanf("%d", &cas);
	for (int casi = 1; casi <= cas; ++casi){
		printf("Case #%d:\n", casi);

		int n, J;
		scanf("%d%d", &n, &J);
		for (int i = 0; i < J; ++i){
			putchar('1');
			for (int j = n - 4 >> 1; j >= 0; --j){
				putchar('0' + (i >> j & 1));
				putchar('0' + (i >> j & 1));
			}
			putchar('1');
			for (int j = 2; j <= 10; ++j)
				printf(" %d", j & 1 ? 2 : j + 1);
			puts("");
		}
	}
	return 0;
}
