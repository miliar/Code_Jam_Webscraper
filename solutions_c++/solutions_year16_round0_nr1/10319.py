#include <bits/stdc++.h>

using namespace std;

int mask, LIM;

int main() {
	int cases;
	char str[20];
	LIM = (1 << 10) - 1;
	scanf("%d", &cases);
	for(int cc = 1; cc <= cases; cc++) {
		int n;
		scanf("%d", &n);
		printf("Case #%d: ", cc);
		if(n == 0) {
			puts("INSOMNIA");
		} else {
			long long res, cnt = 1;
			mask = 0;
			while(mask != LIM) {
				res = n * cnt;
				sprintf(str, "%lld", res);
				for(int i = 0; str[i]; i++) {
					int d = str[i] - 48;
					mask = mask | (1 << d);
				}
				cnt++;
			}
			printf("%lld\n", res);
		}
	}
	return 0;
}