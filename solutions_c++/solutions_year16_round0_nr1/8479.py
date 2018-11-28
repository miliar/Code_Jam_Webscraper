#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
bool found[10];
int main() {
	int T; scanf("%d", &T);
	ll ans = 0, temp, t, counter = 0, n;
	for(int TT = 1; TT <= T; ++TT) {
		printf("Case #%d: ", TT);
		scanf("%I64d", &n);
		if(n == 0) {
			puts("INSOMNIA");
			continue;
		}
		ans = 0, counter = 0;
		memset(found, 0, sizeof found);
		while(true) {
			ans += n;
			temp = ans;
			while(temp) {
				t = temp%10;
				if(!found[t]) {
					found[t] = true;
					++counter;
				}
				temp/=10;
			}
			if(counter == 10)
				break;
		}
		printf("%I64d\n", ans);
	}
	return 0;
}
