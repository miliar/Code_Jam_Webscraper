#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int main() {
	int t;
	scanf("%d\n", &t);
	
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		int n;
		scanf("%d", &n);
		int count[2501];
		memset(count, 0, sizeof(count));
		int tmp;
		for (int j = 0; j < 2*n-1; j++) {
			for (int k = 0; k < n; k++) {
				scanf("%d", &tmp);
				count[tmp]++;
			}
		}
		bool first = true;
		for (int j = 1; j <= 2500; j++) {
			if (count[j] & 1) {
				if (first) {
					printf("%d", j);
					first = false;
				} else {
					printf(" %d", j);
				}
			}
		}
		printf("\n");
	}
	
	return 0;
}