#include<bits/stdc++.h>

using namespace std;

int main() {
	int t;
	scanf("%d", &t);
	for (int T = 1; T <= t; T++) {
		int n;
		long long m;
		scanf("%d %lld", &n, &m);
		
		printf("Case #%d: ", T);
		if (m > (1ll << (n - 2))) {
			printf("IMPOSSIBLE\n");
			
			continue;
		}
		
		printf("POSSIBLE\n");
		m--;
		printf("0");
		for (int i = 1; i < n - 1; i++) printf("%lld", (m >> (n - 2 - i)) & 1);
		printf("1\n");
		for (int i = 1; i < n; i++) {
			for (int j = 0; j <= i; j++) printf("0");
			for (int j = i + 1; j < n; j++) printf("1");
			printf("\n");
		}
	}
	
	return 0;
}
