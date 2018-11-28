#include <cstdio>

typedef long long lint;

int main() {
	lint N;
	int T, cnt;
	bool seen[10];
	
	scanf("%d", &T);
	
	for (int i = 1; i <= T; i++) {
		scanf("%I64d", &N);
		cnt = 0;
		for (int j = 0; j < 10; j++) {
			seen[j] = false;
		}
		
		lint ans = N;
		
		while (ans) {
			lint tmp = ans;
			
			while (tmp) {
				if (!seen[tmp%10]) {
					cnt++;
				}
				seen[tmp % 10] = true;
				tmp /= 10;
			}
			
			if (cnt == 10) {
				printf("Case #%d: %I64d\n", i, ans);
				break;
			}
			
			ans += N;
		}
		
		if (ans == 0) {
			printf("Case #%d: INSOMNIA\n", i);
		}
	}
	
	return 0;
}