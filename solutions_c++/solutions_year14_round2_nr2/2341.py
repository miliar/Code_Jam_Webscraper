#include <stdio.h>
#include <string.h>
int a, b, k;
int main(){
	int t, tc = 1;
	for(scanf("%d", &t); tc <= t; tc++) {
		scanf("%d%d%d", &a, &b, &k);
		int ans = 0;
		for(int i = 0; i < a; i++)
			for(int j = 0; j < b; j++)
				if((i&j) < k) ans++;
		printf("Case #%d: %d\n", tc, ans);
	}
	return 0;
}
