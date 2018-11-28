#include <bits/stdc++.h>

using namespace std;

int main(void) {
	int tcase;
	scanf("%d", &tcase);
	for(int _i = 0; _i < tcase; _i++) {
		int n, has[10], ans;
		scanf("%d", &n);
		if(n == 0) {
			printf("Case #%d: INSOMNIA\n", _i+1);
			continue;
		}
		for(int i = 0; i < 10; i++) {
			has[i] = 0;
		}
		ans = n;
		for(int i = 1;; i++) {
			int temp = i*n;
			ans = temp;
			while(temp) {
				has[temp%10] = 1;
				temp /= 10;
			}
			bool ff = true;
			for(int k = 0; k < 10; k++) {
				if(has[k] == 0) {
					ff = false;
				}
			}
			if(ff) {
				break;
			}
		}
		printf("Case #%d: %d\n", _i+1, ans);
	}
}
