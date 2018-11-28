#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define maxHeight 2505

int main() {
	int test;
	scanf("%d\n", &test);
	for(int t=0; t<test; t++) {
		int n;
		scanf("%d\n", &n);
		int heightN[maxHeight];
		memset(heightN, 0, sizeof(int)*(maxHeight));
		int tmp;
		for(int i=0; i<(2*n-1); i++) {
			for(int j=0; j<n; j++) {
				scanf("%d", &tmp);
				heightN[tmp] += 1;
			}
		}
		int ans = 0;
		printf("Case #%d:", t+1);
		for(int i=1; i<maxHeight; i++) {
			if(ans == n)
				break;
			if((heightN[i]%2) == 1) {
				printf(" %d", i);
				ans += 1;
			}
		}
		printf("\n");
	}

	return 0;
}
