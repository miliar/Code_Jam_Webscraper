#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	scanf("%d", &t);
	
	for (int i = 1; i <= t; ++i) {
		long long n;
		scanf("%lld", &n);
		
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", i);
			continue;
		}
		
		long long x = n;
		
		int visited = 0;
		
		while (true) {
			long long t = x;
			if (t == 0) visited |= 1;
			while (t) {
				int digit = t % 10;
				visited |= (1 << digit);
				t /= 10;
			}
			
			if (visited == 1023) break;
			x += n;
		}
		
		printf("Case #%d: %d\n", i, x);
	}
	return 0;
}