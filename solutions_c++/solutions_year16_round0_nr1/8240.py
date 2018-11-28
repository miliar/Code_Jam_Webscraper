#include <bits/stdc++.h>

typedef long long lint;

int main() {
	int tc;
	
	scanf("%d",&tc);
	for(int t = 1; t <= tc; t++) {
		lint n;
		bool flag[10];
		
		scanf("%lld",&n);
		memset(flag, 0, sizeof flag);
		
		if(n == 0ll) printf("Case #%d: INSOMNIA\n",t);
		else {
			int req = 10;
			for(int i = 1; i; i++) {
				lint x = n * i, pow10 = 1;
				
				while(pow10 <= x) {
					int digit = (x % (pow10 * 10)) / pow10;
					pow10 *= 10;
					
					req -= (flag[digit] == false);
					flag[digit] = true;
				}
				
				if(req == 0) {
					printf("Case #%d: %lld\n",t,x);
					break;
				}
			}
		}
	}
	
	return 0;
}
