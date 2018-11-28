#include <iostream>
#include <cstdio>

using namespace std;

int main() {
	// your code goes here
	int t;
	cin >> t;
	int d;
	for (int x = 1; x <= t; x++) {
		cin >> d;
		int a[d];
		int m, sum;
		scanf("%d", &a[0]);
		m = a[0];
		sum = a[0];
		for (int i = 1; i < d; i++) {
			scanf("%d", &a[i]);
			if (m < a[i]) m = a[i];
			sum += a[i];
		}
		
		int ans = m;
		
		int sm = 0;
		int l = 0, r = sum;
		int i = 5;
		for (int i = 1; i <= sum; i++) {
			sm = 0;
			for (int j = 0; j < d; j++) {
				if (a[j] % i == 0) {
					sm += (a[j]/i) - 1;
				} else {
					sm += a[j]/i;
				}
			}
			if (ans > sm + i) {
				ans = sm + i;
			}
		}
		
		
		printf("Case #%d: %d\n", x, ans);
	}
	return 0;
}