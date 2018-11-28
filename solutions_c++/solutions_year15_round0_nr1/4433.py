#include <stdio.h>

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, m;
	scanf("%d", &t);
	for (m = 0; m < t; m++){
		int n, i, sum = 0, add = 0;
		char shy[1005];
		scanf("%d %s", &n, shy);
		for (i = 0; i <= n; i++){
			if (sum < i){
				add += i - sum;
				sum = i;
			}
			sum += shy[i] - '0';
		}
		printf("Case #%d: %d\n", m + 1, add);
	}
	return 0;
}