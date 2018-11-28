#include <bits/stdc++.h>
using namespace std;
int main() {
	int t, i;
	int cnt = 1;
	scanf("%d", &t);
	while(t--) {
		int n;
		scanf("%d", &n);
		char input[1005];
		int hash[1005];
		scanf("%s", input);
		int sum = 0;
		int ans = 0;
		for(i = 0; i <= n; i++) {
			int num = input[i] - 48;
			if(num != 0) {
				if(sum >= i) {
					sum += num;
				} else {
					int diff = i - sum;
					ans += diff;
					sum += num + diff;
				}	
			}
			
		}
		printf("Case #%d: %d\n", cnt++, ans);
	}
	return 0;
}