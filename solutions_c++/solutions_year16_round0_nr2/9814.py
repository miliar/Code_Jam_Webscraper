#include <stdio.h>
#include <string.h>

int main () {

	int T;
	scanf("%d", &T);

	for(int i = 1; i <= T; ++i) {
		int temp[101] = {0, };
		char pancake[101];

		scanf("%s", &pancake);

		int N = strlen(pancake);

		for(int j = 0; j < N; ++j) {
			if(pancake[j] == '+') {
				temp[j] = 1;
			}
		}

		int result = 0;

		N--;
		while(N >= 0) {
			if(temp[N] == 0) {
				if(temp[0] == 1) {
					for(int j = 0; temp[j] == 1; ++j) {
						temp[j] ^= 1;
					}
					result++;
				}
				else {
					for(int j = 0, k = N; j <= N/2; ++j, --k) {
						int t = temp[j];
						
						temp[j] = temp[k]^1;
						temp[k] = t^1;
					}
					result++;
				}
			}
			else {
				N--;
			}
		}

		printf("Case #%d: %d\n", i, result);
	}
	
	return 0;
}