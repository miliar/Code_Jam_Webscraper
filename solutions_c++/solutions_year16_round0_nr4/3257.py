#include <cstdio>
#include <cstdlib>

int main(){
	int t;
	scanf("%d", &t);
	for(int u; u < t; u++){
		printf("Case #%d:", u+1);
		int k, c, s;
		scanf("%d %d %d", &k, &c, &s);
		for(int i = 1; i <= k; i++){
			printf(" %d", i);
		}
		printf("\n");
	}
	return 0;
}
